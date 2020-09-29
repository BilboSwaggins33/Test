#Array has to increase than decrease
#at some point
def ValidMountainArray(arr):
    counter = 0
    if len(arr) < 3:
        return False
    else:
        for i in range(len(arr) - 1):
            if (arr[i] < arr[i + 1] and counter == 0):
                continue
            elif arr[i] > arr[i + 1] and counter == 0:
                counter = counter + 1
            elif arr[i] > arr[i + 1] and counter == 1:
                continue
            else:
                return False
        return True

print(ValidMountainArray([3, 5, 3]))
