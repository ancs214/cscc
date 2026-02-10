"""
FILE_NAME: loop-homework.py
AUTHOR: Ashley-Noel Swarn
DATE:
PURPOSE: Create a program to allow input of individual item prices until the user chooses to stop.
The program will add item prices to a list, then calculate sales tax and total bill amount.
"""


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
        print("ERROR! \nEnter a valid number this time.")
    else:
        print(f"${price_list[-1]} added.")
        print("Current price list: ", price_list)

def calculate_tax(original_prices, tax_rate = 0.0575):
    tax_costs = []

    # for each element multiply by 0.0575 and add each tax cost to empty list
    for price in original_prices:
        taxed_price = round((price * tax_rate), 2)
        tax_costs.append(taxed_price)
        tax_costs_sum = sum(tax_costs)

    # using * (the unpacking operator) unpacks the list element to print without brackets
    print('$', *tax_costs_sum)

    # add sum of taxes and prices together to calculate total cost
    total_price = round((sum(tax_costs) + sum(price_list)), 2)
    print('$', total_price)

# call function to calculate taxes and total cost
calculate_tax(price_list)





