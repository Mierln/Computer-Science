# Edric Factorial Python

number = int(input("factorial of? "))
while 0 > number:
    print("unidentified")

if number > 0:
    a = 1
    x = number
    result = number
    while a < number:
        result = result * (x - 1)
        a += 1
        x -= 1
    print(f"The factorial of {number} is {result}")

if number == 0:
    print("Factorial of 0 is 1")


# Edric Fibonacci sequence
try:
    number = int(input("Fibonacci? "))
    if 0 > number:
        print("can't be NEGATIVE")

    if number == 0:
        print("0 is REJECTED")

    if number > 1:
        num1 = 1
        num2 = 1
        x = 0
        print("""
your Fibonacci sequence is""")
        while x < number:
            print(num1, end=", ")
            nth = num1 + num2
            num1 = num2
            num2 = nth
            x += 1

except:
    print("NO ALPHABETS")
