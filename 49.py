#Two strings are isomorphic if the characters
#in s can be replaced to get t
def isomorphicstrings(s, t):
    number = [int(i) for i in range(len(s))]
    teststring = ''
    key = {}
    for i in s:
        if i not in key:
            key[i] = t[s.index(i)]
    for i in range(len(s)):
        teststring = teststring + key[s[i]]
    if teststring == t:
        return True
    else:
        return False

print('Make sure strings are same length.')
s1 = input('Enter string #1:')
s2 = input('Enter string #2:')
print(isomorphicstrings(s1, s2))
