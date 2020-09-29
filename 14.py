

def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return("Anagram")
    else:
        return("Not an Anagram")

while True:
    str1 = input("Enter first string:")
    str2 = input("Enter second string:")
    print(anagram(str1, str2))
