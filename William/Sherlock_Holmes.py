import pip
pip.main(['install', 'tabulate'])

import random
from tabulate import tabulate

container = [["In The Deep Blue Ocean","The Stranger","Polly wants a cracker"],                     
             ["The Secret of Monkey Island"],                                                       
             ["A Good Leader is A Good Servant","The Quest of Rosetta","Le Chuck’s Revenge"],
             ["The Bloody Hell Mary","The Lost Necklace", "The Magical Season of Christmas"],
             ["Sherlock Holmes", "Graduation Day"]]

def show_containers(container):

    p_container = [[1,2,3,4,5],
                   [1,2,3,4,5],
                   [1,2,3,4,5]] 

    for i in range(5):
        if len(container[i]) == 3:
            p_container[2][i] = container[i][0]
            p_container[1][i] = container[i][1]
            p_container[0][i] = container[i][2]
        
        elif len(container[i]) == 2:
            p_container[2][i] = container[i][0]
            p_container[1][i] = container[i][1]
            p_container[0][i] = ""

        elif len(container[i]) == 1:
            p_container[2][i] = container[i][0]
            p_container[1][i] = ""
            p_container[0][i] = ""

        elif len(container[i]) == 0:
            p_container[2][i] = ""
            p_container[1][i] = ""
            p_container[0][i] = ""
            pass

    p_header = ["Container 1", "Container 2", "Container 3", "Container 4", "Container 5"]

    print(tabulate(p_container, headers = p_header))
    print("\nObjective:\n",
        "1. Sherlock Holmes --> Bottom of Container 4\n",
        "2. The Stranger--> Top of Container 2\n",
        "3. The Lost Necklace --> Bottom of Container 1")

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
    counter = 0
    while True:
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
        counter += 1

        if complete(container):
            print("SUCCESS ALL BOOKS ARE IN THE CORRECT PLACES")  
            print(f"Done in {counter} moves")    
            break

if __name__ == "__main__":
    main()
