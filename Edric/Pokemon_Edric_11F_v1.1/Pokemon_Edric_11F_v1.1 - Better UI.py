import random

#Pokemon
class pokemon:
    moves = []
    def __init__(self):
        self.name = None
        self.type = None
        self.lvl = 0
        self.hp = 0
        self.MaxHp = 0
        self.xp = 0
        self.MaxXp = 10
        self.attack = 0

    @classmethod
    def addscratch(cls, scratch1):
        cls.moves.append(scratch1)

    def GetXp(self, xp):
        self.xp = self.xp + xp
        if (self.xp >= self.MaxXp):
            self.LevelUp()

    def LevelUp(self):
        self.lvl = self.lvl+1
        self.MaxHp = self.MaxHp+3
        self.hp = self.MaxHp
        self.xp = 0
        self.MaxXp = self.MaxXp+10
        self.attack = self.attack+1
        input(f"{player.pokemon[0].name} Level Up!")
        self.ViewStats()

    def ViewStats(self):
        print("\nName : ",self.name)
        print("Type : ",self.type)
        print("Level : ",self.lvl)
        print("HP : ",self.hp,"/",self.MaxHp)
        print("XP : ",self.xp,"/",self.MaxXp)


class enemy:
    def __init__(self):
        self.name = None
        self.type = None
        self.lvl = 0
        self.hp = 0
        self.MaxHp = 0
        self.xp = 0
        self.MaxXp = 10
        self.attack = 0
        self.givexp = 0
        self.moves = []


class moves():
    def __init__(self):
        self.name = None
        self.accuracy = 0
        self.multiplier = 0

#moves
scratch = moves()
scratch.name = "Scratch"
scratch.multiplier = 1
scratch.accuracy = 100
pokemon.addscratch(scratch)

inferno = moves()
inferno.name = "Inferno"
inferno.multiplier = 4
inferno.accuracy = 30

hydro_pump = moves()
hydro_pump.name = "Hydro Pump"
hydro_pump.multiplier = 2
hydro_pump.accuracy = 60

magical_leaf = moves()
magical_leaf.name = "Magical Leaf"
magical_leaf.multiplier = 3
magical_leaf.accuracy = 40

#Reshiram moves
fire_fang = moves()
fire_fang.name = "Fire Fang"
fire_fang.multiplier = 1
fire_fang.accuracy = 65

#-Unused
overheat = moves()
overheat.name = "Overheat"
overheat.multiplier = 4
overheat.accuracy = 40

#Growlithe moves
bite = moves()
bite.name = "Bite"
bite.multiplier = 1
bite.accuracy = 100

#-Unused
flamethrower = moves()
flamethrower.name = "Flamethrower"
flamethrower.multiplier = 2
flamethrower.accuracy = 90

#Pokemon list and stats
bulbasaur = pokemon()
bulbasaur.name = "Bulbasaur"
bulbasaur.type = "GRASS"
bulbasaur.lvl = 5
bulbasaur.hp = 20
bulbasaur.MaxHp = 20
bulbasaur.xp = 0
bulbasaur.MaxXp = 10
bulbasaur.attack = 3
bulbasaur.defence = 1

charmander = pokemon()
charmander.name = "Charmander"
charmander.type = "FIRE"
charmander.lvl = 5
charmander.hp = 20
charmander.MaxHp = 20
charmander.xp = 0
charmander.MaxXp = 10
charmander.attack = 3
charmander.defence = 1

squirtle = pokemon()
squirtle.name = "Squirtle"
squirtle.type = "WATER"
squirtle.lvl = 5
squirtle.hp = 20
squirtle.MaxHp = 20
squirtle.xp = 0
squirtle.MaxXp = 10
squirtle.attack = 3
squirtle.defence = 1

#Enemies
growlithe = enemy()
growlithe.name = "Growlithe"
growlithe.lvl = 4
growlithe.hp = 15
growlithe.MaxHp = 15
growlithe.attack = 3
growlithe.defence = 0
growlithe.givexp = 15
growlithe.moves.append(bite)

reshiram = enemy()
reshiram.name = "Reshiram"
reshiram.lvl = 8
reshiram.hp = 25
reshiram.MaxHp = 25
reshiram.attack = 4
reshiram.defence = 3
reshiram.givexp = 999
reshiram.moves.append(fire_fang)


