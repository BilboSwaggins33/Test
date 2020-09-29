#FINDS MISSING NUMBER
#IN A LIST OF CONSECUTIVE
#INTEGERS (RANDOM)
#USES O(n) COMPLEXITY AND
#O(1) EXTRA SPACE COMPLEXITY
#USES MEAN TO FIND MISSING NUMBER
def fmn(x, m):
    sum = 0
    gmean = 0
    for i in range(x):
        if i != m:
            print(i)
            sum = sum + i
        gmean = gmean + i
    gmean = gmean / x
    ans = (gmean * (x)) - sum
    return ans

while True:
    x = int(input('Enter n:'))
    m = int(input('Enter missing number:'))
    print('The missing number is:', fmn(x, m))
