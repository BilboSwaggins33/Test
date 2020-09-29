import random
def checkcow(x, y):
    numc = 0
    for i in range(4):
        if x[i] == y[i]:
            numc = numc + 1
    return numc

#checkbull function kinda haywire
def checkbull(x, y):
    numb = 0
    for i in range(4):
        for j in range(4):
            if i != j:
                if x[i] == y[j]:
                    numb = numb + 1
    return numb


num = str(random.randint(1000, 9999))
while True:
    print("Enter Number (1000 - 9999)")
    g = input(">>>")
    if checkcow(g, num) != 4:
        print("Cows:", checkcow(g, num))
        print("Bulls:", checkbull(g, num))
    else:
        print("You got it!")
        break
