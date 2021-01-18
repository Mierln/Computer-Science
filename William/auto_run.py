import Sherlock_Holmes

container = [["In The Deep Blue Ocean","The Stranger","Polly wants a cracker"],                     
             ["The Secret of Monkey Island"],                                                       
             ["A Good Leader is A Good Servant","The Quest of Rosetta","Le Chuck’s Revenge"],
             ["The Bloody Hell Mary","The Lost Necklace", "The Magical Season of Christmas"],
             ["Sherlock Holmes", "Graduation Day"]]


print("\n" *3)
Sherlock_Holmes.show_containers(container)

print("\nMOVES")
print(f"move 5 to 2")
print(f"move 5 to 2")
print(f"move 4 to 5")
print(f"move 4 to 5")
print(f"move 4 to 5")

print(f"move 2 to 4")
print(f"move 5 to 4")
print(f"move 5 to 4")
print(f"move 1 to 5")
print(f"move 2 to 5")

print(f"move 1 to 2")
print(f"move 1 to 2")
print(f"move 4 to 1")
print(f"move 2 to 1")

run = input("Press return/enter to run: ")
if run == "":
    Sherlock_Holmes.mover(container,5,2)
    Sherlock_Holmes.mover(container,5,2)
    Sherlock_Holmes.mover(container,4,5)
    Sherlock_Holmes.mover(container,4,5)
    Sherlock_Holmes.mover(container,4,5)

    Sherlock_Holmes.mover(container,2,4)
    Sherlock_Holmes.mover(container,5,4)
    Sherlock_Holmes.mover(container,5,4)
    Sherlock_Holmes.mover(container,1,5)
    Sherlock_Holmes.mover(container,2,5)

    Sherlock_Holmes.mover(container,1,2)
    Sherlock_Holmes.mover(container,1,2)
    Sherlock_Holmes.mover(container,4,1)
    Sherlock_Holmes.mover(container,2,1)

print("\n\nResult\n")
Sherlock_Holmes.show_containers(container)
