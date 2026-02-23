"""
FILE_NAME: lists-homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-22-2026
PURPOSE: Create a function that takes a list of animals as input and outputs a dictionary with counts of each
kind of animal from the list, then use methods to access specific elements.
"""

def create_dict(animals):
    """Function that takes a list as input and outputs a dictionary with counts of each unique animal"""
    try:
        animal_dict = {}
        for animal in animals:
            # if animal is already in dict, add one to it's corresponding value
            if animal in animal_dict:
                animal_dict[animal] += 1
            # else create a key/value pair: key = animal, value = 1
            else:
                animal_dict[animal] = 1
        # print(animal_dict)
        return animal_dict

    except TypeError:
        print('Oops! Enter a list into the function.')


animal_list = ['lion', 'lion', 'boa', 'spider', 'spider']
create_dict(animal_list)



random_animals_list = [
    'lion', 'tiger', 'lion', 'bear', 'wolf', 'tiger', 'snake', 'lion', 'spider', 'bear',
    'wolf', 'wolf', 'lion', 'spider', 'snake', 'panda', 'koala', 'panda', 'otter', 'koala',
    'panda', 'falcon', 'otter', 'falcon', 'koala', 'panda', 'panda', 'otter', 'koala', 'falcon',
    'otter', 'koala', 'panda', 'falcon', 'otter'
]

# pass list to the function and assign to a variable
random_animals_dict = create_dict(random_animals_list)

# create a list from dictionary and select the third element
element_3 = (list(random_animals_dict)[2])

# display corresponding value to see how many of that animal need to be fed
count = random_animals_dict.get(element_3)

print(f'My zoo needs enough food for {count} {element_3}(s).')



