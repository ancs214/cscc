import sys

num = 25
is_valid = False

while not is_valid:
    user_input = int(input('Please enter a number from 1 to 25: '))
    # validation logic
    if user_input < 1 or user_input > 25:
        print('Numbers are not between 1 and 25.')
    elif user_input == 15:
        # sys.exit() will end entire program
        # break will exit only the while loop and go on to the next function in the program
        break
print('Out of the loop!')