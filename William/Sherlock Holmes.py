# Where is my Sherlock Holmes project
import random

    # 5 Container (from Bottom to Top)
container = [["In The Deep Blue Ocean","The Stranger","Polly wants a cracker"],                     # Reversed Container 1
             ["The Secret of Monkey Island"],                                                       # Reversed Container 2
             ["A Good Leader is A Good Servant","The Quest of Rosetta","Le Chuck’s Revenge"],       # Reversed Container 3
             ["The Bloody Hell Mary","The Lost Necklace", "The Magical Season of Christmas"],       # Reversed Container 4
             ["Sherlock Holmes", "Graduation Day"]]                                                 # Reversed Container 5



    # Reverse the Container (to make it from top to bottom)
def show_containers(container):

    revcon1 = ", ".join(container[0][::-1])         # Container 1
    revcon2 = ", ".join(container[1][::-1])         # Container 2
    revcon3 = ", ".join(container[2][::-1])         # Container 3
    revcon4 = ", ".join(container[3][::-1])         # Container 4
    revcon5 = ", ".join(container[4][::-1])         # Container 5

        # Printing the Containers + Objective
    print("Here are the containers books are in sequential order from top to bottom\n")

    print(f"Container 1: {revcon1}")                # Printing Container 1
    print(f"Container 2: {revcon2}")                # Printing Container 2
    print(f"Container 3: {revcon3}")                # Printing Container 3
    print(f"Container 4: {revcon4}")                # Printing Container 4
    print(f"Container 5: {revcon5}\n")              # Printing Container 5

    print("Objective:\n",
        "1. Sherlock Holmes    --> Bottom of Container 4\n",
        "2. The Stranger       --> Top of Container 2\n",
        "3. The Lost Necklace  --> Bottom of Container 1")




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
    for i in range(len(container)):
        random.shuffle(container[i])
    random.shuffle(container)

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
