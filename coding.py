import random
import time


def tries(challenge,try1):
    return(f"It took you {try1} tries to complete {challenge}")

def puzzle(guess,answer,won,quit,try1,lost,string,riddle,puzzle,math):
    print(riddle)
    time.sleep(1)
    while guess != answer:
        guess = input(string)
        guess = guess.lower()
        if guess == answer or guess == "quit" or guess == puzzle:
            if guess == answer:
                print(won)
                math += 1
            elif guess == puzzle:
                print(riddle)
            else:
                print(quit)
                break
        else:
            print(lost)
            try1 += 1

door_key = random.randint(1,3)
if door_key == 1:
    key_answer = "green"
elif door_key == 2:
   key_answer = "blue"
else:
   key_answer = "red"

tries_puzzle_math = 1
tries_puzzle_riddle = 1
tries_door = 1
guess1 = ""
guess2 = ""
keys_box = ["green", "blue", "red"]
keys_inventory = []
box_math = 0
box_riddle = 0
escape = 0


print("Welcome to the Escape room. Let's get started\n")


print("You wake up in a gray room, dimly lit yellow lights barely give the room light.\nThere is a box, puzzle, computer, and door")

answer = input("\nWhere would you like to go? ")
answer = answer.lower()

while escape != 1:
    if answer == "puzzle":
        print("\n\nYou make your way over to a puzzle box. It is sitting on a table with a piece of paper on it that says, the box knows what you write on this paper.\nYou think to yourself, maybe I write my answer on here.")
        if guess1 != "2,4":
            puzzle(guess1,"2,4","Congratulations","Puzzle quit",tries_puzzle_math,"\nTry again", "Please input square comma circle. example 5,7 (if you like the riddle to repeat type: riddle   if you would like to quit type: quit) ", "\nsquare + circle = 6\ntriangle - circle = 2\n3 + square = triangle -1\n", "riddle", box_math)
        else:
            print("The box opens revealing another puzzle, this one contains a riddle.")
            puzzle(guess2, "fire", "Congratulations", "Puzzle Quit", tries_puzzle_riddle, "\nTry Again", "What am I? ", "The riddle is: In darkness, there will be light. In discomfort, there will be warmth. And yet, I can be your worst nightmare.", "riddle", box_riddle)
    answer = input("\nWhere would you like to go? ")
    answer = answer.lower()

