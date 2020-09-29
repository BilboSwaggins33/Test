import random

def transposeMatrix(m):
    m2 = []
    for i in range(len(m)):
        t = []
        for j in range(len(m[i])):
            t.append(m[j][i])
        m2.append(t)
    return m2
    
def makeMatrix(x, y):
    matrix = []
    for i in range(y):
        t = []
        for j in range(x):
            t.append(random.randint(0, 99))
        matrix.append(t)
    return matrix

def printMatrix(matrix):
    for i in matrix:
        print(i)
x = int(input('Matrix dimension:'))
y = x
m = makeMatrix(x,y)
printMatrix(m)
printMatrix(transposeMatrix(m))
