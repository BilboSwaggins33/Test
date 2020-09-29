#PROGRAM TO FIND SUM OF LIST OF NUMBERS,THEN
#THE PRODUCT OF THE SUM'S DIGITS, REPEATS UNTIL
#ONLY ONE DIGIT
import random
def pds(x):
    sum = 69
    while len(str(sum)) != 1:
        sum = 0
        #does sum
        for i in range(len(x)):
            sum = sum + int(x[i])
        #clears x
        x = []
        #sets x to sum
        for i in str(sum):
            x.append(i)
        #finds product of digits
        product = 1
        for i in range(len(x)):
            product = product * int(x[i])
        #clear x
        x = []
        #sets x to product
        for i in str(product):
            x.append(i)
    return x[0]

l = []
for i in range(10):
    l.append(random.randint(1, 50))
print(l)
print(pds(l))
