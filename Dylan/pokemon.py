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
        self.status = None


    def ViewStats(self):
        type(f"========[{self.name}]========")
        type(f"Type: {self.type}")
        type(f"Level: {self.lvl}")
        type(f"HP: {self.hp} / {self.maxhp}")
        type(f"Attack: {self.atk}")
        type(f"Defense: {self.defn}")
        type(f"Exp: {self.exp} / {self.maxexp}")
        type("======================")


class Trainer():
    def __init__(self):
        self.name = None
        self.pokemon = []

    def backpack(self):
        self.pokeballs = 0
        self.potion = 0
        self.revive = 0
        self.money = 0

    def ViewBackpack(self):
        type(f"\n(1). Pokeballs: {player.pokeballs}")
        type(f"(2). Potion: {player.potion}")
        type(f"(3). Self-Revives: {player.revive}\n")


class Moves():
    def __init__(self):
        self.name = None
        self.power = 0
        self.accuracy = 0
        self.typ = None

#Moves
tackle = Moves()
tackle.name = "Tackle"
tackle.power = 40
tackle.accuracy = 100
tackle.typ = "Normal"

vinewhip = Moves()
vinewhip.name = "Vine Whip"
vinewhip.power = 45
vinewhip.accuracy = 100
vinewhip.typ = "Grass"

razorleaf = Moves()
razorleaf.name = "Razor Leaf"
razorleaf.power = 55
razorleaf.accuracy = 95
razorleaf.typ = "Grass"

venoshock = Moves()
venoshock.name = "Venoshock"
venoshock.power = 65
venoshock.accuracy = 100
venoshock.typ = "Poison"

solarbeam = Moves()
solarbeam.name = "Solar Beam"
solarbeam.power = 100
solarbeam.accuracy = 70
solarbeam.typ = "Grass"

ember = Moves()
ember.name = "Ember"
ember.power = 40
ember.accuracy = 100
ember.typ = "Fire"

dragonbreath = Moves()
dragonbreath.name = "Dragon Breath"
dragonbreath.power = 60
dragonbreath.accuracy = 100
dragonbreath.typ = "Dragon"

flamethrower = Moves()
flamethrower.name = "Flamethrower"
flamethrower.power = 80
flamethrower.accuracy = 100
flamethrower.typ = "Fire"

inferno = Moves()
inferno.name = "Inferno"
inferno.power = 120
inferno.accuracy = 50
inferno.typ = "Fire"

watergun = Moves()
watergun.name = "Water Gun"
watergun.power = 40
watergun.accuracy = 100
watergun.typ = "Water"

waterpulse = Moves()
watergun.name = "Water Pulse"
watergun.power = 60
watergun.accuracy = 100
watergun.typ = "Water"

aquatail = Moves()
aquatail.name = "Aqua Tail"
aquatail.power = 90
aquatail.accuracy = 90
aquatail.typ = "Water"

hydropump = Moves()
hydropump.name = "Hydro Pump"
hydropump.power = 100
hydropump.accuracy = 70
hydropump.typ = "Water"

gust = Moves()
gust.name = "Gust"
gust.power = 40
gust.accuracy = 100
gust.typ = "Flying"

wingattack = Moves()
wingattack.name = "Wing Attack"
wingattack.power = 60
wingattack.accuracy = 100
wingattack.typ = "Flying"

razorwind = Moves()
razorwind.name = "Razor Wind"
razorwind.power = 80
razorwind.accuracy = 95
razorwind.typ = "Flying"

thundershock = Moves()
thundershock.name = "Thunder Shock"
thundershock.power = 40
thundershock.accuracy = 100
thundershock.typ = "Electric"

spark = Moves()
spark.name = "Spark"
spark.power = 65
spark.accuracy = 100
spark.typ = "Electric"

thunderbolt = Moves()
thunderbolt.name = "Thunder Bolt"
thunderbolt.power = 90
thunderbolt.accuracy = 95
thunderbolt.typ = "Electric"

thunder = Moves()
thunder.name = "Thunder"
thunder.power = 110
thunder.accuracy = 75
thunder.typ = "Electric"

sandattack = Moves()
sandattack.name = "Sand Attack"
sandattack.power = 40
sandattack.accuracy = 95
sandattack.typ = "Ground"

rockthrow = Moves()
rockthrow.name = "Rock Throw"
rockthrow.power = 50
rockthrow.accuracy = 90
rockthrow.typ = "Rock"

earthquake = Moves()
earthquake.name = "Earthquake"
earthquake.power = 100
earthquake.accuracy = 90
earthquake.typ = "Ground"

confusion = Moves()
confusion.name = "Confusion"
confusion.power = 50
confusion.accuracy = 100
confusion.typ = "Psychic"

psybeam = Moves()
psybeam.name = "Psybeam"
psybeam.power = 65
psybeam.accuracy = 100
psybeam.typ = "Psychic"

psychic = Moves()
psychic.name = "Psychic"
psychic.power = 90
psychic.accuracy = 100
psychic.typ = "Psychic"

futuresight = Moves()
futuresight.name = "Future Sight"
futuresight.power = 120
futuresight.accuracy = 90
futuresight.typ = "Psychic"

flashcannon = Moves()
flashcannon.name = "Flash Cannon"
flashcannon.power = 80
flashcannon.accuracy = 100
flashcannon.type = "Steel"

zapcannon = Moves()
zapcannon.name = "Zap Cannon"
zapcannon.power = 120
zapcannon.accuracy = 60
zapcannon.typ = "Electric"

smog = Moves()
smog.name = "Smog"
smog.power = 30
smog.accuracy = 100
smog.typ = "Poison"

assurance = Moves()
assurance.name = "Assurance"
assurance.power = 60
assurance.accuracy = 100
assurance.typ = "Dark"

belch = Moves()
belch.name = "Belch"
belch.power = 120
belch.accuracy = 80
belch.typ = "Poison"

twister = Moves()
twister.name = "Twister"
twister.power = 40
twister.accuracy = 100
twister.typ = "Dragon"

dragontail = Moves()
dragontail.name = "Dragon Tail"
dragontail.power = 60
dragontail.accuracy = 100
dragontail.typ = "Dragon"

dragonrush = Moves()
dragonrush.name = "Dragon Rush"
dragonrush.power = 90
dragonrush.accuracy = 75
dragonrush.typ = "Dragon"

outrage = Moves()
outrage.name = "Outrage"
outrage.power = 120
outrage.accuracy = 95
outrage.typ = "Dragon"

ancientpower = Moves()
ancientpower.name = "Ancient Power"
ancientpower.power = 60
ancientpower.accuracy = 100
ancientpower.typ = "Rock"

freezedry = Moves()
freezedry.name = "Freeze-Dry"
freezedry.power = 70
freezedry.accuracy = 100
freezedry.typ = "Ice"

