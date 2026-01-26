#if-elif-else chain is useful when you just need one test to pass
#if we need to check all conditions of interest, we use a series of if statements instead
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!\n')

#simple for loop
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    print(f'Adding {topping}.')

print('\nFinished making your pizza!\n')

#what if we run out of green peppers?
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print('Sorry, we are out of green peppers at this time.')
    else:
        print(f'Adding {topping}.')

print('Finished making your pizza!\n')

#if we want to check for an empty list, we must do it before the loop (if the list is empty, it doesn't
#have anything to loop through
requested_toppings = []

if requested_toppings:
    # This block only runs if the list is NOT empty
    for topping in requested_toppings:
        if topping == 'green peppers':
            print('Sorry, we are out of green peppers at this time.')
        else:
            print(f'Adding {topping}.')
else:
    # This block runs if the list IS empty
    print('Are you sure you want a plain pizza?\n')

#using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f'Adding {topping}.')
    else:
        print(f"Sorry, we don't have {topping}.")

print('Finished making your pizza!\n')