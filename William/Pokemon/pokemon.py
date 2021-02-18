import random
from colorama import Fore, Back, Style
import dialogue
import time

pokemon_names = ["Pikachu", "Eevee", "Pliplup", "Snorlax", "Ditto", "Gengar", "Charmander", "Bulbasaur", "Gyarados",
                 "Fletchling", "Arceus", "Psyduck", "Lopunny", "Victiny", "Buble", "Mierln", "Huwahh"]
pokemon_attacks = ["Tackle", "Scratch", "Growl", "Fire breath", "Head bang", "Water Gun", "Stomp", "Thunder Strike",
                   "Splash Hit", "Fireball", "Vine Snap", "Forest Voice", "Wind Tunnel", "Slap", "Punch", "Baked Alive",
                   "Close-Up"]
pokemon_type = ["Fire", "Water", "Electric", "Grass"]


class Pokemon:
    # Pokémon Class

    def __init__(self, name, lvl, ptype, hp, maxhp, atk, defn, speed, exp, maxep, wild=False):
        self.name = name
        self.nickname = name
        self.lvl = lvl
        self.type = ptype
        self.hp = hp
        self.max_hp = maxhp
        self.atk = atk
        self.defense = defn
        self.speed = speed
        self.exp = exp
        self.max_exp = maxep
        self.attacks = []
        self.wild = wild

    def view_stats(self):
        # return the Pokémon's stats when called
        print("")
        print(f" {self.nickname} ".center(50, "="))
        print("")
        dialogue.writen(f"name: {self.name}")
        print("")
        dialogue.writen(f"type: {self.type}")
        print("")
        dialogue.writen(f"lvl : {self.lvl}")
        print("")
        dialogue.writen(f"Exp : {self.exp}/{self.max_exp}")
        print("")
        dialogue.writen(f"HP  : {self.hp}/{self.max_hp}")
        print("")
        dialogue.writen(f"ATK : {self.atk}")
        print("")
        dialogue.writen(f"DEF : {self.defense}")
        print("")
        dialogue.writen(f"SPD : {self.speed}")
        print("\n")
        print(f"".center(50, "="))

    def lvlup(self):
        if self.exp >= self.max_exp:
            self.lvl += 1
            self.hp += 10
            self.max_hp += 10
            self.atk += 10
            self.defense += 10
            self.exp = 0
            self.max_exp += 10

        if self.lvl == 6:
            if self.name == "Bulbasaur":
                self.attacks.append("Leech Seed")
            elif self.name == "Charmander":
                self.attacks.append("Smoke Screen")
            elif self.name == "Squirtle":
                self.attacks.append("Withdraw")
            else:
                self.attacks.append(random.choice(pokemon_attacks))

        if self.lvl == 10:
            if self.name == "Bulbasaur":
                self.attacks.append("Razor Leaf")
            elif self.name == "Charmander":
                self.attacks.append("Dragon Breath")
            elif self.name == "Squirtle":
                self.attacks.append("Water Pulse")
                self.attacks.append(random.choice(pokemon_attacks))


class Trainer:

    def __init__(self):
        self.name = None
        self.money = 0
        self.pokemons = []
        self.potions = 3
        self.pokeball = 3

    def show_pokemons(self, full):
        # shows the pokemon player has and their stats

        print("\n")
        print(f" My Pokémons ".center(50, "="))
        a = 1
        for i in self.pokemons:
            print(f"{a}. {i.nickname}")
            a += 1
        print(f"".center(50, "="))

        if full:
            while True:
                try:
                    check_pokemon = int(input(Fore.CYAN + "\nCheck the stats of? [number] " + Style.RESET_ALL))
                    if check_pokemon <= len(self.pokemons):
                        self.pokemons[check_pokemon - 1].view_stats()
                        break
                    else:
                        print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nNumber does not exist" + Style.RESET_ALL + "\n")
                except ValueError:
                    print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nplease enter a number" + Style.RESET_ALL + "\n")


