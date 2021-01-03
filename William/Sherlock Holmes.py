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
    print(f"Container 5: {revcon5}\n")
    print("Objective:\n1. Sherlock Holmes --> Bottom of Container 4\n2. The Stranger --> Top of Container 2\n3. The Lost Necklace --> Bottom of Container 1")

def mover(container, origin, destination):
    item = container[origin - 1][-1]
    container[destination - 1].append(container[origin - 1][-1])
    container[origin - 1].pop()
    print(f"\n\nMoved {item} from Container {origin} to Container {destination}")
    
def complete(container):
    if len(container[0]) > 0 and len(container[1]) > 0 and len(container[3]) > 0:
        if container[3][0] == "Sherlock Holmes" and container[0][0] == "The Lost Necklace" and container[1][-1] == "The Stranger":
            return True
    else: return False

def main():
    a = True
    while a:
        print("\n")
        show_containers(container)
        print(" ")

        print("To move a book")
        while True:
            origin = (int(input("Origin container number: ")))
            if origin in range(1,6): 
                if len(container[origin - 1]) < 1:
                    print("Container is empty\n")
                else: break
            else:
                print("INVALID CONTAINER NUMBER")

        while True:
            destination = (int(input("Destination container number: ")))
            if destination in range(1,6):
                if len(container[destination - 1]) == 3:
                    print("Container is full\n")
                else: break
            else:
                print("INVALID CONTAINER NUMBER")
        
        mover(container, origin, destination)

        if complete(container):
            print("SUCCESS ALL BOOKS ARE IN THE CORRECT PLACES")
            show_containers(container)
            break

        


if __name__ == "__main__":
    main()
