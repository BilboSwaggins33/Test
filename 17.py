
def recaman(x):
    sequence = []
    numbers = []
    for i in range(x * x):
        numbers.append(False)
    counter = 1
    index = 0

    numbers[index] = True
    for i in range(x):
        next = index - counter
        if next < 0 or numbers[next]:
            next = index + counter
        numbers[next] = True
        sequence.append(next)
        index = next
        counter = counter + 1
    return sequence


x = int(input("x:"))
print(recaman(x))
