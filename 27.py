import random
def josephus(n, k):
  if n == 1:
    return 1
  else:
    return (k-1 + josephus(n - 1, k)) % n + 1

n = int(input('Enter number of prisoners:'))
k = int(input('Enter number of steps:'))
print(josephus(n, k))
