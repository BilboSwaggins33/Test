def plural(s):
    if s[len(s) - 1] == 's':
        return 'plural'
    else:
        return 'not plural'

while True:
    s = input('String:')
    print(plural(s))
