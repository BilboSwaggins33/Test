def convertodec(x):
    return int(x, 2)
def convertobin(x):
    return bin(int(x)).replace("0b","")
def addbinary(x, y):
    return convertobin(convertodec(x) + convertodec(y))
while True:
    x = input('Number 1:')
    y = input('NUmber 2:')
    print(addbinary(x, y))
