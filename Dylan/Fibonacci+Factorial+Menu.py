
#FACTORIAL TUGAS
def factorial():
    print("Factorial Calculator!")
    print("\n")
    a = 1
    enter_number = int(input("Please insert a Number: "))
    if enter_number < 0:
        print("Error! Please enter a positive number above 0!")
        enter_number = int(input("Please insert a Number: "))
    elif enter_number == 0:
        print(f"Factorial of {enter_number}! is 1")
    elif enter_number == 1:
        print(f"Factorial of {enter_number}! is 1")
    else:
        b = enter_number
        c = enter_number
        while a < enter_number:
            c = c * (b - 1)
            a += 1
            b -= 1
        print(f"Factorial of {enter_number}! is {c}")

#Fibonacci Sequence
def ask():
    try:
        enter_number = int(input("Fibonacci: "))
        number = enter_number
        if enter_number == 1:
            print("1")
        elif enter_number <= 0:
            print("Invalid, must be above 0!")
    except:
        print("Invalid, must be a number!")
    a = 0
    b = 1
    c = 1
    print("\n")
    print(f"Fionacci({enter_number}), Result:")
    while a < enter_number:
        print(b, end=", ")
        d = b + c #d = 3
        b = c #b = 1
        c = d #c = 2
        a += 1 #a = 1



def main_menu():
    print("Tugas Compsci by Dylan 11F")
    print("Menu: Factorial (1) or Fibonacci (2)")
    try:
        menu = int(input("> "))
        if menu == 1:
            factorial()
        elif menu == 2:
            ask()
        else:
            print("Invalid, must be 1 or 2")
    except:
        print("Invalid, must be 1 or 2!")

main_menu()
