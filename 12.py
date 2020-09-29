import random

pp = 0
cp = 0
def compare(x, y):
    global pp
    global cp
    if x == 'r' and y == 'p':
        pp = pp + 1
        return 'You won! Computer chose rock.'
    if x == 'r' and y == 's':
        cp = cp + 1
        return 'You lost! Computer chose rock.'
    if x == 'r' and y == 'r':
        return 'Tied! Computer chose rock.'
    if x == 'p' and y == 'p':
        return 'Tied! Computer chose paper.'
    if x == 'p' and y == 's':
        pp = pp + 1
        return 'You won! Computer chose paper.'
    if x == 'p' and y == 'r':
        cp = cp + 1
        return 'You lost! Computer chose paper.'
    if x == 's' and y == 'p':
        cp = cp + 1
        return 'You lost! Computer chose scissors.'
    if x == 's' and y == 's':
        return 'Tied! Computer chose scissors.'
    if x == 's' and y == 'r':
        pp = pp + 1
        return 'You won! Computer chose scissors.'

bank = ['r', 'p', 's']
while True:
    x = random.choice(bank)
    y = input('r/p/s  >>>  ')
    print(compare(x, y))
    print("Score:", pp, '-', cp)
