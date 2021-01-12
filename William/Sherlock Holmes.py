# Where is my Sherlock Holmes project
import pip
pip.main(['install', 'tabulate'])

import random
from tabulate import tabulate

    # 5 Container (from Bottom to Top)
container = [["In The Deep Blue Ocean","The Stranger","Polly wants a cracker"],                     # Reversed Container 1
             ["The Secret of Monkey Island"],                                                       # Reversed Container 2
             ["A Good Leader is A Good Servant","The Quest of Rosetta","Le Chuck’s Revenge"],       # Reversed Container 3
             ["The Bloody Hell Mary","The Lost Necklace", "The Magical Season of Christmas"],       # Reversed Container 4
             ["Sherlock Holmes", "Graduation Day"]]                                                 # Reversed Container 5



    # Reverse the Container (to make it from top to bottom)
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



    # Fuction to move a book from a container to another
def mover(container, origin, destination):

    item = container[origin - 1][-1]                                                    # The book that will be moved
    container[destination - 1].append(container[origin - 1][-1])                        # Adding the book at destination
    container[origin - 1].pop()                                                         # Removing the book from origin

    print(f"\n\nMoved {item} from Container {origin} to Container {destination}")       # Printing the Task
    


    # Check if Objective has been achived
def complete(container):

        #Check if no Containers are empty (error prevention)
    if len(container[0]) > 0 and len(container[1]) > 0 and len(container[3]) > 0:    

            # Check if each book are at the correct place                                                                                                           
        if container[3][0] == "Sherlock Holmes" and container[0][0] == "The Lost Necklace" and container[1][-1] == "The Stranger":

            return True     # Objective achived

    else: return False      # Objective not achived 


    # Main Function
def main():
    counter = 0
    while True:                                                             # Infinite Loop
        print("\n")
        show_containers(container)                                          # Showing Current Container
        print(" ")

        print("To move a book")


        while True:                                                         # Origin
            origin = (int(input("Origin container number: "))) 
            if origin in range(1,6):                                        # Check if input is valid
                if len(container[origin - 1]) < 1:                          # Check if Container is empty
                    print("Container is empty\n")
                else: break
            else:
                print("INVALID CONTAINER NUMBER")

        while True:                                                         # Destination
            destination = (int(input("Destination container number: ")))    
            if destination in range(1,6):                                   # Check if input is valid
                if len(container[destination - 1]) == 3:                    # Check if Destination is full
                    print("Container is full\n")
                else: break
            else:
                print("INVALID CONTAINER NUMBER")
        
        mover(container, origin, destination)                               # If Origin and Destination is valid then call the mover function
        counter += 1

        if complete(container):                                             # Call the complete function to check if objective is achived
            print("SUCCESS ALL BOOKS ARE IN THE CORRECT PLACES")  
            print(f"Done in {counter} moves")    
            break                                                           # If objectives has been achived, break the infinite loop




if __name__ == "__main__":                                                  # Run the Main Fuction
    main()
