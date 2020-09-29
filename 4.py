import random

def monasort(x):
    swaps = 1
    while swaps != 0:
        swaps = 0
        for i in range(0, len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i+1] = x[i+1],x[i]
                swaps = swaps + 1
    return x

l = []
for i in range(0, 15):
    l.append(random.randint(0, 100))
print(l)
print(monasort(l))
