def reverseint(x):
    l = [int(i) for i in str(x)]
    for i in range(len(l)//2):
        temp = l[i]
        l[i] = l[len(l)-i-1]
        l[len(l)-i-1] = temp
    for i in range(len(l)):
        print(l[i], end = '')

x = input('Enter num:')
reverseint(x)
