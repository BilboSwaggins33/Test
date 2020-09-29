#Shortest Unsorted Continuous Subarray
def sucs(l):
    largestindex = 0
    smallestindex = 0
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            smallestindex = i
            break

    for i in range(len(l) - 1, 0):
        print(i)
        if l[i] < l[i - 1]:u
            largestindex = i
            break

    # print(largestindex)
    # print(smallestindex)
    return largestindex - smallestindex

print(sucs([2, 6, 4, 8, 10, 9, 15]))