def player1_turn(player, pokemon1, pokemon2):
    while True:
        print("1. Attack")
        print("2. Potion")
        print("3. Catch\n")
        dialogue.writen(Fore.CYAN + "What do you want to do? " + Style.RESET_ALL)
        try:
            user_chose = int(input(""))

            if user_chose == 1:
                for i in range(len(pokemon1.attacks)):
                    print(f"{i + 1}.{pokemon1.attacks[i]}", end=" | ")
                print("")
                dialogue.writen(Fore.CYAN + "Which one do you want to use? " + Style.RESET_ALL)
                while True:
                    try:
                        user_attack = int(input(""))
                        attack(pokemon1, pokemon2, pokemon1.attacks[user_attack - 1])
                        return None
                    except ValueError:
                        print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nplease enter a number" + Style.RESET_ALL + "\n")

                    except IndexError:
                        print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nNumber does not exist" + Style.RESET_ALL + "\n")

            elif user_chose == 2:
                if player.potions > 1:
                    print(Fore.GREEN + "Used 1 potion" + Style.RESET_ALL)
                    heal_percentage = (random.randint(45, 55) / 100)
                    heal = pokemon1.max_hp * heal_percentage
                    pokemon1.hp = pokemon1.hp + heal
                    if pokemon1.hp > pokemon1.max_hp:
                        pokemon1.hp = pokemon1.max_hp
                    player.potions -= 1
                else:
                    dialogue.writen(Fore.RED + Style.BRIGHT + "\n\nYou don't have enough potions\n\n" + Style.RESET_ALL)
                break

            elif user_chose == 3:
                if pokemon2.wild and player.pokeball > 0:
                    chance = round(100 / (pokemon2.max_hp / pokemon2.hp))
                    if random.randint(0, 75) > chance:
                        pokemon2.attacks = []
                        pokemon2.hp = pokemon2.max_hp
                        for _ in range(round(pokemon2.lvl/3)):
                            pokemon2.attacks.append(random.choice(pokemon_attacks))
                        player.pokemons.append(pokemon2)
                        player.pokeball -= 1
                        print(Fore.CYAN + "\nYou caught the pokemon\n" + Style.RESET_ALL)
                        return "Caught"
                    else:
                        player.pokeball -= 1
                        print("Failed")
                        break
                elif not pokemon2.wild:
                    dialogue.writen(Fore.RED + Style.BRIGHT + "\n\nYou can't catch that pokémon\n\n" + Style.RESET_ALL)
                elif player.pokeball == 0:
                    dialogue.writen(
                        Fore.RED + Style.BRIGHT + "\n\nYou don't have enough pokeballs\n\n" + Style.RESET_ALL)
            else:
                print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nNumber does not exist" + Style.RESET_ALL + "\n")

        except ValueError:
            print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nplease enter a number" + Style.RESET_ALL + "\n")


def attack(attacker, attacked, attack_used):
    damage = round((((((2 / 5 * attacker.lvl) + 2) * random.randint(1, 2) * attacker.atk / attacked.defense) / 50) + 2)
                   * random.randint(3, 7))
    attacked.hp -= damage
    print(Fore.BLUE + f"{attacker.name} used {attack_used} and it deals {damage} damage" + Style.RESET_ALL)


