"""
FILE_NAME: NEWS_homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 03-08-2026
PURPOSE: Create a program that will accept a text document and counts the number
of times each word appears, search and replace a specific word, and save a new
version locally.
"""

from pathlib import Path

def count_words(path, ignore_words, search_word):
    """
    Function that accepts a document and provides the following capabilities:
    Calculates total number of words, how many times each word appears and word's proportion,
    Searches for a specific word and allows user to replace with something else,
    Save modified document to a new file
    """
    # initialize variables to 0 in case search_for_word fails
    word_repeats = 0
    percentage = 0.0
    word_proportion = 0.0

    # read text
    contents = path.read_text(encoding='utf-8').lower()

    # replace every punctuation mark in contents with a space
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”‘’'
    for char in punctuation:
        contents = contents.replace(char, " ")
    # split words now that our text is cleaned up
    words = contents.split()

    # find length of words list and display total number of words
    num_words = len(words)
    print(f'The file {path} contains a total of {num_words} words.')

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

    proportion = {}
    for key in counts:
        # calculate proportion of word use:
        # using 'counts[key]' to look up each key's value, divide by total num of words
        word_proportion = round((counts[key] / num_words), 4)
        # add entry to dictionary using word_proportion for values
        proportion[key] = word_proportion

    if search_word in proportion:
        # find how many times word is repeated in counts dictionary
        word_repeats = counts[search_word]
        # calculate percentage of proportion for readability
        percentage = (proportion[search_word] * 100)
        percentage_rounded = round(percentage, 4)
        print(f'The word "{search_word}" appears in the text {word_repeats} times. \nProportion: {proportion[search_word]} or {percentage_rounded}%.')
    else:
        print(f'The word "{search_word}" does not exist in the text.')

    return num_words, counts, proportion, word_proportion, word_repeats, percentage

filename = 'dracula.txt'
ignore = ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to"]
search_for_word = "i"
# turns text string into a pathlib.Path object to pass to function:
file_path = Path(filename)
count_words(file_path, ignore, search_for_word)

