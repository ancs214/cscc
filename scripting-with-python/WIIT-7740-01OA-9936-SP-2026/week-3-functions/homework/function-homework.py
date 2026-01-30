
import random
import sys

#function that returns a random number between 1 and 6
def random_number():
    #randrange() Returns a random number between 1 and 6 (start is inclusive, stop is exclusive)
    #randint() Returns a random number between 1 and 6 (start AND end are inclusive)
    result = int(random.randint(1,6))
    return result

def guess_function(guess, result=4):
    """Function that compares two arguments
    (the user's guess vs actual result of the die roll)."""
    #error logic or "guard clause"
    if guess < 1 or guess > 6:
        print('Error! Guess must be a number between 1 and 6.')
        sys.exit()
    elif not isinstance(guess, int):
        print('Error! Guess must be a number between 1 and 6.')
        sys.exit()

    #gameplay logic
    if guess == result:
        print('matched')
        sys.exit()
    else:
        print('did not match')

#create variables for user guess and random number between 1 and 6
my_guess = 6
die_throw = random_number()
print(die_throw)

#pass variables into our guess_function as arguments
my_result = guess_function(my_guess, die_throw)
print(f'I guessed {my_guess} and the die toss {my_result}.')

# die_roll = random_number()
#
# while True:
#     print('Guess the number between 1 and 6.')
#     user_guess = (input())
#
#     guess_function(user_guess, die_roll)









