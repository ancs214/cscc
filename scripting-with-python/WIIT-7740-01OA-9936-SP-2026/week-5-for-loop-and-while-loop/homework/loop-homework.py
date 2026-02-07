"""
FILE_NAME: loop-homework.py
AUTHOR: Ashley-Noel Swarn
DATE:
PURPOSE: Create a program to allow input of individual item prices until the user chooses to stop.
The program will add item prices to a list, then calculate sales tax and total bill amount.
"""

import sys

# start with empty list
price_list = []
# initial greeting
print("Welcome to your own personal sales tax and bill calculator! Enter 'q' to end the program.")

while True:
    # prompt user to enter item price and save to user_input variable
    user_input = input("Please enter an item price: ")

    if user_input == 'q':
        break
    try:
        # try to add user_input value to item_list
        price_list.append(float(user_input))
    # if it results in ValueError, print error message
    except ValueError:
        print("ERROR! \nEnter a number this time.")
    else:
        print(f"${price_list[-1]} added.")
        print("Current price list: ", price_list)

print("Here is your list of individual prices: ", price_list)

def calculate_tax(original_prices):
    for price in original_prices:


calculate_tax(price_list)





