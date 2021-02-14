import random
import sys
import time

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
        self.moves = []


    def ViewStats(self):
        type(f"========[{self.name}]========")
        type(f"Type: {self.type}")
        type(f"Level: {self.lvl}")
        type(f"HP: {self.hp} / {self.maxhp}")
        type(f"Attack: {self.atk}")
        type(f"Defense: {self.defn}")
        type(f"Speed: {self.speed}")
        type(f"Exp: {self.exp} / {self.maxexp}")
        type("================")


class Trainer():
    def __init__(self):
        self.name = None
        self.pokemon = []

    def backpack(self):
        self.pokeballs = 0
        self.potion = 0
        self.revive = 0


class Moves():
    def __init__(self):
        self.name = None
        self.power = 0
        self.pp = 0
        self.accuracy = 0
        self.typ = None

#Moves
tackle = Moves()
tackle.name = "Tackle"
tackle.power = 40
tackle.pp = 35
tackle.accuracy = 100
tackle.typ = "Normal"

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
bulbasaur.moves = [tackle]


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
charmander.moves = [tackle]

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
squirtle.moves = [tackle]


#Grunt Pokemon
pidgey_noob = Pokemon()
pidgey_noob.name = "Pidgey"
pidgey_noob.lvl = 3
pidgey_noob.type = "Flying"
pidgey_noob.hp = 35
pidgey_noob.maxhp = 35
pidgey_noob.atk = 40
pidgey_noob.defn = 35
pidgey_noob.speed = 50
pidgey_noob.exp = 0
pidgey_noob.maxexp = 10

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
pikachu.moves = [tackle]

#Ash's Future Pokemon
#Second battle

#MC Trainer
player = Trainer()
player.name = ""
player.pokemon = []
player.pokeballs = 1
player.potion = 1
player.revive = 1


def ViewBackpack():
    type(f"\n(1). Pokeballs: {player.pokeballs}")
    type(f"(2). Potion: {player.potion}")
    type(f"(3). Self-Revives: {player.revive}")
    type(f"(4). Back\n")


#Trainer
ash = Trainer()
ash.name = "Ash"
ash.pokemon = [pikachu]

grunt_noob = Trainer()
grunt_noob.name = "Team Rocket Grunt"
grunt_noob.pokemon = [pidgey_noob]

def type(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0)
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
    type("By the way, what's your name?")
    user_name = input("Enter Name: ")
    type("Professor Oak: Quick! Your journey begins soon! I wish you"
         " the best of luck!")
    type("Entering the pokemon world...")
    type("...")
    type("..")
    type(".")
    player.name = user_name
    game(user_name)


