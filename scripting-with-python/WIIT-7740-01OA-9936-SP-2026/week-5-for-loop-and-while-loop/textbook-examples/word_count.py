"""
FILE_NAME: word_count.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-17-2026
PURPOSE: Demonstrate how to work with multiple files using pathlib
"""

from pathlib import Path

def count_words(path):
    """count the approximate number of words in a file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn't exist.")
    else:
        # count approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words.')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    # turns a string into a pathlib.Path object by passing it to the Path class:
    path = Path(filename)
    count_words(path)