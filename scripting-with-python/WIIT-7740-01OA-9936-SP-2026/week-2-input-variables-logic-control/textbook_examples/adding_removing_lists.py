from logging import lastResort
from os import remove

#using individual values from a list
#title method capitalizes the first letter
#"backslash n" = new line (used within a string)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[3].title()} touring bike.\n"
print(message)

#append method adds an element to the end of a list
car_makes = ['subaru', 'porsche', 'hyundai']
print(car_makes)
car_makes.append('jeep')
print(car_makes, '\n')

#insert method too add element to any position in the list
car_makes.insert(0, 'nissan')
print(car_makes, '\n')

#using remove method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\n A {too_expensive.title()} is too expensive for me.\n')

#use delete statement if you know the element's index
print(motorcycles)
del motorcycles[1]
print(motorcycles, '\n')

#pop method removes last item by default, but lets you work with that item after removing
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle, '\n')
print(f'The last motorcycle I owned was a {popped_motorcycle.title()}.\n')
#to use pop to remove from any position, include the index in parentheses
motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)
first_owned_motorcycle = motorcycles.pop(0)
print(f'My very first motorcycle was a {first_owned_motorcycle.title()}.', '\n')

#remove method - don't know index, but know the value
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles, '\n')
