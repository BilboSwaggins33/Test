#NON-RECURSIVE SOLUTION (works only for bases less than ten)
def numlength(num, base):
    i = 0
    while base ** i < num:
        i = i + 1
    return i

def ConvertToBase(num, base):
    ans = []
    nlength = numlength(num, base)
    for i in range(nlength):
        ans.append(0)
    for i in range(nlength):
        while num >= base ** (nlength - i - 1):
            num = num - (base ** (nlength - i - 1))
            ans[i] = ans[i] + 1
    return ans





#RECURSIVE SOLUTION (works for bases greater than nine)
def conv(num,b):
    convStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]
b = int(input('Enter base (less than 10):'))
x = int(input('Enter num:'))
print(ConvertToBase(x, b))
#print(conv(x, b))