icebeam = Moves()
icebeam.name = "Ice Beam"
icebeam.power = 90
icebeam.accuracy = 100
icebeam.typ = "Ice"

hurricane = Moves()
hurricane.name = "Hurricane"
hurricane.power = 110
hurricane.accuracy = 75
hurricane.typ = "Flying"

blizzard = Moves()
blizzard.name = "Blizzard"
blizzard.power = 120
blizzard.accuracy = 90
blizzard.typ = "Ice"

shadowball = Moves()
shadowball.name = "Shadow Ball"
shadowball.power = 80
shadowball.accuracy = 100
shadowball.typ = "Ghost"

#Starter Pokemon
bulbasaur = Pokemon()
bulbasaur.name = "Bulbasaur"
bulbasaur.lvl = 5
bulbasaur.type = "Grass"
bulbasaur.hp = 45
bulbasaur.maxhp = 45
bulbasaur.atk = 49
bulbasaur.defn = 49
bulbasaur.exp = 0
bulbasaur.maxexp = 10
bulbasaur.moves = [tackle]
bulbasaur.status = "Alive"


charmander = Pokemon()
charmander.name = "Charmander"
charmander.lvl = 5
charmander.type = "Fire"
charmander.hp = 39
charmander.maxhp = 39
charmander.atk = 52
charmander.defn = 43
charmander.exp = 0
charmander.maxexp = 10
charmander.moves = [tackle]
charmander.status = "Alive"

squirtle = Pokemon()
squirtle.name = "Squirtle"
squirtle.lvl = 5
squirtle.type = "Water"
squirtle.hp = 44
squirtle.maxhp = 44
squirtle.atk = 48
squirtle.defn = 65
squirtle.exp = 0
squirtle.maxexp = 10
squirtle.moves = [tackle]
squirtle.status = "Alive"


#Grunt Pokemon
pidgey_noob = Pokemon()
pidgey_noob.name = "Pidgey"
pidgey_noob.lvl = 3
pidgey_noob.type = "Flying"
pidgey_noob.hp = 35
pidgey_noob.maxhp = 35
pidgey_noob.atk = 40
pidgey_noob.defn = 35
pidgey_noob.exp = 0
pidgey_noob.maxexp = 10
pidgey_noob.status = "Alive"
pidgey_noob.moves = [tackle]
pidgey = Trainer()
pidgey.name = "Pidgey"
pidgey.pokemon = [pidgey_noob]

#Ash's Pokemon (Rival)
pikachu = Pokemon()
pikachu.name = "Pikachu"
pikachu.lvl = 5
pikachu.type = "Electric"
pikachu.hp = 35
pikachu.maxhp = 35
pikachu.atk = 55
pikachu.defn = 30
pikachu.exp = 0
pikachu.maxexp = 10
pikachu.moves = [tackle]
pikachu.status = "Alive"
pika = Trainer()
pika.name = "Pikachu"
pika.pokemon = [pikachu]

#Sandshrew, Kirlia, Magnemite, Koffing, Articuno, Dragonair

onix = Pokemon()
onix.name = "Onix"
onix.lvl = 15
onix.type = "Rock"
onix.hp = 60
onix.maxhp = 60
onix.atk = 58
onix.defn = 75
onix.moves = [tackle, rockthrow, sandattack]

flail = Moves()
flail.name = "Flail"
flail.accuracy = 0
flail.power = 0
flail.typ = "Water"
magikarp = Pokemon()
magikarp.name = "Magikarp"
magikarp.lvl = 5
magikarp.type = "Water"
magikarp.hp = 20
magikarp.maxhp = 20
magikarp.atk = 20
magikarp.defn = 20
magikarp.moves = [flail]

stomp = Moves()
stomp.name = "Stomp"
stomp.power = 60
stomp.accuracy = 100
stomp.typ = "Normal"
snorlax = Pokemon()
snorlax.name = "Snorlax"
snorlax.lvl = 30
snorlax.type = "Normal"
snorlax.hp = 100
snorlax.maxhp = 100
snorlax.atk = 50
snorlax.defn = 50
snorlax.moves = [tackle, stomp]

gengar = Pokemon()
gengar.name = "Gengar"
gengar.lvl = 30
gengar.type = "Ghost"
gengar.hp = 85
gengar.maxhp = 85
gengar.atk = 100
gengar.defn = 60
gengar.moves = [smog, venoshock, assurance, shadowball]

gible = Pokemon()
gible.name = "Gible"
gible.lvl = 45
gible.type = "Dragon"
gible.hp = 95
gible.maxhp = 95
gible.atk = 100
gible.defn = 100
gible.moves = [sandattack, dragontail]

lapras = Pokemon()
lapras.name = "Lapras"
lapras.lvl = 45
lapras.type = "Ice"
lapras.hp = 110
lapras.maxhp = 110
lapras.atk = 105
lapras.defn = 110
lapras.moves = [waterpulse, freezedry, watergun]

sands = Pokemon()
sands.name = "Sandshrew"
sands.lvl = 25
sands.type = "Ground"
sands.hp = 80
sands.maxhp = 80
sands.atk = 90
sands.defn = 85
sands.exp = 0
sands.maxexp = 200
sands.moves = [sandattack, rockthrow]
sands.status = "Alive"
sandshrew = Trainer()
sandshrew.name = "Sandshrew"
sandshrew.pokemon = [sands]

ralt = Pokemon()
ralt.name = "Kirlia"
ralt.lvl = 25
ralt.type = "Psychic"
ralt.hp = 77
ralt.maxhp = 77
ralt.atk = 95
ralt.defn = 73
ralt.exp = 0
ralt.maxexp = 200
ralt.moves = [confusion]
ralt.status = "Alive"
ralts = Trainer()
ralts.name = "Kirlia"
ralts.pokemon = [ralt]

magne = Pokemon()
magne.name = "Magnemite"
magne.lvl = 40
magne.type = "Steel"
magne.hp = 105
magne.maxhp = 105
magne.atk = 110
magne.defn = 110
magne.exp = 0
magne.maxexp = 350
magne.moves = [tackle, thundershock]
magne.status = "Alive"
magnemite = Trainer()
magnemite.name = "Magnemite"
magnemite.pokemon = [magne]

weez = Pokemon()
weez.name = "Weezing"
weez.lvl = 40
weez.type = "Poison"
weez.hp = 95
weez.maxhp = 95
weez.atk = 112
weez.defn = 98
weez.exp = 0
weez.maxexp = 350
weez.moves = [tackle, smog]
weez.status = "Alive"
weezing = Trainer()
weezing.name = "Weezing"
weezing.pokemon = [weez]

dair = Pokemon()
dair.name = "Dragonair"
dair.lvl = 40
dair.type = "Poison"
dair.hp = 104
dair.maxhp = 104
dair.atk = 110
dair.defn = 108
dair.exp = 0
dair.maxexp = 350
dair.moves = [twister, dragontail, dragonbreath]
dair.status = "Alive"
dragonair = Trainer()
dragonair.name = "Dragonair"
dragonair.pokemon = [dair]

