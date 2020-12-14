container = [["In The Deep Blue Ocean","The Stranger","Polly wants a cracker"],
             ["The Secret of Monkey Island"],
             ["A Good Leader is A Good Servant","The Quest of Rosetta","Le Chuck’s Revenge"],
             ["The Bloody Hell Mary","The Lost Necklace", "The Magical Season of Christmas"],
             ["Sherlock Holmes", "Graduation Day"]]

def show_containers(container):
    revcon1 = ", ".join(container[0][::-1])
    revcon2 = ", ".join(container[1][::-1])
    revcon3 = ", ".join(container[2][::-1])
    revcon4 = ", ".join(container[3][::-1])
    revcon5 = ", ".join(container[4][::-1])

    print("Here are the containers books are in sequential order from top to bottom\n")
    print(f"Container 1: {revcon1}")
    print(f"Container 2: {revcon2}")
    print(f"Container 3: {revcon3}")
    print(f"Container 4: {revcon4}")
    print(f"Container 5: {revcon5}")

def mover(container, origin, destination):
    item = container[origin - 1][-1]
    container[destination - 1].append(container[origin - 1][-1])
    container[origin - 1].pop()
    print(f"Moved {item} from Container {origin} to Container {destination}")

def main():
    a = True
    while a:
        print("\n" * 3)
        show_containers(container)
        print(" ")


        print("To move a book")
        while True:
            origin = (int(input("Origin container number: ")))
            if len(container[origin - 1]) < 1:
                print("Container is empty\n")
            else: break

        while True:
            destination = (int(input("Destination container number: ")))
            if len(container[destination - 1]) == 3:
                print("Container is full\n")
            else: break

        mover(container, origin, destination)



main()
