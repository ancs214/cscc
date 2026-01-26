import random
import sys

secret_number = random.randint(1,20)
print("MOTHER is thinking of a number between 1 and 20.")

while True:
    print("Please guess the number that MOTHER is thinking of or the Xenomorphs will get you.")
    print("Take a guess.")
    #for the input function python interprets everything as a string, so we change the result to integer
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low and the Xenomorph queen has allowed the facehuggers to have a play date with you.")
    elif guess > secret_number:
        print("Your guess is too high and you're in a battle with a Xenomorph soldier.")
    else:
        print("Victory is yours!! You have defeated the Xenomorphs...for now.")
        sys.exit()
