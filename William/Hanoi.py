#The Tower Of Hanoi
global towers
donut1 = ("*")
donut2 = ("**")
donut3 = ("***")
donut4 = ("****")
towers = [[donut4, donut3, donut2, donut1],
        [], 
        []]

def show_tower():
    
    print("\nTowers \n")
    print(f"Tower 1 : {towers[0][::-1]}")
    print(f"Tower 2 : {towers[1][::-1]}")
    print(f"Tower 3 : {towers[2][::-1]}")
    print("\nObjective: \n"
          "Move all rings to Tower 3 but you can't stack bigger rings on top of smaller rings\n")

def move(origin, destination):
    if check(origin, destination):
        item = origin.pop()
        destination.append(item)
        return(f"\n{item} has been")
    else: return(f"\nCan't stack on smaller rings")
    

def complete(towers):
    if len(towers[2]) > 0:
        if len(towers[2]) == 4:
            return True
        else: return False
    
def check(origin, destination):
    if len(destination) > 0 :
        if len(destination[-1]) > len(origin[-1]):
            return True
        else:
            return False
    return True
    
def main():
    while True:

        show_tower()

        o_in = int(input("Origin tower: "))
        d_in = int(input("Destination tower: "))
        if len(towers[o_in - 1]) == 0:
            print(f"Tower {o_in} is Empty")

        else:
            print(move(towers[o_in - 1], towers[d_in - 1]))

        if complete(towers):
            show_tower()
            print("YOU WIN")
            break

if __name__ == "__main__":
    main()
         
