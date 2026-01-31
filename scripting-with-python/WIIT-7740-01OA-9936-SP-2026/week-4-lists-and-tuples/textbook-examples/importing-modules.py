"""
PURPOSE: explain different ways to import modules. please note, if imported files have
executable code (like a standalone print function), they will also execute if the entire
module was imported.
"""

#because we used hyphens in our python file title, we must use python's import library
import importlib
# This loads the module despite the hyphens
arb_args = importlib.import_module("arbitrary-number-of-arguments")
# Now you can use it via the 'ana' variable
user1 = arb_args.build_profile(
    'ashley-noel',
    'swarn',
    age=38,
    hobbies='moping',
    location='columbus',
    field='nursing'
)
print(user1)

#if we did not use hyphens we can import this way
import passing_lists_to_functions as greeting
usernames = ['ashley-noel', 'erica', 'hannah', 'ty']
greeting.greet_users(usernames)

#we can import specific functions
from passing_lists_to_functions import greet_users
usernames = ['dorian', 'sally', 'aster', 'ron']
greet_users(usernames)


import lists
#there are no functions in list.py file.
#we imported a list, so do not need parentheses after million_numbers
print(lists.million_numbers[0])
print(lists.million_numbers[0])
print(lists.million_numbers[0])
print(lists.million_numbers[0])

