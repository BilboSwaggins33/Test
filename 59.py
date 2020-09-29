#Taken an input, writes it in a ZigZag pattern
#then return in that pattern
#ex. 'PYTHONISLIT' rows: 3
#P   O   L
#Y H N S I
#T   I   T
#RETURNS 'POYHNT'
def ZigZag(string, rows):
    m = []
    for i in range(rows):
        m.append([])

    counter = 0
    dir = 1

    i = 0
    while i < len(string):
        if counter < rows and counter > -1 and dir == 1:
            m[counter].append(string[i])
            counter = counter + dir
            i = i + 1
        elif counter < rows and counter > -1 and dir == -1:
            m[counter].append(string[i])
            counter = counter + dir
            i = i + 1
        elif counter == rows:
            dir = -1
            counter = counter + dir + dir
            #i = i - 1
        elif counter == -1:
            dir = 1
            counter = counter + dir + dir
            #i = i - 1
        else:
            return 'Error'

    return m

def printzigzag(matrix):
    if matrix == 'Error':
        print('Error')
    else:
        for i in matrix:
            for j in i:
                print(j, end = '')




x = input('Enter string:')
rows = int(input('Enter rows:'))
printzigzag(ZigZag(x, rows))
