
def menu():
    print("Factorial and Fibonacci Sequence Generator \n\n")


    while True:

        #Validation
        try:
            mode = int(input("For factorial type 1, fibonacci type 2, to stop type 0: "))

            if mode == 1: #Factorial
               factorial()
               print("")

            elif mode == 2: #Fibonacci
               fibonacci_sequence()

            elif mode == 0: #Stop
                break

            #Error (Wrong Number)
            else:
               print("Enter either 0, 1 or 2\n")

        #Error (char)
        except ValueError:
            print("Enter a Number \n")

#Factorial Function
def factorial():

    while True:
        try:
            user_input = int(input("Factorial of: "))  # User input

            #Error (Number < 0)
            if user_input < 0:
                print("Number Can't be Negative \n")

            #Approved (Number = 0)
            elif user_input == 0:
                print("Factorial = 1")
                break

            # Approved
            else:
                a = 1
                x = user_input
                y = user_input
                while a < user_input:
                    y = y * (x - 1)
                    a += 1
                    x -= 1

                print(f"Factorial = {y}")
                break

        #Error (char)
        except ValueError:
            print("That is not a number Try again! \n")


#Fibonacci Generator Function
def fibonacci_sequence():
    # Validation
    while True:
        try:
            user_input = int(input("Fibonacci of: "))  # Asking for input

            # ERROR (0 or Negative Value)
            if user_input < 0:
                print("Number Cant be less then 1, Try Again! \n")


            # Approved (input = 1)
            elif user_input == 1:
                print("Sequence = [1] \n")
                break


            # Approved (input > 1)
            else:
                final_Number = [1, 1]  # Final sequence that will be printed out
                for i in range(0, user_input - 2):
                    new_number = final_Number[-1] + final_Number[-2]
                    final_Number.append(new_number)  # Adding new number to the sequence
                print(f"Sequence = {final_Number} \n")
                break

        # ERROR (char)
        except ValueError:
            print("Enter a number, Try Again!\n")

menu()
