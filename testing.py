import time

guess1 = ""

def puzzle(guess,answer,won,quit,try1,lost,string,riddle,puzzle):
    print(riddle)
    time.sleep(1)
    while guess != answer:
        guess = input(string)
        guess = guess.lower()
        if guess == answer or guess == "quit" or guess == puzzle:
            if guess == answer:
                print(won)
            elif guess == puzzle:
                print(riddle)
            else:
                print(quit)
                break
        else:
            print(lost)
            try1 += 1
    return guess

puzzle(guess1,".","won","quit",0,"lost","string,","riddle","puzzle")
print(guess1)