arti = Pokemon()
arti.name = "Articuno"
arti.lvl = 50
arti.type = "Ice"
arti.hp = 145
arti.maxhp = 145
arti.atk = 110
arti.defn = 120
arti.exp = 0
arti.maxexp = 450
arti.moves = [ancientpower, freezedry, icebeam, hurricane]
arti.status = "Alive"
articuno = Trainer()
articuno.name = "Articuno"
articuno.pokemon = [arti]

#Ash's Future Pokemon
pidgeot = Pokemon()
pidgeot.name = "Pidgeot"
pidgeot.lvl = 60
pidgeot.type = "Flying"
pidgeot.hp = 140
pidgeot.maxhp = 140
pidgeot.atk = 125
pidgeot.defn = 125
pidgeot.moves = [gust, wingattack, razorwind]

pikachu_pro = Pokemon()
pikachu_pro.name = "Pikachu"
pikachu_pro.lvl = 60
pikachu_pro.type = "Electric"
pikachu_pro.hp = 130
pikachu_pro.maxhp = 130
pikachu_pro.atk = 140
pikachu_pro.defn = 105
pikachu_pro.moves = [thunder, thundershock, thunderbolt]

dragonite = Pokemon()
dragonite.name = "Dragonite"
dragonite.lvl = 60
dragonite.type = "Dragon"
dragonite.hp = 150
dragonite.maxhp = 150
dragonite.atk = 135
dragonite.defn = 135
dragonite.moves = [twister, dragonrush, dragonbreath, outrage]

#MC Trainer
player = Trainer()
player.name = ""
player.pokemon = []
player.pokeballs = 100
player.potion = 1
player.revive = 1
player.money = 100

#Trainer
ash = Trainer()
ash.name = "Ash"
ash.pokemon = [pikachu]

grunt_noob = Trainer()
grunt_noob.name = "Team Rocket Grunt"
grunt_noob.pokemon = [pidgey_noob]

grunt_med = Trainer()
grunt_med.name = "Team Rocket Grunt"
grunt_med.pokemon = [onix]

gym_jose = Trainer()
gym_jose.name = "Gym Leader Jose"
gym_jose.pokemon = [pidgey_noob, onix]

gym_justin = Trainer()
gym_justin.name = "Gym Leader Justin"
gym_justin.pokemon = [magikarp, snorlax]

dason = Trainer()
dason.name = "Team Rocket Leader Dason"
dason.pokemon = [sandshrew, gengar]

gym_henry = Trainer()
gym_henry.name = "Gym Leader Henry"
gym_henry.pokemon = [gible, lapras]

champion_ash = Trainer()
champion_ash.name = "Pokemon Champion Ash"
champion_ash.pokemon = [pidgeot, pikachu_pro, dragonite]


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
    type("Professor Oak: Greetings! My name is Professor Oak!"
         " You have probably seen me on TV.\n")
    type("Professor Oak: In this world, pokemon are our friends, they can be our pets"
         " but some people use them for battle as well!\n")
    type("Professor Oak: Your task will be to explore the pokemon world!\n")
    type("Professor Oak: But do not worry, you won't be alone, my grandson Ash"
         " will help you throughout your journey as well!\n")
    type("By the way, what's your name?")
    user_name = input("Enter Name: ")
    type(f"\nProfessor Oak: Quick {user_name}! Your journey begins soon! I wish you"
         " the best of luck!\n")
    type("Entering the pokemon world...")
    type("...")
    type("..")
    type(".")
    player.name = user_name
    game(user_name)


