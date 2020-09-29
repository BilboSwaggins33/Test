#determines if the sum of the prime factors
#are equal, tests both unique factors and
#repeated factors
def ra(n):
    n2 = n + 1
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for i in range(len(pfac(n))):
        s1 = s1 + pfac(n)[i]
    for i in range(len(pfac(n2))):
        s2 = s2 + pfac(n2)[i]
    for i in range(len(iso(pfac(n)))):
        s3 = s3 + iso(pfac(n))[i]
    for i in range(len(iso(pfac(n2)))):
        s4 = s4 + iso(pfac(n))[i]
    if s1 == s2 and s3 != s4:
        return True, 'def1'
    elif s1 != s2 and s3 == s4:
        return True, 'def2'
    elif s1 == s2 and s3 == s4:
        return True, 'def1&def2'
    else:
        return False

def iso(l):
    l2 = []
    x = len(l)
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2

def pfac(x):
    counter = 2
    pfactors = []
    while not prime(x):
        if prime(counter):
            while x % counter == 0:
                x = x // counter
                pfactors.append(counter)
        counter = counter + 1
    if x != 1:
        pfactors.append(x)
    return pfactors

def prime(n):
    if n != 1:
        factors = []
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
        if len(factors) == 1:
            return True
        else:
            return False
    else:
        return True
x = int(input('Enter num:'))
print(ra(x))