#Player
class trainer:
    def __init__(self):
        self.name = None
        self.pokemon = []

    def inventory(self):
        self.potion = 0

player = trainer()
player.pokemon = []
player.potion = 5

#Intro Dialogue
print("\n              _                              \n  _ __   ___ | | _____ _ __ ___   ___  _ __  \n | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ \n | |_) | (_) |   <  __/ | | | | | (_) | | | |\n | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|\n |_|                                         ")
print("               By: Edric 11F")
input("\n        - PRESS ENTER TO CONTINUE -")
input("\nWelcome kid, to the Pokemon World!\n")
name = input("Can you introduce yourself?\nName: ")
player.name = name
if name:
    pass
else:
    input("\nIf you don't want to tell your name then we shouldn't talk.")
    exit()

print(f"\nWhat a good name {player.name}")
input("Sounds like a future Pokemon Legend")
input("\nI heard you're going on an adventure?")
print("\nWild Pokemon lives in tall grass.")
input("You will need a Pokemon for your protection.")

#Menu pog
menutrue = True
def menu():

    while menutrue == True:
        print("\n[1] Credits")
        print("[2] Pokemon Stats")
        print("[3] Fast Travel")
        print("[0] Quit Game")
        menuinput = input("Your choice: ")
        if menuinput == "1":
            print(f"\nCredits\nEdric Dario Wijaya / 11F")
            input("\n- PRESS ENTER TO GO BACK -")
            menu()
        elif menuinput == "2":
            player.pokemon[0].ViewStats()
            input("\n- PRESS ENTER TO GO BACK -")
            menu()
        elif menuinput == "3":
            print("\n[1] Midgar")
            print("[2] Home")
            print("[3] PokeCenter")
            print("[4] Return to Menu")
            destination = input("Choose your destination: ")
            if destination == "1":
                input("\nYou've arrived in Midgar\n")
                if random.randint(0, 4) == 0:
                    battle(reshiram)
                else:
                    battle(growlithe)

            elif destination == "2":
                input("\nYou took a rest at home and eat good food.\n  _________\n ///////////\ \n///////////  \ \n|    _    |  |\n|[] | | []|[]|\n|   | |   |  |\n")
            elif destination == "3":
                player.pokemon[0].hp = player.pokemon[0].MaxHp
                input("\nHP has been restored")
            elif destination == "4":
                menu()
            else:
                input("\nDestination Unknown\n")
                menu()
        elif menuinput == "0":
            print("\nThanks for playing!")
            print(
                "\n              _                              \n  _ __   ___ | | _____ _ __ ___   ___  _ __  \n | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ \n | |_) | (_) |   <  __/ | | | | | (_) | | | |\n | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|\n |_|                                         ")
            print("               By: Edric 11F")
            exit()
        else:
            input("Enter a Valid Number")
            menu()

#move list in battle
def movelist():
    print("\n================")
    print("[1] Scratch")
    print(f"[2] {player.pokemon[0].moves[1].name}")
    print("================\n")

#accuracy
def hitaccuracy():
    if random.randint(1, 100) <= int(f"{player.pokemon[0].moves[1].accuracy}"):
        hit = False
    else:
        hit = True
    return hit

