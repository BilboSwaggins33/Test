import random

av = []
x = 0
for i in range(0, 5):
    g = 50
    num = random.randint(1, 100)
    low = 1
    high = 100
    numguesses = 1
    print("The number is:", num)
    while True:
        print("Computer guessed:", g)
        if num > g:
            low = g
        elif num < g:
            high = g
        else:
            print("The computer guessed", numguesses, "times.")
            break
        g = (low+high)//2
        numguesses = numguesses + 1
    av.append(numguesses)

#calculate average amount of guesses
for i in range(0, 5):
    x = x + av[i]
average = x/(len(av))
print("The computer guessed an average of", average, "times.")
