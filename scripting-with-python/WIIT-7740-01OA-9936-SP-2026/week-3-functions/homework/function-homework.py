
import random
import sys

#create function that returns a random number between 1 and 6
def random_number():
    #randrange() Returns a random number between 1 and 6 (start is inclusive, stop is exclusive)
    #randint() Returns a random number between 1 and 6 (start AND end are inclusive)
    result = int(random.randint(1,6))
    return result

def guess_function(guess, result=4):
    """Function to compare the user's guess and actual result of the die roll."""
    if guess < 1 or guess > 6:
        print('Error! Guess must be a number between 1 and 6.')
        sys.exit()
    elif guess != int(guess):
        print('Error! Guess must be a number between 1 and 6.')
        sys.exit()

    if guess == result:
        print('matched')
        sys.exit()
    else:
        print('did not match')

die_roll = random_number()

while True:
    print('Guess the number between 1 and 6.')
    user_guess = int(input())

    guess_function(user_guess, die_roll)









