import random
import time

door_key = random.randint(1,3)
if door_key == 1:
    key_answer = "green"
elif door_key == 2:
    key_answer = "blue"
else:
    key_answer = "red"

print("Welcome to the Escape room. Let's get started\n")

print("You wake up in a gray room, dimly lit yellow lights barely give the room light.\nThere is a box, puzzle, computer, and door")

box = 0
puzzle = 1
computer = 1
door = 0
escape = 0

print()

answer = input("Where would you like to go? ")
answer.lower()

guess = "0"

keys_box = ["green", "blue", "red"]
length = len(keys_box)
keys_invetory = []

while escape != 1:
        if answer == "puzzle":
            while guess != "2,4":
                    print("\n\nYou make your way over to a puzzle box. It is sitting on a table with a piece of paper on it that says, the box knows what you write on this paper.\nYou think to yourself, maybe I write my answer on here.\n\nThe puzzle on the top of the box states:\nsquare + circle = 6\ntriangle - circle = 2\n3 + square = triangle -1\n")
                    guess = input("Please input it in this order: square,circle. If square was 5 and circle was 7 it would be 5,7   If you wish to quit this riddle please input 'quit' ")
                    if guess == "2,4" or guess == "quit":
                        if guess == "2,4":
                                pass
                        else:
                            answer = input("Where would you like to go? ")
                            answer.lower()
                            break
                    else:
                        print("Try again!")
                        time.sleep(2)
        if answer == "box":
            print("\n\nYou walk up to the box, it is locked and a 3-digit code is needed to unlock it.")
            if box == 1:
                code = input("Please input code: ")
                if code == "327":
                    print(f"\nThe box unlocks, revealing {length} different keys; {keys_box}")
                    key_choice = input(f"Pick a key; enter one of the following {keys_box}: ")
                    key_choice = key_choice.lower()
                    if key_choice == "green":
                        keys_invetory.append("green")
                        keys_box.remove("green")
                    elif key_choice == "blue":
                        keys_invetory.append("blue")
                        keys_box.remove("blue")
                    else:
                        keys_invetory.append("red")
                        keys_box.remove("red")
                    print("\nThere is nothing you can do here")
                else:
                    print("Go somewhere else if you don't know it: ")
            else:
                print("\nThere is nothing you can do here")
        if answer == "door":
            print("\n\nYou walk up to the door, there is a key hole. The door needs a key to unlock.")
            if door == 1:
                for key in keys_invetory:
                    if key == key_answer:
                        print(f"The {key} key worked!")
                        escape += 1
                        break
                    else:
                        print("The key did not work, maybe try getting another key.")
                        print("\nThere is nothing you can do here")
            else:
                print("There is nothing you can do here")
        if escape != 1:
            answer = input("Where would you like to go? ") 
            answer.lower()
        else:
            break

print("\n\n!CONGRATULATIONS! You beat the escape room!")

                    
