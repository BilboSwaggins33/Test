#function to determine if at most
#one modification to an array
#can make it become a non-decreasing array
def f(x):
    counter = 0
    for i in range(len(x) - 1):
        if x[i] <= x[i + 1]:
            counter = counter + 1
    if counter < 2:
        return True
    else:
        return False

list = [4, 2, 1]
print(f(list))
