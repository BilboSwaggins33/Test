import random
def check(num1, num2):
    if num1 > num2:
        return "Lower. "
    elif num1 < num2:
        return "Higher."
    elif num1 == num2:
        return "You got it!"
#test
number = random.randint(1, 100)
guesses = 0
while True:
    x = int(input("Guess number:"))
    if check(x, number) != "You got it!":
        print(check(x, number))
        guesses = guesses + 1
    else:
        print(check(x, number))
        print("Guesses:", guesses)
        y = input("Continue?(Y/N)")
        if y == 'Y':
            number = random.randint(1, 100)
            guesses = 0
            continue
        elif y == 'N':
            break