def battle(enemy_name, enemy, trainer_or_wild, xp, money):
    mc_poke = player.pokemon[0]
    enemy_poke = enemy.pokemon[0]
    print("===============================================")
    type(f"{enemy_name} CHALLENGES YOU TO A POKEMON BATTLE!")
    print("===============================================\n")
    type(f"{player.name}: Go {mc_poke.name}!\n")
    type(f"{enemy.name}: Go {enemy_poke.name}!\n")
    fight = True
    win = False
    bruh = 0
    run = False
    catch = False

    while fight:
        what_to_do = True
        type(f"Enemy: {enemy_poke.name} (Lvl: {enemy_poke.lvl}) ")
        type(f"HP: {enemy_poke.hp}/{enemy_poke.maxhp}\n")
        type(f"Your Pokemon: {mc_poke.name} (Lvl: {mc_poke.lvl}) ")
        type(f"HP: {mc_poke.hp}/{mc_poke.maxhp}\n")

        while what_to_do:
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
                        type(f"{number}. {mc_poke.moves[i - 1].name} ({mc_poke.moves[i - 1].typ})")
                    move = int(input("\nSelect Your Moves: "))
                    move = move - 1
                    if move > -1:
                        type(f"{mc_poke.name}, use {mc_poke.moves[move - 1].name}!\n")
                        crit_or_no = random.randint(1, 30)
                        crit = 1
                        if crit_or_no == 15:
                            crit = 2
                            type("Critical Damage!\n")
                        if random.randint(1, 100) < mc_poke.moves[move - 1].accuracy:
                            eff = effective(mc_poke, enemy_poke, move)
                            damage = round((mc_poke.lvl + mc_poke.atk + mc_poke.moves[move - 1].power - enemy_poke.defn) / 6 * crit * eff)
                            enemy_poke.hp = enemy_poke.hp - damage
                            type(f"{mc_poke.name} did {damage} damage!\n")
                            if enemy_poke.hp <= 0:
                                enemy_poke.status = "Dead"
                                type(f"{enemy_poke.name} has been knocked out!")
                                mc_poke.exp = mc_poke.exp + xp
                                type(f"{mc_poke.name} has earned {xp} xp!")
                                type(f"Exp: {mc_poke.exp}/{mc_poke.maxexp}")
                                if mc_poke.exp >= mc_poke.maxexp:
                                    levelup(mc_poke)
                                    type(f"Congratulations, {mc_poke.name} leveled up to level {mc_poke.lvl}\n")
                                try:
                                    enemy_poke = enemy.pokemon[bruh + 1]
                                    type(f"{enemy_poke} come out!\n")
                                    bruh += 1
                                except IndexError:
                                    fight = False
                                    win = True
                                    win_or_lose = "Win"
                                    return win_or_lose
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
                player.ViewBackpack()
                backpack = int(input("Which should I choose? "))
                if backpack <= 4 and backpack >= 1:
                    if backpack == 1:
                        if player.pokeballs >= 1:
                            if trainer_or_wild == "trainer":
                                type("You can't capture someone's Pokemon!")
                            else:
                                type("You used 1 Pokeball!\n")
                                player.pokeballs = player.pokeballs - 1
                                if enemy_poke.hp <= enemy_poke.maxhp * 1 / 2:
                                    rando = random.randint(1,2)
                                    if rando == 1:
                                        type(f"You successfully captured a wild {enemy_poke.name}")
                                        player.pokemon.append(enemy.pokemon[0])
                                        return
                                        fight = False
                                    else:
                                        type(f"{enemy_poke.name} broke free!")
                                        what_to_do = False
                                else:
                                    rand = random.randint(1, 10)
                                    if rand == 1:
                                        type(f"You successfully captured a wild {enemy_poke.name}")
                                        player.pokemon.append(enemy.pokemon[0])
                                        return
                                        fight = False
                                    else:
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
                                pot = int(input("\nChoose Your Pokemon To Use Potion! (Number): "))
                                if player.pokemon[pot - 1].status == "Dead":
                                    type(f"{player.pokemon[pot - 1].name} has been knocked out, cannot be healed!")
                                if player.pokemon[pot - 1].hp == player.pokemon[pot - 1].maxhp:
                                    type(f"{player.pokemon[pot - 1].name} has full health!")
                                else:
                                    if player.pokemon[pot - 1].hp > round(player.pokemon[pot - 1].maxhp *0.5):
                                        player.pokemon[pot - 1].hp = player.pokemon[pot - 1].maxhp
                                        type(f"{player.pokemon[pot - 1].name} healed by half its health!\n")
                                        what_to_do = False
                                    else:
                                        player.pokemon[pot - 1].hp = round(player.pokemon[pot - 1].maxhp *0.5) + player.pokemon[pot - 1].hp
                                        type(f"{player.pokemon[pot - 1].name} healed by half health!")
                                        what_to_do = False
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
                                revive_poke = int(input("\nChoose Your Pokemon To Revive! (Number): "))
                                if mc_poke.status == "Alive":
                                    type(f"{mc_poke.name} is not knocked out, you can't use a Revive!")
                                else:
                                    player.pokemon[revive_poke - 1].hp = player.pokemon[revive_poke - 1].maxhp
                                    player.revive = player.revive - 1
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
                    return
        else:
            #Enemy attack
            abcd = len(enemy_poke.moves) - 1
            abc = random.randint(0, abcd)
            type(f"Enemy {enemy_poke.name} used {enemy_poke.moves[abc].name}!\n")
            crit_or = random.randint(1, 30)
            crit = 1
            if crit_or == 15:
                crit = 2
                type("Enemy Critical Damage!\n")
            if random.randint(1, 100) < enemy_poke.moves[abc].accuracy:
                effec = effective(enemy_poke, mc_poke, abc)
                damag = round((enemy_poke.lvl + enemy_poke.atk + enemy_poke.moves[abc].power - mc_poke.defn) / 6 * crit * effec)
                mc_poke.hp = mc_poke.hp - damag
                type(f"Enemy {enemy_poke.name} did {damag} damage!\n")
            if mc_poke.hp <= 0:
                mc_poke.status = "Dead"
                type(f"{mc_poke.name} has been knocked out!\n")
                for i in range(0, len(player.pokemon)):
                    if player.pokemon[i].status == "Dead":
                        type("Oh no, one of your Pokemon has been knocked out...\n")
                        type("You lose and black out...\n")
                        type("...\n")
                        type("Your Pokemon got healed!\n")
                        player.pokemon[i].hp = player.pokemon[i].maxhp
                        win_or_no = "Lose"
                        return win_or_no

    if win:
        type("You won!")
        type(f"You got ${money}!\n")
        player.money = player.money + money
        type("You got a free healing!\n")
        for i in range(0, len(player.pokemon)):
            player.pokemon[i].hp = player.pokemon[i].maxhp
        for a in range(0, len(enemy.pokemon)):
            enemy.pokemon[a].hp = enemy.pokemon[a].maxhp


def levelup(poke):
    poke.lvl = poke.lvl + 1
    xpb = poke.lvl - 5
    poke.maxexp = 10 * xpb
    poke.hp = poke.hp + 2
    poke.maxhp = poke.maxhp + 2
    poke.atk = poke.atk + 2
    poke.defn = poke.defn + 2
    poke.exp = 0
    #Start 3
    if poke.name == "Bulbasaur":
        if poke.lvl == 6:
            poke.moves.append(vinewhip)
            type(f"{poke.name} Learned {vinewhip.name}\n")
        if poke.lvl == 16:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Ivysaur!\n")
            poke.name = "Ivysaur"
            poke.moves.append(razorleaf)
            type(f"{poke.name} Learned {razorleaf.name}\n")
        if poke.lvl == 32:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Venusaur!\n")
            poke.name = "Venusaur"
            poke.moves.append(venoshock)
            type(f"{poke.name} Learned {venoshock.name}\n")
        if poke.lvl == 55:
            poke.moves.append(solarbeam)
            type(f"{poke.name} Learned {solarbeam.name}\n")

    if poke.name == "Charmander":
        if poke.lvl == 6:
            poke.moves.append(ember)
            type(f"{poke.name} Learned {ember.name}\n")
        if poke.lvl == 16:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Charmeleon!\n")
            poke.name = "Charmeleon"
            poke.moves.append(dragonbreath)
            type(f"{poke.name} Learned {dragonbreath.name}\n")
        if poke.lvl == 32:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Charizard!\n")
            poke.name = "Charizard"
            poke.moves.append(flamethrower)
            type(f"{poke.name} Learned {flamethrower.name}\n")
        if poke.lvl == 55:
            poke.moves.append(inferno)
            type(f"{poke.name} Learned {inferno.name}\n")

    if poke.name == "Squirtle":
        if poke.lvl == 6:
            poke.moves.append(watergun)
            type(f"{poke.name} Learned {watergun.name}\n")
        if poke.lvl == 16:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Wartortle!\n")
            poke.name = "Wartortle"
            poke.moves.append(waterpulse)
            type(f"{poke.name} Learned {waterpulse.name}\n")
        if poke.lvl == 32:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Blastoise!\n")
            poke.name = "Blastoise"
            poke.moves.append(aquatail)
            type(f"{poke.name} Learned {aquatail.name}\n")
        if poke.lvl == 55:
            poke.moves.append(hydropump)
            type(f"{poke.name} Learned {hydropump.name}\n")
    #City 1
    if poke.name == "Pidgey":
        if poke.lvl == 6:
            poke.moves.append(gust)
            type(f"{poke.name} Learned {gust.name}\n")
        if poke.lvl == 18:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Pidgeotto!\n")
            poke.name = "Pidgeotto"
            poke.moves.append(wingattack)
            type(f"{poke.name} Learned {wingattack.name}\n")
        if poke.lvl == 36:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Pidgeot!\n")
            poke.name = "Pidgeot"
            poke.moves.append(razorwind)
            type(f"{poke.name} Learned {razorwind.name}\n")

    if poke.name == "Pikachu":
        if poke.lvl == 6:
            poke.moves.append(thundershock)
            type(f"{poke.name} Learned {thundershock.name}\n")
        if poke.lvl == 16:
            poke.moves.append(spark)
            type(f"{poke.name} Learned {spark.name}\n")
        if poke.lvl == 32:
            poke.moves.append(thunderbolt)
            type(f"{poke.name} Learned {thunderbolt.name}\n")
        if poke.lvl == 55:
            poke.moves.append(thunder)
            type(f"{poke.name} Learned {thunder.name}\n")
    #City 2
    if poke.name == "Sandshrew":
        if poke.lvl == 30:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Sandslash!\n")
            poke.name = "Sandslash"
            poke.moves.append(earthquake)
            type(f"{poke.name} Learned {earthquake.name}\n")
    if poke.name == "Kirlia":
        if poke.lvl == 30:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Gardevoir!\n")
            poke.name = "Gardevoir"
            poke.moves.append(psychic)
            type(f"{poke.name} Learned {psychic.name}\n")
        if poke.lvl == 55:
            poke.moves.append(futuresight)
            type(f"{poke.name} Learned {futuresight.name}\n")
    #City 3
    if poke.name == "Magnemite":
        if poke.lvl == 30:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Magneton!\n")
            poke.name = "Magneton"
            poke.moves.append(flashcannon)
            type(f"{poke.name} Learned {flashcannon.name}\n")
        if poke.lvl == 55:
            poke.moves.append(zapcannon)
            type(f"{poke.name} Learned {zapcannon.name}\n")
    if poke.name == "Koffing":
        if poke.lvl == 30:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Weezing!\n")
            poke.name = "Weezing"
            poke.moves.append(assurance)
            type(f"{poke.name} Learned {assurance.name}\n")
        if poke.lvl == 55:
            poke.moves.append(belch)
            type(f"{poke.name} Learned {belch.name}\n")
    if poke.name == "Dragonair":
        if poke.lvl == 30:
            poke.moves.append(dragonrush)
            type(f"{poke.name} Learned {dragonrush.name}\n")
        if poke.lvl == 55:
            type(f"What? {poke.name} is evolving!\n")
            type(f"Congratulations, {poke.name} evolved into Dragonite!\n")
            poke.name = "Dragonite"
            poke.moves.append(outrage)
            type(f"{poke.name} Learned {outrage.name}\n")
    if poke.name == "Articuno":
        pass


