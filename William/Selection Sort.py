
#Selection Sort Python Program
import random


#Create Random Numbers
def random_numbers(amount):
    num = []
    for i in range (0, amount):
        num.append(random.randint(0,100))
    return num

#Sorting Procedure
def selection_sort(my_numbers):
    repeat = len(my_numbers) #Ammount of passes
    new_number = my_numbers

    #Passes
    for all in range(repeat):
        min_number = my_numbers[all]

        #Looking for minimum
        for i in range(all, repeat):
            if new_number[i] < min_number:

                #Swaping
                min_number = new_number[i]
                new_number[all], new_number[i] = new_number[i], new_number[all]

        print(new_number)

    return(new_number)



def main():
    my_numbers = []

    user_input = int(input("Enter amount of random numbers: "))
    my_numbers = random_numbers(user_input)
    print (f"Random Numbers: {my_numbers}\n")
    print ("=== Start Sorting ===")
    selection_sort(my_numbers)
    print ("=== Finished Sorting ===\n")



main()
