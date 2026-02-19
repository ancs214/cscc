"""
FILE_NAME: lists-homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-17-2026
PURPOSE: Create a function that takes a list of animals as input and outputs a dictionary with counts of each
kind of animal from the list, then use methods to access specific elements.
"""

# def create_dictionary(animals):
#     """takes list of animals and creates an indexed dictionary with count of each animal"""

dictionary = {}
animals = ['lion', 'lion', 'boa', 'spider', 'spider']
index = 0

for index, animal in enumerate(animals):
    print('List contains', animal, 'at index', index)

