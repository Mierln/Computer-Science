import random


def menu():
    print("\nTeam Divider")
    print("============")
    print("1. Add Player")
    print("2. View Players")
    print("3. Divide Players")
    print("4. Remove Player")
    print("5. Quit")
    what = int(input("> "))
    return what


player = []


def main():
    i = True
    while i:
        what = menu()
        if what == 1:
            add(input("Name: "))
        elif what == 2:
            view()
        elif what == 3:
            divide()
        elif what == 4:
            pop(input("Who will be removed? "))
        elif what == 5:
            i = False


def add(name):
    if name in player:
        print(f"{name} Already Exists")
    else:
        player.append(name)


def view():
    print(player)


def pop(who):
    if who not in player:
        print(f"{who} is not in the list")
    else:
        player.remove(who)
        print(f"{who} has been removed")


def divide():
    i = 0
    a = 0
    second = []
    first_team = []
    second_team = []
    for abc in player:
        second.append(abc)

    while i < len(second):
        random.shuffle(second)
        if a % 2 == 0:
            first_team.append(second[-1])
            second.pop()
        else:
            second_team.append(second[-1])
            second.pop()
        a += 1
    print(f"First Team: {first_team}")
    print(f"Second Team: {second_team}")


if __name__ == '__main__':
    main()
