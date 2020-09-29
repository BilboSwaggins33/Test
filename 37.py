def majority(l):
    ans = []
    l2 = []
    c = []
    for i in l:
        if i not in l2:
            l2.append(i)
    for i in range(len(l2)):
        c.append(0)
    for i in range(len(l)):
        for j in range(len(l2)):
            if l2[j] == l[i]:
                c[j] = c[j] + 1
    for i in range(len(c)):
        if c[i] > len(l) // 2:
            return l2[i]
    return 'null'

print("Type 'x' to stop adding numbers to list.")
x = []
while True:
    ch = input('>>>')
    if ch == 'x':
        print(x)
        print('The majority is', majority(x))
        x = []
    else:
        x.append(int(ch))
        print('List:', x)
