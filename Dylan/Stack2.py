def StackMenu():
    print('Main Menu')
    print('1. Push Data')
    print('2. Pop Data')
    print('3. View Stack')
    print('4. Empty Stack')
    print('5. Quit')
    choice = int(input('Enter your choice: '))

choice = 0
while choice != 5:
    StackMenu()
    if choice == 1:
        print("Push Data")
    elif choice == 2:
        print("Pop Data")
    elif choice == 3:
        print("View Stack")
    elif choice == 4:
        print("Empty Stack")
    else:
        print("Program ended")