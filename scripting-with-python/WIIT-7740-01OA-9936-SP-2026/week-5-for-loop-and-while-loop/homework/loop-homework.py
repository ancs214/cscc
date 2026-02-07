"""
FILE_NAME: loop-homework.py
AUTHOR: Ashley-Noel Swarn
DATE:
PURPOSE: Create a program to allow input of individual item prices until the user chooses to stop.
The program will add item prices to a list, then calculate sales tax and total bill amount.
"""

import sys

# start with empty list
item_list = []
# initial greeting
print("Welcome to your own personal sales tax and bill calculator! Enter 'q' to end the program.")

while True:
    # prompt user to enter item price and save to user_input variable
    user_input = input("Please enter an item price.")

    if user_input == 'q':
        sys.exit()
    else:
        # add user_input value to item_list
        item_list.append(float(user_input))
        print(f"${item_list[-1]} added.")
        print("Current price list: ", item_list)



