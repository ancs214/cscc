#python allows a function to collect an arbitrary number of arguments
def make_pizza(*toppings):
    """Create a tuple containing list of toppings"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#now we can replace the print() with a loop that runs through the list of toppings
def create_pizza(*toppings):
    """Summarize pizza creation"""
    print('\nMaking a pizza with the following toppings:')

    for topping in toppings:
        print(f'-{topping}')

create_pizza('mushrooms', 'green peppers', 'extra cheese')
create_pizza('pepperoni', 'anchovies', 'mike"s hot honey')

#parameter with arbitrary # of arguments must be placed last
def make_more_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_more_pizza(16,'pepperoni')
make_more_pizza(12,'green peppers', 'extra cheese')

#the parameter with a default value must come before the arbitrary number of arguments
def make_yet_another_pizza(size, crust='thick', *toppings):
    print(f"\nMaking a {size}-inch pizza with {crust} crust.")
    print("Toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_yet_another_pizza(12, 'thin', 'mushrooms', 'peppers\n')

#for an arbitrary # of key:value pairs
def build_profile(first,last,**user_info):
    """Build a dictionary of user information"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert',
                             'einstein',
                             location='princeton',
                             field='physics')
print(f'New user information: {user_profile}')