#Battle
def battle(enemy):
    input(f"{enemy.name} appeared!\n")
    print(f"{player.pokemon[0].name} // HP: {player.pokemon[0].hp}")
    input(f"{enemy.name} // HP: {enemy.hp}")

    while player.pokemon[0].hp > 0 and enemy.hp > 0:
        poketurn = True

        while poketurn == True:
            movelist()
            pokemove = input(f"What will {player.pokemon[0].name} do? ")
            if pokemove == "1":
                print(f"{player.pokemon[0].name} used Scratch!")
                print(f"{player.pokemon[0].name} dealt {player.pokemon[0].attack} damage!")
                enemy.hp -= player.pokemon[0].attack
                print(f"{player.pokemon[0].name} HP: {player.pokemon[0].hp}/{player.pokemon[0].MaxHp}")
                input(f"{enemy.name} HP: {enemy.hp}/{enemy.MaxHp}")
                if enemy.hp <= 0:
                    input("\nYOU WIN!")
                    player.pokemon[0].GetXp(enemy.givexp)
                    enemy.hp = enemy.MaxHp
                    return None

                print(f"\n{enemy.name} used {enemy.moves[0].name}!")
                print(f"{enemy.name} dealt {enemy.attack} damage!")
                player.pokemon[0].hp -= enemy.attack
                print(f"{player.pokemon[0].name} HP: {player.pokemon[0].hp}/{player.pokemon[0].MaxHp}")
                input(f"{enemy.name} HP: {enemy.hp}/{enemy.MaxHp}")
                if player.pokemon[0].hp <= 0:
                    input("\nYOUR POKEMON DIED")
                    exit()

                poketurn = False

            elif pokemove == "2":
                input(f"{player.pokemon[0].name} used {player.pokemon[0].moves[1].name}!")
                hit = hitaccuracy()
                if hit == True:
                    finaldamage = player.pokemon[0].attack * player.pokemon[0].moves[1].multiplier
                    print(f"{player.pokemon[0].name} dealt {finaldamage} damage!")
                    enemy.hp -= finaldamage
                    print(f"{player.pokemon[0].name} HP: {player.pokemon[0].hp}/{player.pokemon[0].MaxHp}")
                    input(f"{enemy.name} HP: {enemy.hp}/{enemy.MaxHp}")
                    if enemy.hp <= 0:
                        input("\nYOU WIN!")
                        player.pokemon[0].GetXp(enemy.givexp)
                        enemy.hp = enemy.MaxHp
                        return None

                    print(f"\n{enemy.name} used {enemy.moves[0].name}!")
                    print(f"{enemy.name} dealt {enemy.attack} damage!")
                    player.pokemon[0].hp -= enemy.attack
                    print(f"{player.pokemon[0].name} HP: {player.pokemon[0].hp}/{player.pokemon[0].MaxHp}")
                    input(f"{enemy.name} HP: {enemy.hp}/{enemy.MaxHp}")
                    if player.pokemon[0].hp <= 0:
                        input("\nYOUR POKEMON DIED")
                        exit()

                    poketurn = False

                if hit == False:
                    print(f"{player.pokemon[0].name} missed!")
                    print(f"\n{enemy.name} used {enemy.moves[0].name}!")
                    print(f"{enemy.name} dealt {enemy.attack} damage!")
                    player.pokemon[0].hp -= enemy.attack
                    print(f"{player.pokemon[0].name} HP: {player.pokemon[0].hp}/{player.pokemon[0].MaxHp}")
                    input(f"{enemy.name} HP: {enemy.hp}/{enemy.MaxHp}")
                    if player.pokemon[0].hp <= 0:
                        input("\nYOUR POKEMON DIED")
                        exit()

            else:
                input("\nEnter a Valid Number\n")


def pok_finaldamage():
    finaldamage = player.pokemon[0].attack * player.pokemon[0].moves[1].multiplier
    print(finaldamage)
    return finaldamage


#Starter
starterchoose = True
while starterchoose == True:
    starterpok = input("\nHere, I give you 3 choices for your first Pokemon.\n[1] Left\n[2] Middle\n[3] Right\n")
    if starterpok == ("1"):
        player.pokemon.append(bulbasaur)
        player.pokemon[0].moves.append(magical_leaf)
        starterchoose = False
    elif starterpok == ("2"):
        player.pokemon.append(charmander)
        player.pokemon[0].moves.append(inferno)
        starterchoose = False
    elif starterpok == ("3"):
        player.pokemon.append(squirtle)
        player.pokemon[0].moves.append(hydro_pump)
        starterchoose = False
    else:
        input("Enter a Valid Number")


input(f"\nYour Pokemon is {player.pokemon[0].name}")
yesnostarter = input(f"\nAren't you lucky to have {player.pokemon[0].name}? ")
yesnostarterlow = yesnostarter.lower()
if yesnostarterlow == ("yes"):
    pass
if yesnostarterlow == ("no"):
    input("\nOK then you may go home.")
    exit()
else:
    input("I'll take that as a yes.")


#Menu Dialogue
input("\nYou can navigate through your inventory by entering a number from the menu")
menu()
