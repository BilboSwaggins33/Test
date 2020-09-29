#function to reverse all vowels inside a string
def reversevowels(x):
    l = [str(i) for i in x]
    v = ['a', 'e', 'i', 'o', 'u']
    vs = []
    for i in range(len(l)):
        if l[i] in v:
            vs.append(l[i])
    vs2 = vs[::-1]
    counter = 0
    for i in range(len(l)):
        if l[i] in v:
            l[i] = vs2[counter]
            counter = counter + 1
    return ''.join(l)


x = input('Enter String:')
print(reversevowels(x))
