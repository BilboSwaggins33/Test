import random
def selectionsort(a):
    for j in range(len(a)):
        min = j
        for i in range(j + 1, len(a)):
            if a[min] > a[i]:
                min = i
        a[min], a[j] = a[j], a[min]
    return a

list = []
print(selectionsort(list))
