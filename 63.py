import random
def topKfrequent(l, k):
    l2 = []
    l3 = []
    ans = []
    for i in range(len(l)):
        if l[i] not in l2:
            l2.append(l[i])
    for i in range(len(l2)):
        l3.append(0)
    for i in range(len(l)):
        l3[l2.index(l[i])] = l3[l2.index(l[i])] + 1
    for i in range(len(l3)):
        if l3[i] == k:
            ans.append(l2[i])
    return ans

alphabet = 'abcdefghijklmnopqrstuvwxyz'
list = []
n = int(input('Enter length of list:'))
#r = int(input('Enter range from 0 - '))
k = int(input('k:'))
for i in range(n):
    list.append(random.choice(alphabet))
print(list)
print(topKfrequent(list, k))
