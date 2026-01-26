#sort method organizes alphabetically (permanent change)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#reverse alphabetically
cars.sort(reverse=True)
print(cars, '\n')

#temporarily sort a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('Here is the original list again:')
print(cars, '\n')

#print a list in reverse order
print(cars)
cars.reverse()
print(cars, '\n')

#find the length of a list
#python starts counting the length of a list at 1 instead of 0
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))




