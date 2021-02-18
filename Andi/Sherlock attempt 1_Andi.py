def pop():
    global top

    d = stack[choice1][top]
    top = top - 1
    return d

def push():
    global top
    stack[choice2][top] = stack[choice2][top + 1]


def stacks():
    print(f"Stack 0: {stack[0][::-1]}")
    print(f"Stack 1: {stack[1][::-1]}")
    print(f"Stack 2: {stack[2][::-1]}")
    print(f"Stack 3: {stack[3][::-1]}")
    print(f"Stack 4: {stack[4][::-1]}")

stack = [["In The Deep Blue Ocean", "The Stranger", "Polly Wants a Cracker"],
         ["The Secret of Monkey Island"],
         ["A Good Leader Is a Good Servant", "The Quest of Rosetta", "Le Chuck's Revenge"],
         ["The Bloody Hell Mary", "The Lost Necklace", "The Magical Season of Christmas"],
         ["Sherlock Holmes", "Graduation Day"]]

top = 0
r = True
counter = 0

while r == True:
    if stack[0][0] == "The lost necklace" and stack[3][0] == "Sherlock Holmes" and stack[2][2] == "The lost necklace":
        print(stacks())
        print(" ")
        print("All books are in order. YOU'VE WON")
        print(" ")
        print("Finished after " + counter + " tries")
        break
    else:
        stacks()
        choice1 = int(input("Take out book from stack (0~4): "))
        pop()
        print (stack[choice1][top])
        choice2 = int(input("Return book to stack (0~4): "))
        push()
        counter = counter + 1
