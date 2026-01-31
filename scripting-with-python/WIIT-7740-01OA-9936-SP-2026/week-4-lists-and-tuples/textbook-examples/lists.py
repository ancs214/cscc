
#to make a list of numbers, we can use the list() and range() function together
million_numbers = list(range(1,1_000_001))
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

#list comprehensions combine a for loop and the creation of new elements into one line
#and automatically appends each new element
squares = [value*2 for value in range(1,21)]
print(squares)

#slicing a list
players = ['charles', 'martina', 'michael', 'goldfish', 'sam', 'ashley', 'erica', 'tobe', 'theo']
#print 0 through 2 elements
print(players[0:3])
#print last 3 items
print(players[-3:])
#print last 3 items in reverse order
print(players[:-4:-1])

#copying a list to a new list
#we CANNOT just say my_foods = friends_foods or both variables will point to the same list
my_foods = ['pizza', 'chicken adobo', 'ice cream', 'ox tail', 'rice']
friends_foods = my_foods[:]
print('\nmy favorite foods are:')
print(my_foods)
print('\nmy friend"s favorite foods are:')
print(friends_foods)