def effective(move, second_poke, numb):
    if move.moves[numb].typ == "Fire":
        if second_poke.type == "Bug" or second_poke.type == "Steel" or second_poke.type == "Grass" or second_poke.type == "Ice":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Rock" or second_poke.type == "Fire" or second_poke.type == "Water" or second_poke.type == "Dragon":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Water":
        if second_poke.type == "Ground" or second_poke.type == "Rock" or second_poke.type == "Fire":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Water" or second_poke.type == "Grass" or second_poke.type == "Dragon":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Grass":
        if second_poke.type == "Ground" or second_poke.type == "Rock" or second_poke.type == "Water":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Flying" or second_poke.type == "Steel" or second_poke.type == "Poison" or second_poke.type == "Bug" or second_poke.type == "Fire" or second_poke.type == "Grass" or second_poke.type == "Dragon":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Normal":
        if second_poke.type == "Ghost":
            type("Does Not Affect!\n")
            return 0
        if second_poke.type == "Fighting":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Flying":
        if second_poke.type == "Fighting" or second_poke.type == "Bug" or second_poke.type == "Grass":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Rock" or second_poke.type == "Steel" or second_poke.type == "Electric":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Electric":
        if second_poke.type == "Flying" or second_poke.type == "Water":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Psychic" or second_poke.type == "Electric" or second_poke.type == "Dragon":
            type("Not Very Effective!\n")
            return 0.5
        if second_poke.type == "Ground":
            type("Does Not Affect!\n")
            return 0
        else:
            return 1
    if move.moves[numb].typ == "Fighting":
        if second_poke.type == "Normal" or second_poke.type == "Dark" or second_poke.type == "Rock" or second_poke.type == "Ice" or second_poke.type == "Steel":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Psychic" or second_poke.type == "Flying" or second_poke.type == "Poison" or second_poke.type == "Bug":
            type("Not Very Effective!\n")
            return 0.5
        if second_poke.type == "Ghost":
            type("Does Not Affect!\n")
            return 0
        else:
            return 1
    if move.moves[numb].typ == "Ghost":
        if second_poke.type == "Ghost" or second_poke.type == "Psychic":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Dark":
            type("Not Very Effective!\n")
            return 0.5
        if second_poke.type == "Normal" or "Fighting":
            type("Does Not Affect!\n")
            return 0
        else:
            return 1
    if move.moves[numb].typ == "Psychic":
        if second_poke.type == "Fighting" or second_poke.type == "Poison":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Steel" or second_poke.type == "Psychic" or second_poke.type == "Dark":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Dark":
        if second_poke.type == "Psychic" or second_poke.type == "Ghost":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Bug" or second_poke.type == "Fighting":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Dragon":
        if second_poke.type == "Dragon":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Steel":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Rock":
        if second_poke.type == "Flying" or second_poke.type == "Bug" or second_poke.type == "Fire" or second_poke.type == "Ice":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Fighting" or second_poke.type == "Ground" or second_poke.type == "Steel":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Ground":
        if second_poke.type == "Poison" or second_poke.type == "Rock" or second_poke.type == "Steel" or second_poke.type == "Fire" or second_poke.type == "Electric":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Flying" or second_poke.type == "Bug" or second_poke.type == "Grass":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Steel":
        if second_poke.type == "Rock" or second_poke.type == "Ice":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Steel" or second_poke.type == "Fire" or second_poke.type == "Water" or second_poke.type == "Electric":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1
    if move.moves[numb].typ == "Ice":
        if second_poke.type == "Flying" or second_poke.type == "Ground" or second_poke.type == "Grass" or second_poke.type == "Dragon":
            type("Super Effective!\n")
            return 2
        if second_poke.type == "Steel" or second_poke.type == "Fire" or second_poke.type == "Water" or second_poke.type == "Ice":
            type("Not Very Effective!\n")
            return 0.5
        else:
            return 1


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
    while pick:
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
                player.pokemon[0].ViewStats()
                pick = False
            elif starter_poke == 2:
                type("Congratulations! You chose Squirtle\n")
                player.pokemon.append(squirtle)
                player.pokemon[0].ViewStats()
                pick = False
            elif starter_poke == 3:
                type("Congratulations! You chose Bulbasaur\n")
                player.pokemon.append(bulbasaur)
                player.pokemon[0].ViewStats()
                pick = False
        except ValueError:
            print("ERROR: Please pick a number!\n")

    #First Battle with Rival
    type("Ash: Alright! Now you got your first Pokemon, Let's battle!"
         " By the way, I chose Pikachu, hehe!\n")
    win_or_lose = battle("ASH", ash, "trainer", 10, 150)
    if win_or_lose == "Lose":
        type("Ash: Yay!, I Won, It's okay, I'll heal your Pokemon!\n")
        type("...\n")
    if win_or_lose == "Win":
        type("Ash: Aww.. I Lost, I'll heal your Pokemon!\n")
        player.pokemon[0].hp = player.pokemon[0].maxhp

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
    loopy = True
    while loopy:
        win_or_lose_grunt = battle("Team Rocket Grunt", grunt_noob, "trainer", 10, 200)
        if win_or_lose_grunt == "Win":
            type(f"{name}: Return his Pokemon!\n")
            type("Team Rocket Grunt: Okay, okay fine you win this time! But Team Rocket will get you one day!")
            type("???: Thankyou kind sir, what's your name?\n")
            type(f"{name}: My name is {name}, I come from Pallete Town\n")
            type("Bobby: My name is Bobby, I will remember this! Thankyou!\n")
            type(f"{name}: Oh, do you know where the next city is? I'm trying to get there\n")
            type("Bobby: Oh, don't worry, my father is the mayor of the city! I'll take you there, my father is also the Pokemon Gym Leader!\n")
            type(f"{name:}: Alright, I'll accept your offer\n")
            type("Bobby: Okay, follow me!\n")
            type("Heading to Bublè city...")
            type("...")
            type("..")
            type(".\n")
            main(name)
        if win_or_lose_grunt == "Lose":
            type("Team Rocket Grunt: Hahaha! Now I'll take your Pokemon too!\n")
            type("Restarting battle...")


