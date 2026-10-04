names = [""] * 10
def displaymenu():
    print("1. add name")
    print("2. display list")
    print("3. quit")
    
    choice = int(input("enter your choice: "))
    while choice < 1 or choice > 3:
        print("invalid choice - please re-enter")
        choice = int(input("enter your choice: "))
    return choice

def add_name():
    name = input("what name do you want to add")
    position = int(input("what position on the list do you want it"))
    
    while position < 1 or position > 10:
        print("that is invalid")
        position = int(input("what position on the list do you want it"))
    names[position -1] = name
    
def display_list():
    for i in range(10):
        print(i + 1, names[i])


running = True
while running:
    choice = displaymenu()
    if choice == 1:
        add_name()
    elif choice == 2:
        display_list()
    else:
        print("program has finished")
        running = False