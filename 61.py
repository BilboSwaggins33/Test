import random
#looks through list to see if there is
#an a + b + c that adds to 0
#a, b, c are distinct
def sum3(l):
    ans = []
    for a in range(len(l)):
        for b in range(len(l)):
            for c in range(len(l)):
                t = []
                if a != b and a != c and b != c:
                    if l[a] + l[b] + l[c] == 0:
                        t.append(l[a])
                        t.append(l[b])
                        t.append(l[c])
                        if sorted(t) not in ans:
                            ans.append(sorted(t))
    return ans

def main():
    list = []
    while True:
        print('1.Add')
        print('2.Sum3')
        print('3.Randomize')
        choice = int(input('>>>'))
        if choice == 1:
            x = int(input('Num:'))
            list.append(x)
            print(list)
        elif choice == 2:
            print(sum3(list))
            list = []
        elif choice == 3:
            x = int(input('Size:'))
            r = int(input('Range Min:'))
            r2 = int(input('Range Max:'))
            for i in range(x):
                list.append(random.randint(r, r2))
                print(list)
main()