def main(name):
    type("Bobby: Alright, we arrived at Bublè city! Wonderful isn't it?\n")
    type(f"{name}: Ah, yes!\n")
    type("Gym Leader Jose: Hello son! Welcome back, who is this?\n")
    type(f"Bobby: His name is {name}, he saved me and my Pokemon from a bad guy!\n")
    type(f"Gym Leader Jose: I see, thankyou {name}\n")
    type("Gym Leader Jose: You seem like a Pokemon Trainer, you should visit my Gym and get a badge soon!\n")
    type(f"{name}: Okay, I need to find my friend Ash first\n")
    type(f"Ash: {name}? Hey! Over Here! I just got my badge from the Gym Leader, hehe\n")
    type(f"Ash: You just arrived? Okay then I'll head to the next city, better catch up!\n")
    first = True
    while first:
        type("(1). Route 101")
        type("(2). PokeCenter")
        type("(3). PokeMart")
        type("(4). Gym *Recommended Level 15*")
        type("(5). View Pokemon")
        type("(6). View Backpack")
        where = int(input("Where Should I Go? "))
        try:
            if where > 0 and where < 7:
                if where == 1:
                    wild_random = random.randint(1,10)
                    if wild_random == 10:
                        pikachu.hp = pikachu.maxhp
                        p = battle("PIKACHU", pika, "wild", 30, 50)
                        if p == "escape":
                            pass
                        if p == "catch":
                            pass
                    else:
                        pidgey_noob.hp = pidgey_noob.maxhp
                        pi = battle("PIDGEY", pidgey, "wild", 25, 50)
                        if pi == "escape":
                            pass
                        if pi == "catch":
                            pass
                elif where == 2:
                    type("Welcome to the PokeCenter, let me heal your Pokemon!\n")
                    type("Healed all your Pokemon!\n")
                    for i in range(0, len(player.pokemon)):
                        player.pokemon[i].hp = player.pokemon[i].maxhp
                elif where == 3:
                    mart = True
                    while mart:
                        type("Welcome to the PokeMart\n")
                        type("(1). Pokeballs = $200")
                        type("(2). Potions = $200")
                        type("(3). Revive = $1000")
                        type("(4). Exit")
                        type(f"Your Money: ${player.money}")
                        buy = int(input("What Should I Buy? "))
                        try:
                            if buy >= 0 and buy <= 5:
                                if buy == 1:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Pokeball!")
                                        player.pokeballs = player.pokeballs + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 2:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Potion!")
                                        player.potion = player.potion + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 3:
                                    if player.money < 1000:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Revive!")
                                        player.revive = player.revive + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 4:
                                    mart = False
                            else:
                                print("ERROR: Please choose between 1-4\n")
                        except ValueError:
                            print("ERROR: Please choose a number\n")
                elif where == 4:
                    type("Gym Leader Jose: Welcome to my Gym, If you want a badge, you must defeat me in a Pokemon battle!\n")
                    jose = battle("GYM LEADER JOSE", gym_jose, "trainer", 200, 1000)
                    if jose == "Win":
                        type("Gym Leader Jose: Congratulations, here is the Gym Badge! I wish you the best of luck, if you need help, you can come to me!\n")
                        type(f"{name}: Thanks Jose!\n")
                        first = False
                    if jose == "Lose":
                        type("Gym Leader Jose: Nice try! You should practice in Route 101 and level up first before you fight me again!\n")
                elif where == 5:
                    try:
                        type("\nYour Pokemon:")
                        for i in range(1, len(player.pokemon) + 1):
                            numb = 1 * i
                            type(f"{numb}. {player.pokemon[i - 1].name}")
                        check_stat = int(input("\nChoose Your Pokemon To Check Stats!(Number): "))
                        try:
                            if check_stat > 0:
                                player.pokemon[check_stat - 1].ViewStats()
                            else:
                                print("ERROR: Can't go below 0!\n")
                        except IndexError:
                            print("ERROR: Must be in range of your pokemon!\n")
                    except ValueError:
                        print("ERROR: Please choose a number!\n")
                elif where == 6:
                    player.ViewBackpack()
            else:
                print("ERROR: Please choose between 1-7\n")
        except ValueError:
            print("ERROR: Please choose a number\n")

    type("Bobby: Hey, I heard you beat my dad, wow you must be strong!\n")
    type("Bobby: With the Gym Badge, you can probably head to the next city, I think it's called Morning City\n")
    type(f"{name}: Okay, thanks for your help!\n")
    type("Heading to Route 201...")
    type("...")
    type("..")
    type(".\n")
    type("Team Rocket Grunt: Hey, You! I heared you stirred some trouble, now I'm here to beat you!\n")
    medium = True
    while medium:
        med = battle("TEAM ROCKET GRUNT", grunt_med, "trainer", 100, 500)
        if med == "Lose":
            type("Team Rocket Grunt: Hahaha! I knew you were weak!\n")
        if med == "Win":
            type("Team Rocket Grunt: Huh, you seem strong, but don't worry, we'll rule the world soon!\n")
            medium = False
    type(f"{name}: He ran away... Well, I better head to the next city\n")
    second = True
    while second:
        type("(1). Route 201")
        type("(2). PokeCenter")
        type("(3). PokeMart")
        type("(4). Gym 2 *Recommended Level 30*")
        type("(5). View Pokemon")
        type("(6). View Backpack")
        where = int(input("Where Should I Go? "))
        try:
            if where > 0 and where < 7:
                if where == 1:
                    wild_random = random.randint(1, 10)
                    if wild_random == 10:
                        r = battle("RALTS", ralts, "wild", 80, 100)
                        if r == "escape":
                            pass
                        if r == "catch":
                            pass
                    else:
                        s = battle("SANDSHREW", sandshrew, "wild", 70, 100)
                        if s == "escape":
                            pass
                        if s == "catch":
                            pass
                elif where == 2:
                    type("Welcome to the PokeCenter, let me heal your Pokemon!\n")
                    for i in range(0, len(player.pokemon) - 1):
                        player.pokemon[i].hp = player.pokemon[i].maxhp
                elif where == 3:
                    mart = True
                    while mart:
                        type("Welcome to the PokeMart\n")
                        type("(1). Pokeballs = $200")
                        type("(2). Potions = $200")
                        type("(3). Revive = $1000")
                        type("(4). Exit")
                        type(f"Your Money: ${player.money}")
                        buy = int(input("What Should I Buy? "))
                        try:
                            if buy >= 0 and buy <= 5:
                                if buy == 1:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Pokeball!")
                                        player.pokeballs = player.pokeballs + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 2:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Potion!")
                                        player.potion = player.potion + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 3:
                                    if player.money < 1000:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Revive!")
                                        player.revive = player.revive + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 4:
                                    mart = False
                            else:
                                print("ERROR: Please choose between 1-4\n")
                        except ValueError:
                            print("ERROR: Please choose a number\n")
                elif where == 4:
                    type("Gym Leader Justin: Welcome to my Gym, If you want a badge, you must defeat me in a Pokemon battle!\n")
                    justin = battle("GYM LEADER JUSTIN", gym_justin, "trainer", 150, 2500)
                    if justin == "Win":
                        type("Gym Leader Justin: Congratulations, here is the Gym Badge!\n")
                        type("Gym Leader Justin: You should visit Saiyan City, there you can get the final badge and try to defeat the Pokemon Champion")
                        type(f"{name}: Thanks Justin!\n")
                        second = False
                    if justin == "Lose":
                        type("Gym Leader Jose: Nice try! You should practice in Route 201 and level up first before you fight me again!\n")
                elif where == 5:
                    try:
                        type("\nYour Pokemon:")
                        for i in range(1, len(player.pokemon) + 1):
                            numb = 1 * i
                            type(f"{numb}. {player.pokemon[i - 1].name}")
                        check_stat = int(input("\nChoose Your Pokemon To Check Stats!(Number): "))
                        try:
                            if check_stat > 0:
                                player.pokemon[check_stat - 1].ViewStats()
                            else:
                                print("ERROR: Can't go below 0!\n")
                        except IndexError:
                            print("ERROR: Must be in range of your pokemon!\n")
                    except ValueError:
                        print("ERROR: Please choose a number!\n")
                elif where == 6:
                    player.ViewBackpack()
            else:
                print("ERROR: Please choose between 1-7\n")
        except ValueError:
            print("ERROR: Please choose a number\n")

    type("Heading to Route 301...")
    type("...")
    type("..")
    type(".\n")
    type(f"Gym Leader Jose: Hey wait up {name}! You have to help us in Bublè city, Team Rocket has recently raided the nearby cave where"
         f" they say that Articuno stays at, and they are trying to use Articuno to destroy the world!\n")
    type(f"Gym Leader Jose: Professor Oak told me to give you this\n")
    type(f"Obtained Masterball!\n")
    type(f"Gym Leader Jose: Use it wisely...\n")
    type(f"Gym Leader Jose: Alright, follow me to the cave!\n")
    type("Heading to Articuno's Cave")
    type("...")
    type("..")
    type(".\n")
    type(f"Team Rocket Leader Dason: You must be the trainer that has been interfering with us!\n")
    type(f"Team Rocket Leader Dason: Hahaha! You're too late, Articuno has been chained and is sleeping!\n")
    type(f'Gym Leader Jose: {name}, hurry use the Masterball!\n')
    type(f"{name}: Okay!\n")
    type(f"Used Masterball on Articuno!\n")
    type(f"Successfully captured Articuno\n")
    type(f"Team Rocket Leader Dason: That's it! I will defeat you and make you regret interfering with us!\n")
    final_dason = True
    while final_dason:
        das = battle("TEAM ROCKET LEADER DASON", dason, "trainer", 250, 5000)
        if das == "Lose":
            type(f"Team Rocket Leader Dason: Hahaha! You weakling, now give me Articuno!\n")
        if das == "Win":
            type(f"Team Rocket Leader Dason: No. You can't defeat me. How?\n")
            type(f"Team Rocket Leader Dason: Fine! We'll leave you alone!\n")
            final_dason = False

    type(f"Gym Leader Jose: ...")
    type(f"Gym Leader Jose: Wow, thank you for all your effort {name}, you can keep Articuno since you seem like a worthy Trainer!\n")
    type(f"Gym Leader Jose: You can continue your journey and become the Pokemon Champion, I belive you can do it!\n")

    third = True
    while third:
        type("(1). Route 301")
        type("(2). PokeCenter")
        type("(3). PokeMart")
        type("(4). Gym 3 *Recommended Level 45*")
        type("(5). View Pokemon")
        type("(6). View Backpack")
        where = int(input("Where Should I Go? "))
        try:
            if where > 0 and where < 7:
                if where == 1:
                    wild_random = random.randint(1, 10)
                    if wild_random == 10:
                        d = battle("DRAGONAIR", dragonair, "wild", 150, 150)
                        if d == "escape":
                            pass
                        if d == "catch":
                            pass
                    elif wild_random >= 5 and wild_random < 10:
                        m = battle("MAGNEMITE", magnemite, "wild", 100, 150)
                        if m == "escape":
                            pass
                        if m == "catch":
                            pass
                    elif wild_random >= 1 and wild_random < 5:
                        w = battle("WEEZING", weezing, "wild", 100, 150)
                        if w == "escape":
                            pass
                        if w == "catch":
                            pass
                elif where == 2:
                    type("Welcome to the PokeCenter, let me heal your Pokemon!\n")
                    for i in range(0, len(player.pokemon) - 1):
                        player.pokemon[i].hp = player.pokemon[i].maxhp
                elif where == 3:
                    mart = True
                    while mart:
                        type("Welcome to the PokeMart\n")
                        type("(1). Pokeballs = $200")
                        type("(2). Potions = $200")
                        type("(3). Revive = $1000")
                        type("(4). Exit")
                        type(f"Your Money: ${player.money}")
                        buy = int(input("What Should I Buy? "))
                        try:
                            if buy >= 0 and buy <= 5:
                                if buy == 1:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Pokeball!")
                                        player.pokeballs = player.pokeballs + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 2:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Potion!")
                                        player.potion = player.potion + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 3:
                                    if player.money < 1000:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Revive!")
                                        player.revive = player.revive + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 4:
                                    mart = False
                            else:
                                print("ERROR: Please choose between 1-4\n")
                        except ValueError:
                            print("ERROR: Please choose a number\n")
                elif where == 4:
                    type("Gym Leader Henry: Welcome to my Gym, If you want a badge, you must defeat me in a Pokemon battle!\n")
                    type("Gym Leader Henry: I heared you defeated Dason, you must be strong! Lets test it!\n")
                    henry = battle("GYM LEADER HENRY", gym_henry, "trainer", 250, 2500)
                    if henry == "Win":
                        type("Gym Leader Henry: Congratulations, here is the Gym Badge! You truly are worthy!\n")
                        type(f"{name}: Thanks Henry!\n")
                        third = False
                    if henry == "Lose":
                        type("Gym Leader Henry: Nice try! You should practice in Route 201 and level up first before you fight me again!\n")

                elif where == 5:
                    try:
                        type("\nYour Pokemon:")
                        for i in range(1, len(player.pokemon) + 1):
                            numb = 1 * i
                            type(f"{numb}. {player.pokemon[i - 1].name}")
                        check_stat = int(input("\nChoose Your Pokemon To Check Stats!(Number): "))
                        try:
                            if check_stat > 0:
                                player.pokemon[check_stat - 1].ViewStats()
                            else:
                                print("ERROR: Can't go below 0!\n")
                        except IndexError:
                            print("ERROR: Must be in range of your pokemon!\n")
                    except ValueError:
                        print("ERROR: Please choose a number!\n")
                elif where == 6:
                    player.ViewBackpack()
            else:
                print("ERROR: Please choose between 1-7\n")
        except ValueError:
            print("ERROR: Please choose a number\n")

    type(f"Heading to Victory Road...")
    type(f"...")
    type("..")
    type(".\n")
    type("Ash: Hey! You're finally here, I already beat every Trainer here!\n")
    type(f"{name}: So You're now the Pokemon Champion?\n")
    type("Ash: Haha! Yes, are you here to claim my title?\n")
    type("Ash: Well, lets have a final battle! Come see me when you're ready!\n")

    finaL_ash = True
    while finaL_ash:
        type("(1). Route 301")
        type("(2). PokeCenter")
        type("(3). PokeMart")
        type("(4). Final Battle Against Ash *Recommended Level 60*")
        type("(5). View Pokemon")
        type("(6). View Backpack")
        where = int(input("Where Should I Go? "))
        try:
            if where > 0 and where < 7:
                if where == 1:
                    wild_random = random.randint(1, 10)
                    if wild_random == 10:
                        dd = battle("DRAGONAIR", dragonair, "wild", 200, 250)
                        if dd == "escape":
                            pass
                        if dd == "catch":
                            pass
                    elif wild_random >= 5 and wild_random < 10:
                        mm = battle("MAGNEMITE", magnemite, "wild", 150, 250)
                        if mm == "escape":
                            pass
                        if mm == "catch":
                            pass
                    elif wild_random >= 1 and wild_random < 5:
                        ww = battle("WEEZING", weezing, "wild", 150, 250)
                        if ww == "escape":
                            pass
                        if ww == "catch":
                            pass
                elif where == 2:
                    type("Welcome to the PokeCenter, let me heal your Pokemon!\n")
                    for i in range(0, len(player.pokemon) - 1):
                        player.pokemon[i].hp = player.pokemon[i].maxhp
                elif where == 3:
                    mart = True
                    while mart:
                        type("Welcome to the PokeMart\n")
                        type("(1). Pokeballs = $200")
                        type("(2). Potions = $200")
                        type("(3). Revive = $1000")
                        type("(4). Exit")
                        type(f"Your Money: ${player.money}")
                        buy = int(input("What Should I Buy? "))
                        try:
                            if buy >= 0 and buy <= 5:
                                if buy == 1:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Pokeball!")
                                        player.pokeballs = player.pokeballs + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 2:
                                    if player.money < 200:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Potion!")
                                        player.potion = player.potion + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 3:
                                    if player.money < 1000:
                                        type("You can't afford that yet!\n")
                                    else:
                                        type("Thankyou for purchasing a Revive!")
                                        player.revive = player.revive + 1
                                        player.money = player.money - 200
                                        type(f"Money left: {player.money}")
                                elif buy == 4:
                                    mart = False
                            else:
                                print("ERROR: Please choose between 1-4\n")
                        except ValueError:
                            print("ERROR: Please choose a number\n")
                elif where == 4:
                    type(f"Pokemon Champion Ash: You like my title? Haha! Let's see if you can win against me!\n")
                    ashh = battle("POKEMON CHAMPION ASH", champion_ash, "trainer", 1000, 10000)
                    if ashh == "Win":
                        type("Pokemon Champion Ash: Wow, you won, this is surprising...\n")
                        type("Pokemon Champion Ash: I guess you are the new Pokemon Champ!\n")
                        type(f"Title Added: Pokemon Champion {name}!\n")
                        type(f"Pokemon Champion {name}: I Did it!!\n")
                        finaL_ash = False
                    if ashh == "Lose":
                        type("Pokemon Champion Ash: Nice try! You should practice in Route 201 and level up first before you fight me again!\n")

                elif where == 5:
                    try:
                        type("\nYour Pokemon:")
                        for i in range(1, len(player.pokemon) + 1):
                            numb = 1 * i
                            type(f"{numb}. {player.pokemon[i - 1].name}")
                        check_stat = int(input("\nChoose Your Pokemon To Check Stats!(Number): "))
                        try:
                            if check_stat > 0:
                                player.pokemon[check_stat - 1].ViewStats()
                            else:
                                print("ERROR: Can't go below 0!\n")
                        except IndexError:
                            print("ERROR: Must be in range of your pokemon!\n")
                    except ValueError:
                        print("ERROR: Please choose a number!\n")
                elif where == 6:
                    player.ViewBackpack()
            else:
                print("ERROR: Please choose between 1-7\n")
        except ValueError:
            print("ERROR: Please choose a number\n")

    type("Professor Oak: Ah, good to see you two\n")
    type(f"Professor Oak: Congratulations {name}, or should I say Pokemon Champion {name}\n")
    type(f"Professor Oak: Your journey is complete, and thank you for your help in defeating Team Rocket...")
    type("...")
    type("...")
    type("...\n")
    type("Mom: You finally did it! Your journey is complete!\n")
    type("=====================")
    type("THE END")
    type("THANKYOU FOR PLAYING")
    type("BY: DYLAN 11F")
    type("=====================")
    finaL_ash = False


a = True
if __name__ == '__main__':
    intro()
