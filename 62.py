import random
def mintriangle(list):
    row = len(list) - 1
    while row > 0:
        for i in range(row):
            printTriangle(list)
            if list[row][i] >= list[row][i + 1]:
                list[row - 1][i] += list[row][i + 1]
            elif list[row][i + 1] > list[row][i]:
                list[row - 1][i] += list[row][i]
        row = row - 1
    return list[0][0]

def printTriangle(list):
    n = len(list)
    k = 2 * n - 2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k = k - 1

        for j in range(i + 1):
            print(list[i][j], end = ",")
        print("\r")
l = []
r = int(input('Rows:'))
min = int(input('Min Range:'))
max = int(input('Max Range:'))
counter = 1
for i in range(r):
    t = []
    for j in range(counter):
        t.append(random.randint(min, max))
    l.append(t)
    counter = counter + 1
printTriangle(l)
print(mintriangle(l))
