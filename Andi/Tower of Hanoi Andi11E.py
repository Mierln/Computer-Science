ring1 = "1#"
ring2 = "2##"
ring3 = "3###"
ring4 = "4####"


Towers = [[ring4, ring3, ring2, ring1],[],[]]

counter = 0

def ViewTower():
    print("\n")
    print("Tower 1 = ", Towers[0][::-1])
    print("Tower 2 = ", Towers[1][::-1])
    print("Tower 3 = ", Towers[2][::-1])
    print("\n")

def Shift(take, place):
    Towers[place - 1].append(Towers[take - 1][-1])
    Towers[take - 1].pop()

def Fm(take, place):
    if len(Towers[place - 1]) > 0:
        if len(Towers[take - 1][-1]) > len(Towers[place - 1][-1]):
            print("***ERROR: You can't do that")
            return True
        return False
    return False

def WinState():
    if len(Towers[2]) == 4:
        print("You WON with " + str(counter) + " moves")
        if counter == 15:
            print("Congratulations, you finished the tower within the minimum moves")
        return exit(-1)

def game():
    global counter
    g = True
    while g:
        print("(1,2) (1,3) (2,3) (1,3) (1,2) (3,1) (3,2) (1,2) (1,3) (2,3) (2,1) (3,1) (2,3) (1,2) (1,3) (2,3)")
        print("Objectives: Move all 4 rings into the 3rd square bracket")
        print("Rules: You cannot place bigger rings on top of smaller rings")
        ViewTower()
        take = int(input("Take a ring out of tower (1~3): "))
        place = int(input("Insert ring to tower (1~3): "))
        if Fm(take,place) == False:
            Shift(take,place)
        WinState()
        counter = counter + 1

game()