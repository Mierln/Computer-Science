hanoi = [["*******", "*****", "***", "*"], [], []]
"""(1,2) (1,3) (2,3) (1,2) (3,1) (3,2) (1,2) (1,3) (2,3) (2,1) (3,1) (2,3) (1,2) (1,3) (2,3)"""


def container():
    print("\n")
    print(f"First Tower: {hanoi[0]}")
    print(f"Second Tower: {hanoi[1]}")
    print(f"Third Tower: {hanoi[2]}")


def game():
    while True:
        container()
        origin = int(input("\n Select a tower to move the donut (Number): "))
        if len(hanoi[origin - 1]) == 0:
            print("ERROR: That Tower is Empty")
            game()

        destination = int(input(" Select a tower to be moved to (Number): "))
        if len(hanoi[destination - 1]) >= 1:
            if len(hanoi[origin - 1][-1]) > len(hanoi[destination - 1][-1]):
                print("ERROR: The Bigger Discs Cannot Be On Top of a Smaller One!")
                game()

        if origin == destination:
            print(f"You Can't Move Tower {origin} to Tower {destination}")
            game()

        move(origin, destination)


def move(origin, destination):
    hanoi[destination - 1].append(hanoi[origin - 1][-1])
    hanoi[origin - 1].pop()


if __name__ == '__main__':
    print("\nTower of Hanoi")
    game()