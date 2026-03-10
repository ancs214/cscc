"""
FILE_NAME: NEWS_homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 03-08-2026
PURPOSE: Create a program that will accept a text document and counts the number
of times each word appears, search and replace a specific word, and save a new
version locally.
"""

from pathlib import Path

def clean_text(path):
    # read text
    contents = path.read_text(encoding='utf-8').lower()

    # replace every punctuation mark in contents with a space
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”‘’'
    for char in punctuation:
        contents = contents.replace(char, " ")
    # split words now that our text is cleaned up
    return contents.split()

def count_words(words, path, ignore_words):
    # find length of words list and display total number of words
    num_words = len(words)
    print('--- TOTAL WORDS ---')
    print(f'The file {path} contains a total of {num_words} words.\n')

    counts = {}
    for word in words:
        # ignore designated words input by user
        if word in ignore_words:
            # skip the rest of the loop and move to next item
            continue

        if word in counts:
            # if word is already a key, increase value in key/value pair by 1
            counts[word] += 1
        else:
            # if word is new, create key and set value to 1
            counts[word] = 1

        return counts

filename = 'dracula.txt'
ignore = ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to"]
search_for_word = "dear"
top_n_words = 3
# turns text string into a pathlib.Path object to pass to function:
file_path = Path(filename)

text = clean_text(file_path)
total_words = count_words(text,file_path, ignore)

