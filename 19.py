def freq(s2):
    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    l = []
    ans = []
    l2 = []
    #creates list full of 0s that will count the frequency of each letter
    for i in range(25):
        l.append(0)
    #finds letter in s, uses that letter to find index in alpha, counts that index in l up by 1
    #therefore counting the letter index
    for i in s:
        if i != ' ':
            l[alpha.index(i)] = l[alpha.index(i)] + 1

    for i in range(len(l)):
        if l[i] != 0:
            ans.append(alpha[i])
            l2.append(i)
    #print(ans)
    #print(l2)
    for i in range(len(ans)):
        x = l2[i]
        print(ans[i] + ":" + str(l[x]))


s = input('Enter word:')
freq(s)
