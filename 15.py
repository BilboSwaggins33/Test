def expand(num):
    numlist = [int(i) for i in str(num)]
    for i in range(0, len(numlist)):
        for j in range(len(numlist) - i):
            numlist[i] = str(numlist[i]) + '0'

        numlist[i] = str(numlist[i])[:-1]

    return ' + '.join(numlist)

while True:
    x = input("N:")
    print(expand(x))
