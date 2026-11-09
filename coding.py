print("Welcome to the Escape room. Let's get started")

print("You wake up in a gray room, dimly lit yellow lights barely give the room light.\nThere is a box, puzzle, computer, door")

things_to_do = ["box", "puzzle", "computer", "door"]

print()

answer = input("Where would you like to go? ")
answer.lower()

if answer == "box":
    print("You walk up to the box, it is locked and a ")
