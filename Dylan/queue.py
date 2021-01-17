def QueueMenu():
  global choice
  print("\nMAIN MENU")
  print("1.Push Data")
  print("2.Pop Queue")
  print("3.View Queue")
  print("4.Empty Queue")
  print("5.Quit")
  choice=int(input("Enter your choice: "))

def ViewStack():
  global maks
  i=maks-1
  while(i>=0):
    print("------")
    if (stack[i]!=0):
      print(stack[i])
    else:
      print('')
    i=i-1

def push(d):
  global top
  if (isFull()):
    print("***ERROR: Stack is Full")
  else:
    top=top+1
    stack[top]=d

def isFull():
  global top,maks
  if (top==maks-1):
    return True
  else:
    return False

def pop():
  global top
  i = 0
  if (isEmpty()):
    print("***ERROR: Stack is Empty")
  else:
    d=stack[0]
    while i < len(stack) - 1:
        stack[i]=stack[i + 1]
        i += 1
    stack[-1] = 0
    top -= 1
    return d

def isEmpty():
  global top
  if (top==-1):
    return True
  else:
    return False

def EmptyStack():
  global top,maks
  top=-1
  i=maks-1
  while(i>=0):
    stack[i]=0
    i=i-1

#mainmodule
stack=[0,0,0,0,0,0,0,0]
maks=8
top=-1
choice=0
while(choice!=5):
  QueueMenu()
  if (choice==1):
    print("Push Data")
    print("==========")
    d=int(input("Input Your Number : "))
    push(d)
  elif (choice==2):
    print("Pop Data")
    print("==========")
    c = pop()
    print(c," has taken from the stack")
  elif (choice==3):
    print("View Stack")
    print("==========")
    ViewStack()
  elif (choice==4):
    print("Empty Stack")
    print("==========")
    print("Stack has been emptied")
    EmptyStack()
  else:
    print("Program ended")
