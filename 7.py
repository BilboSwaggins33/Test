def divisorsof(num):
    ans = []
    x = range(1, num)
    for i in x:
        if num % i == 0:
            ans.append(i)

    return ans

while True:
    x = int(input("Enter num:"))
    print(divisorsof(x))
