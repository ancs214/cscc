

magicians = ['alice', 'david', 'carolina']
#this line tells python to retrieve the first value from the list and associate with the variable 'magician'
#then print the value
#the for loop will repeat for each element in the list
for magician in magicians:
    print(magician)

#we can use range() in the for loop to perform that function on a range of numbers
for value in range(1,21):
    print(value)

#using the third parameter to make a list of odd numbers
odd_nums = range(1,21,2)
for value in odd_nums:
    print(value)

#using list comprehension (see lists.py file), create a list of the first 10 cubes
numbers_list = range(1,11)
cubes = [value**3 for value in numbers_list]
for value in cubes:
    print(value)

#looping through a sliced list using the cubes list we just created
print(cubes)
for value in cubes[:3]:
    print(value)

