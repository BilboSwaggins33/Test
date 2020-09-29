# Goat Latin Rules:
# If word begins with vowel, add 'ma' to end of word
# If word begins with consonant, remove first letter
# to end, then add 'ma'
# Add one letter 'a' to end of each word per word index
# ex. First word has one 'a', then second word has 'aa', etc.
def GoatLatin(string):
    s = string.split(' ')
    s2 = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if i[0] in vowels:
            s2.append(i + 'ma')
        else:
            s2.append(i[1:] + i[0] + 'ma')
    for i in range(1, len(s2) + 1):
        ts = s2[i - 1]
        for j in range(i):
            ts = ts + 'a'
        s2[i - 1] = ts
    return ' '.join(s2)

string = input('Enter string:')
print(GoatLatin(string))
