def StackMenu():
    global choice
    print("Main Menu")
    print("1. Push Data")
    print("2. Pop Data")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

def ViewStack():
    global max
    i=max-1
    while(i>=0):
        print ("------")
        if (stack[i]!=0):
            print(stack[i])
        else:
            print("")
        i=i-1

def push(d):
    global top
    if (isFull()):
        print("***ERROR: Stack is FULL")
    else:
        top = top+1
        stack[top] = d

def pop():
    global top
    if (isEmpty()):
        print("***ERROR: Stack is Empty")
    else:
        d = stack[top]
        stack[top] = 0
        top = top-1
        return d

def isFull():
    global top,max
    if(top == max):
        return True
    else:
        return False

def isEmpty():
    global top
    if (top == -1):
        return True
    else:
        return False

def EmptyStack():
    global max, top
    top = -1
    i = max-1
    while(i>=0):
        stack[i]=0
        i = i-1

#mainmodule
stack = [0,0,0]
max = 3
top = -1
choice = 0
while (choice!=3):
    StackMenu()
    if (choice==1):
        print ("Push Data")
        print ("=========")
        d = int(input("Input your number: "))
        push(d)
    elif (choice==2):
        print ("Pop Data")
        print ("========")
        pop()
        print(d," is taken out from the stack")

    else:
        print ("Program ended")
    print(ViewStack())

