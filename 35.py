from tkinter import *
from tkinter import messagebox
from random import *
import random
import time
root = Tk()
WIDTH = 1500
HEIGHT = 920
root.geometry('1500x1000')
root.grid()
canvas1 = Canvas(root, width = WIDTH, height = HEIGHT, bg = 'black')
canvas1.pack()
playersize = 25
circles = []
spedx = []
spedy = []
sizes = []
color = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'purple', 'pink', 'aquamarine']

def shiny():
    canvas1.config(bg = random.choice(color))

## button1 = Button(root, text = 'Shiny Mode', command = shiny)## button1.pack()

def collision(coords1, coords2, index1):
    bboxcenter1x = (coords1[0] + coords1[2]) / 2
    bboxcenter1y = (coords1[1] + coords1[3]) / 2
    bboxcenter2x = (coords2[0] + coords2[2]) / 2
    bboxcenter2y = (coords2[1] + coords2[3]) / 2
    radius1 = playersize / 2
    radius2 = sizes[index1] / 2
    dist = ((bboxcenter1x - bboxcenter2x) ** 2) + ((bboxcenter1y - bboxcenter2y) ** 2) ** 0.5
    radius = radius1 + radius2
    if dist < radius:
        return True
    else :
        return False

def comparesizes():
    global playersize
    circles_copy = list(circles)# shiny()
    sizes_copy = list(sizes)
    spedx_copy = list(spedx)
    spedy_copy = list(spedy)

    for i in range(len(circles_copy)):
        try:
            playercircle_bbox = canvas1.coords(player)
            candidate_circle_bbox = canvas1.coords(circles_copy[i])
            if playersize >= sizes_copy[i] and collision(playercircle_bbox, candidate_circle_bbox, i):
                canvas1.delete(circles_copy[i])
                del circles[i]
                del sizes[i]
                del spedx[i]
                del spedy[i]
                playersize = playersize + 2
                canvas1.scale(player, 0, 0, 1.05, 1.05)
            elif playersize < sizes_copy[i] and collision(playercircle_bbox, candidate_circle_bbox, i):
                messagebox.showerror('YOU LOST!!!', 'YOUR NOT GOOD AT THE GAME')
                root.destroy()
        except:
            continue

def createcirc(x, y):
    spped = 4

    size = random.randint(10, 100)
    sizes.append(size)
    circle = canvas1.create_oval(x, y, x - size, y - size, fill = random.choice(color))
    circles.append(circle)
    xd = random.randint(-spped, spped)
    yd = random.randint(-spped, spped)
    while xd == 0 or yd == 0:
        xd = random.randint(-spped, spped)
        yd = random.randint(-spped, spped)
        spedx.append(xd)
        spedy.append(yd)


def move_circle():
    global poos
    poos = random.randint(1, 4)
    if playersize > 100:
        messagebox.showerror("YOU WON!!!", "YOU WON, YOU'RE GOOD AT THE GAME!!!")
        root.destroy()
    for i in range(len(circles)):
        spedx_ = spedx[i]
        spedy_ = spedy[i]
        canvas1.move(circles[i], spedx_, spedy_)

        comparesizes()
        createcirc(spawnx(), spawny())
        root.after(5, move_circle)


def onPress(event = None):
    root.after(5, move_circle)


def spawnx():
    if poos == 1:
        x = random.randint(0, WIDTH + 90)
        return x
    elif poos == 2:
        x = -90
        return x
    elif poos == 3:
        x = random.randint(0, WIDTH + 90)
        return x
    else :
        x = WIDTH + 90
        return x


def spawny():
    if poos == 1:
        y = -90
        return y
    elif poos == 2:
        y = random.randint(0, HEIGHT + 90)
        return y
    elif poos == 3:
        y = HEIGHT + 90
        return y
    else :
        y = random.randint(0, HEIGHT + 90)
        return y


player = canvas1.create_oval(5, 5, 30, 30, fill = 'white')


def handleMotion(event):
    playercoords = canvas1.coords(player)
    playerx = (playercoords[0] + playercoords[2]) / 2
    playery = (playercoords[1] + playercoords[3]) / 2
    canvas1.move(player, event.x - playerx, event.y - playery)


root.bind('<Button-1>', onPress)
root.bind('<Motion>', handleMotion)
for i in range(75):
    circx = random.randint(0, WIDTH)
    circy = random.randint(0, HEIGHT)
    createcirc(circx, circy)

root.mainloop()
