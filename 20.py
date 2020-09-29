#history program; records history in list h
#records any undos into r, which allows for redos
h = []
r = []
while True:
    print('Commands: undo, redo, else')
    choice = input(">>>")
    if choice == 'undo':
        try:
            #pops from history list into redo list
            x = h.pop(len(h)-1)
            print(x)
            r.append(x)
        except:
            print('Error: Nothing to undo')
    elif choice == 'redo':
        #pops from redo list into history list
        try:
            x = r.pop(len(r) - 1)
            print(x)
            h.append(x)
        except:
            print('Error: Nothing to redo')
    else:
        #add input to history
        h.append(choice)
