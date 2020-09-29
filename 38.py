def countprimes(x):
    ans = []
    i = 0
    while i < x:
        if prime(i):
            ans.append(i)
        i = i + 1
    return ans
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
x = int(input('>>>'))
print(countprimes(x))
