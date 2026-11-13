import random
import time


def tries_print(list_try,list_challenge,len_list):
    for i  in range(len_list):
        a = list_try[i]
        b = list_challenge[i]
        print(f"It took you {a} tries to {b}")
    c = sum(list_try)
    print(f"\nIn total it took you {c} tries")
    d = list_try[-1]
    if d == 1:
        print("You got lucky getting the door in 1 try")
    elif d == 2:
        print("2 tries for the door, not bad")
    else:
        print("3rd times the charm, right? You must have bad luck.")

door_key = random.randint(1,3)
if door_key == 1:
    key_answer = "green"
elif door_key == 2:
   key_answer = "blue"
else:
   key_answer = "red"

tries_puzzle_math = 1
tries_puzzle_riddle = 1
tries_box = 1
tries_computer = 1
tries_door = 1

guess1 = ""
guess2 = ""

keys_box = ["green", "blue", "red"]
keys_inventory = []

box_math = 0
box_riddle = 0
puzzle = 0
box = 0
computer = 0
door = 0
escape = 0
something1 = False
something2 = True
tries = [tries_puzzle_math, tries_puzzle_riddle, tries_computer, tries_box, tries_door, ]
challenge = ["finish the puzzle box math challenge", "finish the puzzle box riddle challenge", "log onto the computer", "open the box", "open the door", ]
try_length = len(tries)

print("Welcome to the Escape room. Let's get started\n")


print("You wake up in a gray room, dimly lit yellow lights barely give the room light.\nThere is a box, puzzle, computer, and door")

answer = input("\nWhere would you like to go? ")
answer = answer.lower()

while escape != 1:
    if answer == "puzzle" and puzzle == 0:
        print("\n\nYou make your way over to a puzzle box. It is sitting on a table with a piece of paper on it that says, the box knows what you write on this paper.\nYou think to yourself, maybe I write my answer on here.")
        time.sleep(2)
        while guess1 != "2,4":
            print("\nThe puzzle on the top of the box states:\nsquare + circle = 6\ntriangle - circle = 2\n3 + square = triangle -1\n")
            guess1 = input("Please input square comma circle. Example; 5,7 (if you would like to quit type: quit) ")
            if guess1 == "quit" or guess1 == "2,4":
                if guess1 == "2,4":
                    print("\nThe box opens revealing another puzzle, this one contains a riddle.")
                    time.sleep(2)
                else: 
                    print("\nThe box shakes as you walk away.")
                    break
            else:
                print(f"\nYou write {guess1} on the piece of paper, the box does not respond.")
                tries_puzzle_math += 1
                time.sleep(1)
        while guess1 == "2,4":
            print("\nThe riddle is: In darkness, there will be light. In discomfort, there will be warmth. And yet, I can be your worst nightmare.")
            guess2 = input("What am I? (if you would like to quit type: quit) ")
            guess2 = guess2.lower()
            if guess2 == "quit" or guess2 == "fire":
                if guess2 == "fire":
                    print("\nYou write fire on the piece of paper, the box opens up again to reveal a check mark ingrained in the wood. The box closes. ")
                    time.sleep(2)
                    print("\nThere is nothing you can do here")
                    puzzle = 1
                    break
                else: 
                    print("\nThe box shakes as you walk away.")
                    break
            else:
                print(f"\nYou write {guess2} on the piece of paper, the box does not respond as {guess2} fades into the paper.")
                tries_puzzle_riddle += 1
                time.sleep(1)
    if puzzle == 1 and answer == "puzzle":
        print("The box shakes, '2,4' and 'fire' are written on the paper. There is nothing you can do here")

    if answer == "computer":
        pass
    if answer == "box":
        pass
    if answer == "door":
        pass
    if "escape" in answer:
        print("You won't get it if you ask for it!")
        time.sleep(2)
        

            

    answer = input("\n\n\nWhere would you like to go? ")
    answer = answer.lower()

won = tries_print(tries,challenge,try_length)
print(won)