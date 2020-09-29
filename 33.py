def convertbin(x):
    return int(x, 2)
def convertdec(x):
    return bin(int(x)).replace("0b","")
while True:
    print('1.Binary -> Decimal')
    print('2.Decimal -> Binary')
    choice = input('>>>')
    if choice == '1':
        x = input('Enter binary num:')
        print(convertbin(x))
    elif choice == '2':
        x = input('Enter decimal num:')
        print(convertdec(x))
