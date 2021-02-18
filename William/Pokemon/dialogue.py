import time
import sys
from colorama import Fore, Back, Style


def writen(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def title():
    print("\n" * 3)
    print("".center(50, "="))
    time.sleep(0.75)
    print(" Welcome to Pokémon Lite ".center(50, " "))
    time.sleep(0.75)
    print("".center(50, "="))
    print("\n" * 1)

    writen(Fore.CYAN + 'Are you ready to play? ')
    while True:

        user_input = input(Fore.CYAN + "[Y]/[N] " + Style.RESET_ALL)
        if user_input.upper() == "Y":
            return True
        elif user_input.upper() == "N":
            quit("Thank You For Playing")
        else:
            print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nPlease enter either Y or N" + Style.RESET_ALL + "\n")


def intro(name):
    print("\nProfessor Oak:", end=" ")
    writen(f"Welcome {name} to the world of pokémon\n")
    print("\nProfessor Oak:", end=" ")
    writen("In this world, pokémon are our friends, they can be our pets\n")
    print("\nProfessor Oak:", end=" ")
    writen("Your task will be to explore the pokémon world!\n")
    print("\nProfessor Oak:", end=" ")
    writen("Here is my my grandson Nathan\n")
    print("\n       Nathan:", end=" ")
    writen("Hey, I will help you throughout your journey\n")
    print("\nProfessor Oak:", end=" ")
    writen("Your journey start now, good luck!")
    time.sleep(1)
    print("\n\nProfessor Oak:", end=" ")
    writen("But Wait! You need your own pokémon")
    print("\n\nProfessor Oak:", end=" ")
    writen("I have 3 extra pokémon, go choose 1")


def bulbasaur():
    print("\n\nProfessor Oak:", end=" ")
    writen("Great choice, Bulbasaur is perfect for you")
    print("\n\nProfessor Oak:", end=" ")
    writen("Bulbasaur is a grass type, which means it is strong againts electricity, but weak againts fire")
    print("\n\nProfessor Oak:", end=" ")
    writen("What would be it's name?")
    return input(Fore.CYAN + "\nEnter name: " + Style.RESET_ALL)


def charmander():
    print("\n\nProfessor Oak:", end=" ")
    writen("Great choice, Charmander is amazing")
    print("\n\nProfessor Oak:", end=" ")
    writen("Charmander is a fire type, which means it is strong againts grass, but weak againts water")
    print("\n\nProfessor Oak:", end=" ")
    writen("What would be it's name?")
    return input(Fore.CYAN + "\nEnter name: " + Style.RESET_ALL)


def squirtle():
    print("\n\nProfessor Oak:", end=" ")
    writen("Great choice, Squirtle is great")
    print("\n\nProfessor Oak:", end=" ")
    writen("Squirtle is a water type, which means it is strong againts water, but weak againts electricity")
    print("\n\nProfessor Oak:", end=" ")
    writen("What would be it's name?")
    return input(Fore.CYAN + "\nEnter name: " + Style.RESET_ALL)


def check_first():
    print("\n\nProfessor Oak:", end=" ")
    writen("Here, I give you 3 pokeballs and 3 potions")
    print("\n\nProfessor Oak:", end=" ")
    writen("Each potions will add 45% - 55% of your pokemons full health")
    print("\n\nProfessor Oak:", end=" ")
    writen("Now lets check your new pokémon")


def first_battle():
    time.sleep(2)
    print("\n\nProfessor Oak:", end=" ")
    writen("It's time for your first battle")
    print("\n\nProfessor Oak:", end=" ")
    writen("Nathan come here! ")
    print("\n\n       Nathan:", end=" ")
    writen("Yes?")
    print("\n\nProfessor Oak:", end=" ")
    writen("Time for you two to battle ")
    print("\n\n       Nathan:", end=" ")
    writen("Sure! Lets do this!")

def ready():
    print("\n\nProfessor Oak:", end=" ")
    writen("Well, I think you are ready")
    print("\n\nProfessor Oak:", end=" ")
    writen("Goodluck in the wild!")


if __name__ == "__main__":
    print("WRONG FILE, THIS IS THE DIALOGUE FILE")
    quit("RUN THE pokemon.py INSTEAD")