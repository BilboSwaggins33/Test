#Returns indices of two numbers in a list that add
#up to the target value
def twosum(l, t):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == t:
                print(i, j)
                return i, j
    return 'Target not found'

list1 = [1, 5, 2, 3, 7, 5, 8, 9, 10, 13, 12, 11, 15, 18, 21]
target = int(input('Target:'))
print(twosum(list1, target))