def battle(enemy_name, enemy, trainer_or_wild):
    mc_poke = player.pokemon[0]
    enemy_poke = enemy.pokemon[0]
    print("===============================================")
    type(f"{enemy_name} CHALLENGES YOU TO A POKEMON BATTLE!")
    print("===============================================\n")
    type(f"{player.name}: Go {mc_poke.name}!\n")
    type(f"{enemy.name}: Go {enemy_poke.name}!\n")
    fight = True

    while fight == True:
        what_to_do = True
        type(f"Enemy: {enemy_poke.name} (Lvl: {enemy_poke.lvl}) ")
        type(f"HP: {enemy_poke.hp}/{enemy_poke.maxhp}\n")
        type(f"Your Pokemon: {mc_poke.name} (Lvl: {mc_poke.lvl}) ")
        type(f"HP: {mc_poke.hp}/{mc_poke.maxhp}\n")

        while what_to_do == True:
            type("(1). Attack")
            type("(2). Pokemon")
            type("(3). Backpack")
            type("(4). Run")
            what_do = int(input(f"What should {mc_poke.name} do? "))
            if what_do > 4 or what_do < 1:
                print("ERROR: Please pick 1-4!\n")
            elif what_do == 1:
                try:
                    for i in range(1, len(mc_poke.moves) + 1):
                        number = 1 * i
                        type(f"{number}. {mc_poke.moves[i - 1].name}")
                    move = int(input("\nSelect Your Moves: "))
                    if move > 0:
                        type(f"{mc_poke.name}, use {mc_poke.moves[move - 1].name}!\n")
                        crit_or_no = random.randint(1, 30)
                        crit = 1
                        if crit_or_no == 15:
                            crit = 2
                        if random.randint(1, 100) < mc_poke.moves[move - 1].accuracy:
                            eff = effective(mc_poke, enemy_poke, move)
                            damage = round((mc_poke.lvl + mc_poke.atk + mc_poke.moves[move - 1].power - enemy_poke.defn) / 6 * crit * eff)
                            enemy_poke.hp = enemy_poke.hp - damage
                            type(f"{mc_poke.name} did {damage} damage!\n")
                            what_to_do = False
                        else:
                            type(f"{mc_poke.name} tried to use {mc_poke.moves[move - 1].name} but missed!\n")
                            what_to_do = False
                    else:
                        print("ERROR: Must be in range of your moves!\n")
                except IndexError:
                    print("ERROR: Must be in range of your moves!\n")
                except ValueError:
                    print("ERROR: Please choose a number!\n")

            elif what_do == 2:
                try:
                    type("\nYour Pokemon:")
                    for i in range(1, len(player.pokemon) + 1):
                        numb = 1 * i
                        type(f"{numb}. {player.pokemon[i - 1].name}")
                    swap_poke = int(input("\nChoose Your Pokemon To Swap Out!(Number): "))
                    try:
                        if swap_poke > 0:
                            if player.pokemon[swap_poke - 1] == mc_poke:
                                type("You can't swap out for the same pokemon...\n")
                            if player.pokemon[swap_poke - 1] != mc_poke:
                                type(f"You withdrew {mc_poke.name}, Go {player.pokemon[swap_poke - 1].name}!\n")
                                mc_poke = player.pokemon[swap_poke - 1]
                                what_to_do = False
                        else:
                            print("ERROR: Can't go below 0!\n")
                    except IndexError:
                        print("ERROR: Must be in range of your pokemon!\n")
                except ValueError:
                    print("ERROR: Please choose a number!\n")

            elif what_do == 3:
                ViewBackpack()
                backpack = int(input("Which should I choose? "))
                if backpack <= 4 and backpack >= 1:
                    if backpack == 1:
                        if player.pokeballs >= 1:
                            if trainer_or_wild == "trainer":
                                type("You can't capture someone's Pokemon!")
                            else:
                                type("You used 1 Pokeball!\n")
                                player.pokeballs = player.pokeballs - 1
                                rand = random.randint(1,2)
                                if rand == 1:
                                    type(f"You successfully captured a wild {enemy_poke.name}")
                                    player.pokemon.append(enemy_poke.pokemon[0])
                                    fight = False
                                    catch = True
                                elif rand == 2:
                                    type(f"{enemy_poke.name} broke free!")
                                    what_to_do = False
                        else:
                            type("You have no Pokeballs!\n")
                    if backpack == 2:
                        if player.potion == 0:
                            type("You have no Potions!!\n")
                        else:
                            type("\nYour Pokemon:")
                            for i in range(1, len(player.pokemon) + 1):
                                numb = 1 * i
                                type(f"{numb}. {player.pokemon[i - 1].name}")
                            try:
                                revive_poke = int(input("\nChoose Your Pokemon To Revive!(Number): "))
                                # if mc_poke.name == "dead":
                                # type(f"{mc_poke.name} has been knocked out, cannot be healed!")
                                player.pokemon[revive_poke - 1].hp = player.pokemon[revive_poke - 1].maxhp
                            except IndexError:
                                print("ERROR: Must be in range of your pokemon!\n")
                            except ValueError:
                                print("ERROR: Please choose a number!\n")

                    if backpack == 3:
                        if player.revive == 0:
                            type("You have no Self-Revives!\n")
                        else:
                            type("\nYour Pokemon:")
                            for i in range(1, len(player.pokemon) + 1):
                                numb = 1 * i
                                type(f"{numb}. {player.pokemon[i - 1].name}")
                            try:
                                revive_poke = int(input("\nChoose Your Pokemon To Revive!(Number): "))
                                #if mc_poke.name != "dead":
                                #type(f"{mc_poke.name} is not knocked out, you can't use a Revive!")
                                player.pokemon[revive_poke - 1].hp = player.pokemon[revive_poke - 1].maxhp
                            except IndexError:
                                print("ERROR: Must be in range of your pokemon!\n")
                            except ValueError:
                                print("ERROR: Please choose a number!\n")

                    if backpack == 4:
                        pass
                else:
                    print("ERROR: Must be between 1-4")

            elif what_do == 4:
                if trainer_or_wild == "trainer":
                    type("You can't escape from a Trainer battle!\n")
                elif trainer_or_wild == "wild":
                    type("Escaped Successfully!\n")
                    fight = False
                    run = True

        else:
            #Enemy attack
            abc = random.randint(1, len(enemy_poke.moves))
            type(f"Enemy {enemy_poke.name} used {enemy_poke.moves[abc - 1].name}!\n")
            crit_or = random.randint(1, 30)
            crit = 1
            if crit_or == 15:
                crit = 2
            if random.randint(1, 100) < enemy_poke.moves[abc - 1].accuracy:
                effec = effective(enemy_poke, mc_poke, abc)
                damag = round((mc_poke.lvl + mc_poke.atk + mc_poke.moves[abc - 1].power - enemy_poke.defn) / 6 * crit * effec)
                mc_poke.hp = mc_poke.hp - damag
                type(f"Enemy {enemy_poke.name} did {damag} damage!\n")


    if catch == True:
        pass

    if run == True:
        pass


