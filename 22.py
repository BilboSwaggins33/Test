#FINDS THE PRIME FACTORIZATION OF NUMBER
def primefactorization(x):
    #COUNTER IS THE SAME AS FACTOR VALUE, TESTS
    #ALL VALUES UNDER NUMBER, IF DIVISIBLE ADD TO
    #PFACTORS LIST
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
    return ' x '.join(str(i) for i in pfactors)

#FUNCTION FINDS IF NUMBER IS PRIME
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
print(primefactorization(x))
