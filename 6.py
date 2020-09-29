import random

def bridgeshuffle(l1, l2):
    l3 = []
    if len(l1) > len(l2):
        x = len(l1)
    else:
        x = len(l2)

    for i in range(x):
        if i < len(l1):
            l3.append(l1[i])
        if i < len(l2):
            l3.append(l2[i])

    return l3


l1 = []
l2 = []

for i in range(random.randint(1, 5)):
    l1.append(random.randint(0, 10))
for i in range(random.randint(1, 5)):
    l2.append(random.randint(0,10))


print(l1)
print(l2)
print(bridgeshuffle(l1, l2))
