#This line sets the value of car to 'bmw'
car = 'bmw'
print(car)
#This line checks whether the value of car is 'bmw' with the double equal sign
print(car == 'bmw')
#When the value is anything but 'bmw', this test returns false:
print(car == 'ducati', '\n')

#testing for equality is case sensitive
car = 'Audi'
print(car)
print(car == 'audi', '\n')
#if case doesn't matter, you can convert to lowercase temporarily before testing
print(car.lower() == 'audi')
print(car.lower() == 'Audi', '\n')

#testing inequalities
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print('Hold the anchovies!\n')

#check if a value is already in a list, use keyword "in"
toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in toppings)
print('pepperoni' in toppings, '\n')

#check if value is not in a list
banned_users = ['andrew', 'caroline', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    