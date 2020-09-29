def palindrome(string):
    if string[::-1] == string:
        return "Palindrome"
    else:
        return "Not a Palindrome"

while True:
    string = input("Enter string:")
    print(palindrome(string))
