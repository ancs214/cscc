"""
FILE_NAME: lists-tuples-homework
AUTHOR: Ashley-Noel Swarn
DATE: 01312026
PURPOSE: Create a single function that allows the user to add or remove an item to/from a list
    The function will accept three arguments: a list, an item, and a boolean (remove=True or False)
    The function will return the list as a tuple containing two items: the list sorted alphabetically
    and the length of the new list as an integer.
"""

def list_addend(existing_list, item, remove=False):
    """Takes a list as an argument as well as an item that can be added to it.
    Sort the new list in ascending order and return as tuple containing new list and length."""
    if item in existing_list and remove:
        existing_list.remove(item)
        existing_list.sort()

    elif item in existing_list and remove==False:
        existing_list.sort()

    else:
        existing_list.append(item)
        existing_list.sort()

    # adding a comma at the end will return a tuple instead of a list
    return existing_list, len(existing_list)


names = ['sam', 'harry', 'charlie', 'riley']

#we have the option to unpack the tuple into two separate variables
new_list, item_count = list_addend(names, 'ashley')
print('My new list is {} and has {} elements.'
    .format(new_list, item_count))

new_list, item_count = list_addend(names, 'sam', remove=True)
print('My new list is {} and has {} elements.'
    .format(new_list, item_count))

new_list, item_count = list_addend(names, 'charlie')
print('My new list is {} and has {} elements.'
    .format(new_list, item_count))



