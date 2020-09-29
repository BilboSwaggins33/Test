def MaxSubarray(l):
    if allnegative(l):
        largest = l[0]
        for elem in l:
            if elem > largest:
                largest = elem
    else:
        largest = 0
        sum = 0
        for num in l:
            sum += num
            if sum < 0:
                sum = 0
                continue
            if sum > largest:
                largest = sum
    return largest

def allnegative(l):
    for num in l:
        if num > 0:
            return False
    return True

print(MaxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
