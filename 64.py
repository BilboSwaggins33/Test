#*Smallest Integer Divisible by K
#Given a positive integer K, you need to find the smallest
#positive integer N such that N is divisible by K,
#but N only contains the digit 1
def sidbk(k):
    num = [1]
    for i in range(k):
        num2 = ''
        for i in range(len(num)):
            num2 = num2 + str(num[i])
        if int(num2) % k == 0:
            return len(num)
        else:
            if int(num2) % k != 0:
                num.append(1)
    return -1

print(sidbk(10))
