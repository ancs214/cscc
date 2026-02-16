# create list of numbers
items = [2,4,6,0,1,3,5,7,9]
# create a "pointer" or "counter" variable
item_index = 0

# as long as our counter is less than the length of our list (9), keep going
while item_index < len(items):
    # grabs element that our counter is pointing to
    item = items[item_index]
    # prints that element
    print('List contains: ', item)
    # add one to our counter variable
    item_index += 1

