"""
FILE_NAME: lists-homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-17-2026
PURPOSE: Create a function that takes a list of animals as input and outputs a dictionary with counts of each
kind of animal from the list, then use methods to access specific elements.
"""


def create_dict(l):
    """Function that takes a list as input and outputs a dictionary with counts of each unique animal"""
    animal_dict = {}
    for x in l:
        if x in animal_dict:
            animal_dict[x] += 1
        else:
            animal_dict[x] = 1
    return print(animal_dict)

animals = ['lion', 'lion', 'boa', 'spider', 'spider']
create_dict(animals)
