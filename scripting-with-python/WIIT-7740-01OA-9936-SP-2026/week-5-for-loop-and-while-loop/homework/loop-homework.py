"""
FILE_NAME: loop-homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-11-2026
PURPOSE: Create a program to allow input of individual item prices until the user chooses to stop.
The program will add item prices to a list, then calculate sales tax and total bill amount.
"""

# start with empty list
price_list = []

# initial greeting
print("Welcome to your own personal sales tax and bill calculator! Enter 'q' to see final calculations.")

while True:
    # prompt user to enter item price and save input to user_input variable
    user_input = input("Please enter an item price: ")

    if user_input == 'q':
        break
    try:
        # try to add user_input value to item_list as a float integer
        price_list.append(float(user_input))
    # if it results in ValueError, print error message
    except ValueError:
        print("ERROR! \nEnter a valid number.")
    else:
        print(f"${price_list[-1]} added.")
        print("Current price list: ", price_list)

def calculate_tax(original_prices, tax_rate = 0.0575):
    """Function to calculate total sales tax and bill amount"""
    # initialize empty list
    sales_tax = []

    # for each element multiply by tax_rate and add each tax cost to empty list
    for price in original_prices:
        taxed_price = (price * tax_rate)
        sales_tax.append(taxed_price)

    # calculate total sales tax
    total_sales_tax = sum(sales_tax)
    print('Total Sales Tax: $', round(total_sales_tax, 2))

    # calculate total cost
    total_price = (sum(sales_tax) + sum(price_list))
    print('Total Bill Amount: $', round(total_price, 2))

# call function to calculate taxes and total cost
calculate_tax(price_list)





