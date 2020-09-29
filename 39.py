def addigits(x):
    if len(str(x)) == 1:
        return 'The answer is:' , x
    else:
        sum = 0
        for i in range(len(str(x))):
            sum = sum + int(str(x)[i])
        print(sum)
        return addigits(sum)
while True:
    x = int(input('Enter two digit number:'))
    print(addigits(x))