def effective(move, second_poke, numb):
    if move.moves[numb - 1].typ == "Fire":
        pass
    if move.moves[numb - 1].typ == "Water":
        pass
    if move.moves[numb - 1].typ == "Grass":
        pass
    if move.moves[numb - 1].typ == "Normal":
        if second_poke.type == "Ghost":
            return 0
        if second_poke.type == "Fighting":
            return 0.5
        else:
            return 1
    if move.moves[numb - 1].typ == "Flying":
        pass
    if move.moves[numb - 1].typ == "Electric":
        pass
    if move.moves[numb - 1].typ == "Fighting":
        pass
    if move.moves[numb - 1].typ == "Ghost":
        pass
    if move.moves[numb - 1].typ == "Psychic":
        pass


def game(name):
    print("\n")
    type(f"Mom: Good morning {name}!\n")
    type("Mom: Ash came in and told me to ask you to come to his house"
         " he said something about Pokemon and adventure! I'm sure it will be fun.\n")
    type(f"{name}: Oh, okay thanks mom.\n")
    type("You go outside...")
    type("...")
    type("..")
    type(".")

    #Ash house
    type(f"Ash: Hey! {name}, I've been waiting forever, where have you been?\n")
    type("Ash: Nevermind, lets just get your first pokemon! I already picked mine hehe\n")
    type(f"{name}: Who did you pick?\n")
    type(f"Ash: You'll find out later, just talk to Prof. Oak in his lab!\n")
    type(f"{name}: Okay! I'll see you later!\n")

    #Pick Pokemon
    pick = True
    while pick == True:
        type(f"Professor Oak: Ah, {name}, I think Ash has sent you, well, I think you"
            f" know what you are here for! Pick your first Pokemon!")
        print("===============")
        print("(1). Charmander")
        print("(2). Squirtle")
        print("(3). Bulbasaur")
        print("===============")

        try:
            starter_poke = int(input("Which one should I choose? "))
            if starter_poke > 3 or starter_poke < 1:
                print("ERROR: Please pick 1-3!\n")
            elif starter_poke == 1:
                type("Congratulations! You chose Charmander\n")
                player.pokemon.append(charmander)
                pick = False
            elif starter_poke == 2:
                type("Congratulations! You chose Squirtle\n")
                player.pokemon.append(squirtle)
                pick = False
            elif starter_poke == 3:
                type("Congratulations! You chose Bulbasaur\n")
                player.pokemon.append(bulbasaur)
                pick = False
        except ValueError:
            print("ERROR: Please pick a number!\n")

    #First Battle with Rival
    type("Ash: Alright! Now you got your first Pokemon, Let's battle!"
         " By the way, I chose Pikachu, hehe!\n")
    battle("ASH", ash, "trainer")

    #Go to First City
    type("Ash: That was a tough battle, it was so close!\n")
    type("Ash: Alright then, I'm heading to Lavender Town, and I'm gonna be the Pokemon Champion!\n")
    type("Ash: See you there!\n")
    type("...")
    type("..")
    type(".")
    type("Professor Oak: Well, it seems that he's off already, you should catch up with him.\n")
    type(f"{name}: Alright, thank you professor!\n")
    type("Heading to Route 101...")
    type("...")
    type("..")
    type(".")
    type("In Route 101...\n")
    type("???: Ahhh! Help!!\n")
    type(f"{name}: Huh? who said that?\n")
    type("Team Rocket Grunt: Give me your pokemon kid!\n")
    type(f"{name}: Hey! Stop!\n")
    type("Team Rocket Grunt: Hahaha! You think you can stop me too kid?\n")
    """battle("Team Rocket Grunt")"""

    main(name)

def main(name):
    pass



a = True
if __name__ == '__main__':
    intro()
