def mindist(list, center):
    r = 0
    for i in range(len(list)):
        if abs(center - list[i]) > r:
            r = abs(center - list[i])
    return r

x = int(input(('There are ten houses (index 0-9). Which house do you want to place the heater?')))
print('The radius of the heater should be:', mindist([1,2,3,4,5,6,7,8,9],x))
