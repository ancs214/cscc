#Create a function to put the guessing game into so we can call it with arguments (doomed_guess and secret)

import random
import sys


def guess_output(doomed_guess, secret):
    if doomed_guess < secret:
        print(
            "Your guess is too low and the Xenomorph queen have allowed the facehuggers to have a play date with you.")
    elif doomed_guess > secret:
        print(
            "Your guess is too high and you're in a battle with a Xenomorph soldier.")
    else:
        print("Victory is yours!! You have defeated the Xenomorphs...for now.")
        sys.exit()

secret_number = random.randint(1, 20)
print("Mother is thinking of a number between 1 and 20.")

while True:
    print("Please guess the number that Mother is thinking of or the Xenomorphs will get you.")
    print("Take a guess.")
    guess = int(input())

    guess_output(guess, secret_number)