def battle(player, enemy):
    player.show_pokemons(False)

    while True:
        try:
            dialogue.writen(Fore.CYAN + "Which pokémon do you want to use")
            user_choose = int(input(" [Number]: " + Style.RESET_ALL))
            if user_choose <= len(player.pokemons):
                fight_poke = user_choose - 1
                break
            else:
                print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nNumber does not exist" + Style.RESET_ALL + "\n")
        except ValueError:
            print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nplease enter a number" + Style.RESET_ALL + "\n")

    pokemon1 = player.pokemons[fight_poke]
    pokemon2 = enemy[random.randint(0, len(enemy) - 1)]

    print("\n")
    print(f" Enemy's Pokémons ".center(50, "="))
    pokemon2.view_stats()

    def display_health():
        health1 = round(30 / pokemon1.max_hp * pokemon1.hp)
        health2 = round(30 / pokemon2.max_hp * pokemon2.hp)
        print("\n" * 3)
        print(" Health ".center(50, "="))
        print("\n")
        dialogue.writen("{:<17}:{:>1}".format(pokemon1.nickname, "#" * health1))
        print("\n")
        dialogue.writen("{:<17}:{:>1}".format(pokemon2.nickname, "#" * health2))
        print("\n")
        print("\n")
        print("".center(50, "="))
        print("")

    display_health()

    while pokemon1.hp >= 0 and pokemon2.hp >= 0:

        def checkloss():
            if pokemon1.hp <= 0:
                pokemon1.hp = 0
                print(Fore.RED + Style.BRIGHT + "\nYOU LOST\n" + Style.RESET_ALL)
                xp = random.randint(2, 5)
                gold = random.randint(3, 6) * 10
                pokemon1.exp += xp
                player.money += gold
                print(Fore.CYAN + f"Your pokemon received {xp}xp")
                print(f"You received {gold}gold" + Style.RESET_ALL)
                pokemon1.lvlup()
                pokemon1.hp = pokemon1.max_hp
                return True

            elif pokemon2.hp <= 0:
                print(Fore.GREEN + Style.BRIGHT + "\nYOU WON\n" + Style.RESET_ALL)
                pokemon1.exp += 10
                xp = random.randint(5, 10)
                gold = random.randint(7, 10) * 10
                player.money += gold
                print(Fore.CYAN + f"Your pokemon received {xp}xp")
                print(f"You received {gold}gold" + Style.RESET_ALL)
                pokemon1.lvlup()
                pokemon1.hp = pokemon1.max_hp
                return True

            else:
                return False

        if pokemon1.speed >= pokemon2.speed:
            time.sleep(0.5)
            if player1_turn(player, pokemon1, pokemon2) == "Caught":
                pokemon1.hp = pokemon1.max_hp
                return None
            if checkloss():
                break
            time.sleep(0.5)
            display_health()
            time.sleep(0.5)
            attack(pokemon2, pokemon1, pokemon2.attacks[random.randint(0, len(pokemon2.attacks) - 1)])
            if checkloss():
                break
            time.sleep(0.5)
            display_health()

        else:
            time.sleep(0.5)
            attack(pokemon2, pokemon1, pokemon2.attacks[random.randint(0, len(pokemon2.attacks) - 1)])
            time.sleep(0.5)
            if checkloss():
                break
            display_health()
            time.sleep(0.5)
            if player1_turn(player, pokemon1, pokemon2) == "Caught":
                pokemon1.hp = pokemon1.max_hp
                return None
            if checkloss():
                break
            display_health()


def add_starter_pokemon(start_pokemon):
    start_pokemon.append(Pokemon("Bulbasaur", 5, "Grass", 45, 45, 49, 49, 45, 0, 10))
    start_pokemon.append(Pokemon("Charmander", 5, "Fire", 39, 39, 52, 43, 65, 0, 10))
    start_pokemon.append(Pokemon("Squirtle", 5, "Water", 44, 44, 48, 65, 43, 0, 10))
    start_pokemon.append(Pokemon("Pikachu", 6, "Electric", 45, 45, 65, 50, 90, 0, 30))


