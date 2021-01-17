def QueueMenu():
    print("\nMAIN MENU")
    print("1.Push Data")
    print("2.de-queue Data")
    print("3.View queue")
    print("4.Empty queue")
    print("5.Quit")
    

def ViewQueue(my_queue):
    for i in my_queue:
        if i == 0: 
            print("")
            print("-------")
        else:
            print(i)
            print("-------")

def push(my_queue, data):
    for i in range(len(my_queue)):
        if my_queue[i] == 0:
            my_queue[i] = data
            break
        
def isFull(my_queue):
    a = 0
    for i in my_queue:
        if i == 0:
            a = a + 1
    
    if a > 0: return False
    else: return True
    
def pop(my_queue):
    for i in range(len(my_queue)):
        item = my_queue[0]
        for i in range(7):
            my_queue[i] = my_queue[i + 1]
        my_queue[7] = 0
        return item

def isEmpty(my_queue):
    a = 0
    for i in my_queue:
        if i != 0:
            a = a + 1
    
    if a > 0: return False
    else: return True
    
def EmptyQueue():
    return ([0,0,0,0,0,0,0,0])

#mainmodule
my_queue=[0,0,0,0,0,0,0,0] 
choice = 0
while(choice<5):
    QueueMenu()
    choice = int(input("Enter your choice: "))

    if (choice == 1):
        if(isFull(my_queue)):
            print ("*** QUEUE IS FULL ***")
        else:
            print("\nPush Data")
            print("==========")
            data = int(input("Input Your Number : "))
            push(my_queue, data)

    elif (choice==2):
        if isEmpty(my_queue):
            print ("*** QUEUE IS EMPTY ***")
        else:
            print("\nPop Data")
            print("==========")
            c = pop(my_queue)
            print(c," has taken from the stack")

    elif (choice==3):
        print("\nView Queue")
        print("==========")
        ViewQueue(my_queue)

    elif (choice==4):
        print("")
        print("Queue has been emptied")
        my_queue = EmptyQueue()

    else:
        print("Program ended")
