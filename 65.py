#recursive FUNCTION
def f(x):
    if x < 3:
        return x - f(x+1)
    if 3 <= x < 5:
        return x * 2
    else:
        return x + f(x-5)

x = int(input("x:"))
print(f(x))
