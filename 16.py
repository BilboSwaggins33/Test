def cesarcypher(s, x):
    ans = []
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(s)):
        ans.append(alpha[(alpha.index(s[i]) + x) % 26])
    return ''.join(ans)

s = input('String:')
x = int(input('Increment:'))
print(cesarcypher(s, x))
