def palindrome(x):
    #l = [int(i) for i in str(x)]
    x3 = int(str(x)[::-1]) + x
    while x3 != int(str(x3)[::-1]):
        print(x3)
        palindrome(x3)
    return x3

x = int(input("Enter num:"))
print(palindrome(x))
