import random
import sys
import time
import pokemon

class Pokemon():
    def __init__(self):
        self.name = None
        self.lvl = 0
        self.type = None
        self.hp = 0
        self.maxhp = 0
        self.atk = 0
        self.defn = 0
        self.speed = 0
        self.exp = 0
        self.maxexp = 0

    def ViewStats(self):
        print(f"========[{self.name}]========")
        print(f"Type: {self.type}")
        print(f"Level: {self.lvl}")
        print(f"HP: {self.hp} / {self.maxhp}")
        print(f"Attack: {self.atk}")
        print(f"Defense: {self.defn}")
        print(f"Speed: {self.speed}")
        print(f"Exp: {self.exp} / {self.maxexp}")
        print("================")

class Trainer():
    def __init__(self):
        self.name = None


    def backpack(self):
        pass



#Starter Pokemon
bulbasaur = Pokemon()
bulbasaur.name = "Bulbasaur"
bulbasaur.lvl = 5
bulbasaur.type = "Grass"
bulbasaur.hp = 45
bulbasaur.maxhp = 45
bulbasaur.atk = 49
bulbasaur.defn = 49
bulbasaur.speed = 45
bulbasaur.exp = 0
bulbasaur.maxexp = 10

charmander = Pokemon()
charmander.name = "Charmander"
charmander.lvl = 5
charmander.type = "Fire"
charmander.hp = 39
charmander.maxhp = 39
charmander.atk = 52
charmander.defn = 43
charmander.speed = 65
charmander.exp = 0
charmander.maxexp = 10

squirtle = Pokemon()
squirtle.name = "Squirtle"
squirtle.lvl = 5
squirtle.type = "Water"
squirtle.hp = 44
squirtle.maxhp = 44
squirtle.atk = 48
squirtle.defn = 65
squirtle.speed = 43
squirtle.exp = 0
squirtle.maxexp = 10

#Ash's Pokemon (Rival)
pikachu = Pokemon()
pikachu.name = "Pikachu"
pikachu.lvl = 5
pikachu.type = "Electric"
pikachu.hp = 35
pikachu.maxhp = 35
pikachu.atk = 55
pikachu.defn = 30
pikachu.speed = 90
pikachu.exp = 0
pikachu.maxexp = 10


def type(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def intro():
    print("=================================")
    type("Welcome to Pokemon Yellow Thunder!")
    print("=================================")
    type("Professor Oak: Greetings! My name is proffesor Oak!"
         " You have probably seen me on TV.\n")
    type("Professor Oak: In this world, pokemon are our friends, they can be our pets"
         " but some people use them for battle as well!\n")
    type("Professor Oak: Your task will be to explore the pokemon world!\n")
    type("Professor Oak: But do not worry, you won't be alone, my grandson Ash"
         " will help you throughout your journey as well!\n")
    type("Professor Oak: Quick! Your journey begins soon! I wish you"
         " the best of luck!")
    game()


def game():
    while a == True:





a = True
if __name__ == '__main__':
    intro()
