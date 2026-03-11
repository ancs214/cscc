"""
FILE_NAME: NEWS_homework.py
AUTHOR: Ashley-Noel Swarn
DATE: 03-08-2026
PURPOSE: Create a program that will accept a text document and counts the number
of times each word appears, search and replace a specific word, and save a new
version locally.
"""

from pathlib import Path


#-------------------------------
#------CLEAN TEXT FUNCTION------
#-------------------------------
def clean_text(path):
    # read text
    contents = path.read_text(encoding='utf-8').lower()

    # replace every punctuation mark in contents with a space
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”‘’'
    for char in punctuation:
        contents = contents.replace(char, " ")
    # split words now that our text is cleaned up
    words = contents.split()
    return words

#-----------------------------------------
#------COUNT AND PROPORTION FUNCTION------
#-----------------------------------------
def count_proportion_func(words, ignore_words):
    # total number of words
    num_words = len(words)

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

    proportions = {}
    for word in counts:
        # look up each key's value, divide by total num of words
        word_proportion = round((counts[word] / num_words), 4)
        # add key/value pair to proportion{}
        proportions[word] = word_proportion

    return counts, proportions

#------------------------------
#------TOP WORDS FUNCTION------
#------------------------------
def top_words(top_num, count_dict, total_word_list):
    # total count of words
    total_count = len(total_word_list)

    # sort counts dictionary and convert to list of pairs (each item in list is a tuple)
    # (key=lambda tells python to look at the value as a number for sorting)
    sorted_counts = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    # get top n number of words
    top_words_list = sorted_counts[:top_num]

    top_results = []
    for top_word, count in top_words_list:
        top_word_proportion = round((count / total_count), 4)
        top_word_percentage = top_word_proportion * 100
        top_results.append((top_word, count, top_word_proportion, top_word_percentage))

    return top_results

def print_results(count_dict, total_words, prop, top, searched_word):
    print('--- TOTAL WORDS ---')
    print(f'The file contains a total of {total_words} words.\n')

    if searched_word in prop:
        word_repeats = count_dict[searched_word]
        proportion = prop[searched_word]
        percentage = round(prop[searched_word] * 100, 4)

        print('--- PROPORTION OF SEARCHED WORD ---')
        print(f'The word "{searched_word}" appears in the text {word_repeats} times with a proportion of {proportion} or {percentage}%.\n')
    else:
        print(f'The word "{searched_word}" does not exist in the text.')

    print('--- TOP WORDS ---')
    # tell python to grab one item from top list of tuples and split into four variables
    for word, count, p, pct in top:
        print(f'The word {word} appears {count} times with a proportion of {p} or {pct}%')

def find_positions(word_list, search_word):
    positions = []

    for i, word in enumerate(word_list, start=1):
        if word == search_word:
            positions.append(i)

    return positions


def replace_words(word_list, positions, replacement, replace_all=False):
    if replace_all:
        for pos in positions:
            word_list[pos - 1] = replacement
    else:
        pos = int(input("Enter the position you want to replace: "))

        if pos in positions:
            word_list[pos - 1] = replacement
        else:
            print("Position not found.")

    return word_list

def save_new_file(original_name, new_name, word_list):

    if original_name == new_name:
        print("New file name must be different from the original.")
        return

    new_text = " ".join(word_list)

    with open(new_name, "w", encoding="utf-8") as file:
        file.write(new_text)

    print(f"Modified file saved as {new_name}")

# RUN CLEAN TEXT FUNCTION - INPUT: TEXT FILE, OUTPUT: ISOLATED WORDS
filename = 'dracula.txt'
file_path = Path(filename)
cleaned_text = clean_text(file_path)
# RUN COUNT WORDS FUNCTION - INPUT: CLEANED TEXT, OUTPUT: TOTAL#WORDS, COUNT DICT (WORD:COUNT)
ignore = ["the", "a", "an", "and", "or", "but", "in", "on", "at", "to"]
counted_words = count_proportion_func(cleaned_text, ignore)
# RUN PROPORTION FUNCTION - INPUT: SEARCHED WORD,TOTAL WORDS, OUTPUT: PROPORTION
search_for_word = "dear"
proportion_result = proportion_func(counted_words)
# RUN TOP N WORDS FUNCTION - INPUT: TOP NUM, OUTPUT: (TOP WORD, OCCURRENCE, PROPORTION, PERCENTAGE)
top_n_words = 3
top_words_results = top_words(top_n_words, counted_words, cleaned_text)
# RUN PRINT RESULTS FUNCTION - INPUT: COUNT DICT, PROP DICT, TOP WORDS
total_word_count = len(cleaned_text)
print_results(counted_words, total_word_count, proportion_result, top_words_results, search_for_word)


