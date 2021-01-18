import random

def menus():
    print("")
    print("1. Add Player")
    print("2. Remove Player")
    print("3. View Players")
    print("4. Devide Players")
    print("5. Clear Players")
    print("5. Quit")

def add(players, name):
    for i in players:
        if i == name.lower():
            return (f"There is a player by the name {name} added before")
    
    players.append(name.lower())
    return(f"Added {name.lower()} to list")


def remove(players, name):
    for i in range(len(players)):
        if players[i] == name.lower():
            item = players[i]
            del players[i]

            return (f"{item} has been removed from the list")
    return(f"{name} is not in player list")


def devide(players):
    t1 = []
    t2 = []
    playercopy = []

    for i in players:
        playercopy.append(i)

    
        random.shuffle(playercopy)

    for a in range(int(round(len(playercopy) / 2))):
        t1.append(playercopy.pop())

    for b in range(len(playercopy)):
        t2.append(playercopy.pop())
        
    return (f"Team 1: {t1}\nTeam 2: {t2}")

def main():
    players = []
    while True:
        menus()
        choice = int(input("\n> "))

        if choice == 1:
            print(add(players, input("Name: ")))

        elif choice == 2:
            print(remove(players, input("Name: ")))

        elif choice == 3:
            print(players)
            
        elif choice == 4:
            print(devide(players))
        
        elif choice == 5:
            players = []

        else:
            break



if __name__ == "__main__":
    main()
        