def main():
    start_pokemon = []
    add_starter_pokemon(start_pokemon)
    player = Trainer()
    nathan = Trainer()
    nathan.name = "nathan"
    nathan.pokemons.append(start_pokemon[3])
    nathan.pokemons[0].attacks.append("Thunder Shock")
    nathan.pokemons[0].attacks.append("Thunder Wave")

    if dialogue.title():
        user_name = input(Fore.CYAN + "\nEnter Your name: " + Style.RESET_ALL)
        print("\n\n")
        player.name = user_name

        dialogue.intro(player.name)
        dialogue.writen(Fore.CYAN + "\n\n[1] Grass\n")
        dialogue.writen(Fore.CYAN + "[2] Fire\n")
        dialogue.writen(Fore.CYAN + "[3] Water\n")

        while True:  # First Pokemon Selection

            try:
                choose = int(input("Which one would you like? [1]/[2]/[3] " + Style.RESET_ALL))

                if choose == 1:
                    poke_name = dialogue.bulbasaur()
                    player.pokemons.append(start_pokemon[0])
                    player.pokemons[0].nickname = poke_name
                    player.pokemons[0].attacks.append("Tackle")
                    player.pokemons[0].attacks.append("Vine Whip")
                    break

                elif choose == 2:
                    poke_name = dialogue.charmander()
                    player.pokemons.append(start_pokemon[1])
                    player.pokemons[0].nickname = poke_name
                    player.pokemons[0].attacks.append("Tackle")
                    player.pokemons[0].attacks.append("Ember")
                    break

                elif choose == 3:
                    poke_name = dialogue.squirtle()
                    player.pokemons.append(start_pokemon[2])
                    player.pokemons[0].nickname = poke_name
                    player.pokemons[0].attacks.append("Tackle")
                    player.pokemons[0].attacks.append("Water Gun")
                    break

                else:
                    print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nPlease pick between 1 - 3" + Style.RESET_ALL + "\n")

            except ValueError:
                print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nEnter A Number" + Style.RESET_ALL + "\n")

        del start_pokemon

        dialogue.check_first()
        player.show_pokemons(True)
        dialogue.first_battle()
        battle(player, nathan.pokemons)
        dialogue.ready()
        print("")

        def menu():
            print("")
            print(f" Menu ".center(50, "="))
            print("1. Battle")
            print("2. My Pokémons")
            print("3. Market")
            print("4. Quit")
            print(f"".center(50, "="))
        while True:
            menu()
            while True:
                try:
                    goto = int(input("Go to? "))
                    if goto in range(1, 5):
                        break
                    else:
                        print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nPlease pick between 1 - 4" + Style.RESET_ALL +
                              "\n")

                except ValueError:
                    print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nEnter A Number" + Style.RESET_ALL + "\n")

            if goto == 1:
                guide = player.pokemons[0]
                wild_p_hp = (guide.max_hp + random.randint(-10, 11))
                wild_p = Pokemon(random.choice(pokemon_names), (guide.lvl + random.randint(-2, 2)),
                                 random.choice(pokemon_type), wild_p_hp, wild_p_hp,
                                 (guide.atk + random.randint(-10, 11)), (guide.defense + random.randint(-10, 11)),
                                 (random.randint(0, 100)), 0, 10, wild=True)

                wild_p.attacks = pokemon_attacks[:]
                battle(player, [wild_p])
            elif goto == 2:
                player.show_pokemons(True)
            elif goto == 3:
                while True:
                    print(" Market ".center(50, "="))
                    print(f"My Gold: {player.money}")
                    print("")
                    print("1. Pokeballs - 200 Golds")
                    print("2. Potions - 50 Golds")
                    print("3. Quit")
                    try:
                        buy = int(input("Buy? "))
                        if buy == 1:
                            print(Fore.CYAN + "\nYou have bought 1 pokeball for 200 golds\n" + Fore.RESET)
                            player.pokeball += 1
                            player.money -= 200
                        elif buy == 2:
                            print(Fore.CYAN + "\nYou have bought 1 potion for 50 golds\n" + Fore.RESET)
                            player.potions += 1
                            player.money -= 50
                        elif buy == 3:
                            break
                        else:
                            print(
                                Fore.WHITE + Back.RED + Style.BRIGHT + "\nPlease pick between 1 - 3" + Style.RESET_ALL +
                                "\n")
                    except ValueError:
                        print(Fore.WHITE + Back.RED + Style.BRIGHT + "\nEnter A Number" + Style.RESET_ALL + "\n")

            else:
                print("\n\n" + Fore.WHITE + Back.GREEN + "THANK YOU FOR PLAYING" + Style.RESET_ALL)
                quit()


if __name__ == "__main__":
    main()
