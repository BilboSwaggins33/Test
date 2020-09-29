def compliment(x):
    x2 = bin(int(x)).replace("0b","")
    l = [str(i) for i in str(x2)]
    for i in range(len(l)):
        if l[i] == '1':
            l[i] = '0'
        elif l[i] == '0':
            l[i] = '1'
    x = ''.join(l)
    return int(x, 2)

x = input('Enter num:')
print(compliment(x))
