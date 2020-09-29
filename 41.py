def sumRange(x, y, l):
    sum = 0
    for i in range(x, y):
        sum = sum + l[i]
    return sum

print("Enter 'x' to stop adding to list.")
list = []
while True:
    c = input('>>>')
    if c == 'x':
        r1 = int(input('Enter low range:'))
        r2 = int(input('Enter high range:'))
        print(sumRange(r1, r2, list))
    else:
        list.append(int(c))
        print(list)
