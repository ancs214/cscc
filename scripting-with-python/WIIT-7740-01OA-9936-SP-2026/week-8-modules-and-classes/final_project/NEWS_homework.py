"""
FILE_NAME: NEWS_homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 03-08-2026
PURPOSE: Create a program that will accept a text document and counts the number
of times each word appears, search and replace a specific word, and save a new
version locally.
"""

from pathlib import Path

def count_words(path, ignore_words, search_word, top_num):
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

    proportion = {}
    for key in counts:
        # calculate proportion of word use:
        # using 'counts[key]' to look up each key's value, divide by total num of words
        word_proportion = round((counts[key] / num_words), 4)
        # add key/value pair to proportion{}
        proportion[key] = word_proportion

    if search_word in proportion:
        # find how many times word is repeated in counts dictionary
        word_repeats = counts[search_word]
        # calculate percentage of proportion for readability
        percentage = (proportion[search_word] * 100)
        percentage_rounded = round(percentage, 4)
        print('--- PROPORTION OF SEARCHED WORD ---')
        print(f'The word "{search_word}" appears in the text {word_repeats} times with a proportion of {proportion[search_word]} or {percentage_rounded}%.\n')
    else:
        print(f'The word "{search_word}" does not exist in the text.')

    # sort counts dictionary and convert to list of pairs (each item is a tuple)
    # (key=lambda tells python to look at the value as a number for sorting)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # get top n number of words
    top_words_list = sorted_counts[:top_num]

    print(f"--- Top {top_num} Most Frequent Words ---")
    for item, count in top_words_list:
        top_word = item
        top_word_count = count
        top_word_proportion = round((top_word_count / num_words), 4)
        top_word_percentage = top_word_proportion * 100
        top_word_percentage_rounded = round(top_word_percentage, 4)
        print(f'Word: {top_word}\nAbsolute Count: {top_word_count}\nProportion: {top_word_proportion} or {top_word_percentage_rounded}%\n')

    return num_words, counts, proportion, word_proportion, word_repeats, percentage

filename = 'dracula.txt'
ignore = ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to"]
search_for_word = "dear"
top_n_words = 3
# turns text string into a pathlib.Path object to pass to function:
file_path = Path(filename)
count_words(file_path, ignore, search_for_word, top_n_words)

