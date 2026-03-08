"""
FILE_NAME: NEWS_homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 03-08-2026
PURPOSE: Create a program that will accept a text document and counts the number
of times each word appears, search and replace a specific word, and save a new
version locally.
"""

from pathlib import Path

def count_words(path):
    """

    """
    contents = path.read_text(encoding='utf-8')
    # split into list of words and count number of words in the file
    words = contents.split()
    num_words = len(words)

    print(f'The file {path} contains a total of {num_words} words.')

    counts = {}
    for word in words:
        if word in counts:
            # if word is already a key, increase value by 1
            counts[word] += 1
        else:
            # if word is new, create key and set to 1
            counts[word] = 1

    print(counts)
    return counts

filename = 'dracula.txt'
# turns text string into a pathlib.Path object:
file_path = Path(filename)
count_words(file_path)

