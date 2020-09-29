import random

def pgenerator(x, l):
    alpha = ["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num = []
    password = []
    for i in range(l - 1):
        num.append(str(random.randint(0, x)))
    for i in range(0, l):
        if random.randint(0,1) == 0:
            if random.randint(0, 1) == 0:
                password.append(random.choice(alpha).upper())
            else:
                password.append(random.choice(alpha))
        else:
            password.append(str(random.choice(num)))
    return "".join(password)

x = int(input("Enter complexity:"))
l = int(input("Enter length:"))
print(pgenerator(x, l))
