#Pedro Gallino
#11/20/17
#toDoList.py - Lets people write a to do list

print('Valid Commands Are: add, delete, print, quit')
toDo = []
while True:
    thing = str(input('>'))
    if thing == 'quit':
        break
    elif thing == 'print':
        print(toDo)
        for i in toDo:
            print(i)
    elif thing[0:2] == 'add':
        toDo.append(thing[3:])
    elif thing[0:5] == 'delete':
        toDo.remove[thing[3:]]
        
    
