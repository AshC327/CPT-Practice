import random

print("Welcome to the Escape room. Let's get started")

print("You wake up in a gray room, dimly lit yellow lights barely give the room light.\nThere is a box, puzzle, computer, and door")

box = 1
puzzle = 0
computer = 0
door = 0

print()

answer = input("Where would you like to go? ")
answer.lower()

keys_invetory = []

while answer != "n":
    if answer == "box":
        print("You walk up to the box, it is locked and a 3-digit code is needed to unlock it.")
        if box == 1:
            code = input("Please input code: ")
            if code == "327":
                print("\nThe box unlocks, revealing three different keys; a blue key, a red key, and a green key")
                key_choice = input("Pick a key; enter either green, blue, or red: ")
                key_choice = key_choice.lower()
                if key_choice == "green":
                    keys_invetory.append("green")
                elif key_choice == "blue":
                    keys_invetory.append("blue")
                else:
                    keys_invetory.append("red")
            else:
                answer = input("Go somewhere else if you don't know it: ")
        else:
            answer = input("\nThere is nothing you can do here, where would you like to go? ")

