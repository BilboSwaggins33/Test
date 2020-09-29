def wordpattern(pattern, string):
    slist = string.split(' ')
    plist = [str(i) for i in pattern]
    k = {}
    for i in range(len(plist)):
        if plist[i] not in k:
            k[plist[i]] = slist[i]
    for i in range(len(plist)):
        if k[plist[i]] != slist[i]:
            return False
    return True

p = input('Enter pattern:')
s = input('Enter string:')
print(wordpattern(p, s))
