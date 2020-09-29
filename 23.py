import random
def happyp(x):
    hap = []
    unh = []
    for i in range(len(x)):
        if i == 0:
            if x[i] != x[i + 1]:
                unh.append(x[i])
            else:
                hap.append(x[i])
        elif i == len(x)-1:
            if x[i] != x[i - 1]:
                unh.append(x[i])
            else:
                hap.append(x[i])
        else:
            if x[i] != x[i - 1] and x[i] != x[i + 1]:
                unh.append(x[i])
            else:
                hap.append(x[i])
    print('% of happy:' + str(    (len(hap) / len(x)) * 100  ) + '%'   )
    print('% of unhappy:' + str(   (len(unh) / len(x)) * 100  ) + '%'  )

l = []
for i in range(10):
    l.append(random.randint(0,1))
print(l)
happyp(l)
