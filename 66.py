def rotateleft(l, n):
    l2 = []

    i = n
    while i < len(l):
        l2[i].append(l[n])
    return l2



print(rotateleft([1,2,3], 1))
