#Book Stack
cn = [["In The Deep Blue Ocean", "The Stranger", "Polly wants a cracker"],
       ["The Secret of Monkey Island"],
       ["A Good Leader Is A Good Servant", "The Quest Of Rosetta", "Le Chuck's Revenge"],
       ["The Bloody Hell Mary", "The Lost Necklace", "The Magical Season Of Christmas"],
      ["Sherlock Holmes", "Graduation Day"]]

a = True

def container():
        print(f"Container 1: {cn[0]}")
        print(f"Container 2: {cn[1]}")
        print(f"Container 3: {cn[2]}")
        print(f"Container 4: {cn[3]}")
        print(f"Container 5: {cn[4]}")

def game():
    print("\nWhere's My Sherlock Holmes")
    while a == True:
        print("\n")
        container()

        move_book = int(input("\n Select a container to move the book (Number): "))
        if len(cn[move_book - 1]) < 1:
            print("\nThat container is empty!")
            game()

        move_container = int(input(" Select the container to be moved to (Number): "))
        if len(cn[move_container - 1]) == 3:
            print("\nThat container is full!")
            game()

        else:
            move(move_book, move_container)

def move(book, container):
    cn[container - 1].append(cn[book - 1][-1])
    cn[book - 1].pop()

game()


