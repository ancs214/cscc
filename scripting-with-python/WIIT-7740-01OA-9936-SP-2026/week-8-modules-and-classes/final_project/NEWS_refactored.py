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
    """Cleans the text of the file"""
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
    """
    Creates a dictionary with non-ignored words and their counts. Then creates a
    dictionary with non-ignored words and their proportions of appearance in the text.
    """
    counts = {}
    non_ignored_words = []
    for word in words:
        # ignore designated words input by user
        if word in ignore_words:
            # skip the rest of the loop and move to next item
            continue

        # add to non-ignored list
        non_ignored_words.append(word)

        if word in counts:
            # if word is already a key, increase value in key/value pair by 1
            counts[word] += 1
        else:
            # if word is new, create key and set value to 1
            counts[word] = 1

    # total number of non-ignored words
    total_non_ignored = sum(counts.values())

    proportions = {}
    for word in counts:
        # look up each key's value, divide by total num of words
        word_proportion = round((counts[word] / total_non_ignored), 4)
        # add key/value pair to proportion{}
        proportions[word] = word_proportion

    return counts, proportions, total_non_ignored, non_ignored_words

#------------------------------
#------TOP WORDS FUNCTION------
#------------------------------
def top_words(top_num, counts, total_non_ignored):
    """
    Sorts the counts dictionary from greatest to smallest value and takes user input
    to determine how many top results to display.
    """
    # sort counts dictionary and convert to list of pairs (each item in list is a tuple)
    # (key=lambda tells python to look at the value as a number for sorting)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # get top n number of words
    top_words_list = sorted_counts[:top_num]

    top_results = []
    for top_word, count in top_words_list:
        top_word_proportion = round((count / total_non_ignored), 4)
        top_word_percentage = round(top_word_proportion * 100, 4)
        top_results.append((top_word, count, top_word_proportion, top_word_percentage))

    return top_results

#-----------------------------------
# ------PRINT RESULTS FUNCTION------
#-----------------------------------
def print_results(counts, words, proportions, top_results, searched_word):
    """
    Takes results from counts, proportions, and top words and prints total words, proportion of
    searched word, and top words with corresponding count and proportion.
    """
    num_words = len(words)
    print('---------------------------------------------------------')
    print('----------------------FINAL RESULTS----------------------')
    print('---------------------------------------------------------\n')

    print('--- TOTAL WORDS ---')
    print(f'The file contains a total of {num_words} words.\n')

    if searched_word in counts:
        word_repeats = counts[searched_word]
        proportion = proportions[searched_word]
        percentage = round(proportion * 100, 4)

        print('--- PROPORTION OF SEARCHED WORD ---')
        print(f'The word "{searched_word}" appears in the text {word_repeats} times with a proportion of {proportion} or {percentage}%.\n')
    else:
        print(f'The word "{searched_word}" does not exist in the text.')

    print('--- TOP WORDS ---')
    # "unpacking" tells python to grab one item from top list of tuples and split into four variables
    for word, count, prop, percent in top_results:
        print(f'Word: "{word}"\nCount: {count}\nProportion: {prop} or {percent}%\n')

#--------------------------------------------
#------FIND POSITION OF STRING FUNCTION------
#--------------------------------------------
def find_positions(non_ignored_words, string_search):
    """Finds numerical position of the word user searched text for."""
    positions = []
    # loop through each item with counter, starting at 1 instead of 0
    for i, word in enumerate(non_ignored_words, start=1):
        # if word=string_search, add to positions list
        if word == string_search:
            positions.append(i)

    return positions

#-----------------------------------
#------REPLACE STRING FUNCTION------
#-----------------------------------
def replace_words(total_non_ignored, positions, replacement, replace_all=False):
    """
    Replaces the word user searched for. Gives user the option to replace all occurrences
    or only one word at a specific position.
    """
    # create copy of total_non_ignored so original list remains intact
    replaced_words_list = list(total_non_ignored)
    if replace_all:
        for pos in positions:
            # updates list with replacement, converting "1" back to "0" for python
            replaced_words_list[pos - 1] = replacement
    else:
        try:
            pos = int(input("Enter the position you want to replace: "))

            if pos in positions:
                # updates list with replacement, converting "1" back to "0" for python
                replaced_words_list[pos - 1] = replacement
            else:
                print("Position not found.")
        except ValueError:
            print("Please enter a valid number.")

    return replaced_words_list

#----------------------------------
#------SAVE NEW FILE FUNCTION------
#----------------------------------
def save_new_file(original_name, new_name, replaced_words_list):
    """Save modified document to a new file with new name."""
    if original_name == new_name:
        print("New file name must be different from the original.")
        return

    # converts list of words back into a single string separated by spaces
    new_text = " ".join(replaced_words_list)

    # write file
    with open(new_name, "w", encoding="utf-8") as file:
        file.write(new_text)

    print(f"Modified file saved as {new_name}")

#-------------------------
#------MAIN FUNCTION------
#-------------------------
def main():
    # get file name
    filename = input("Enter the file path (e.g., document.txt): ")
    file_path = Path(filename)

    if not file_path.exists():
        print("Error: File not found.")
        return

    # get ignore words
    ignore = input("Enter words to ignore (separated by space): ").lower().split()

    # clean text
    all_words = clean_text(file_path)

    # pass variables into count_proportion function to get counts and proportion
    counts, proportions, total_non_ignored, non_ignored_words = count_proportion_func(all_words, ignore)

    # search for string
    string_search = input("\nEnter the word you want to find: ").lower()

    # ask replacement word
    replacement = input("\nEnter the replacement word: ").lower()

    # find position of searched word and show user
    positions = find_positions(non_ignored_words, string_search)
    print(f'The word "{string_search}" appears at positions:')
    print(positions)

    # ask replace all or no
    choice = input("Do you want to replace ALL occurrences? (yes/no): ").lower()

    if choice == "yes":
        replace_all = True
    else:
        replace_all = False

    # pass variables into replace function
    replaced_words_list = replace_words(non_ignored_words, positions, replacement, replace_all)

    # ask how many top words
    top_num = int(input("\nHow many top words would you like to see? "))

    # get top results
    top_results_list = top_words(top_num, counts, total_non_ignored)

    # pass variables into print function
    print_results(counts, all_words, proportions, top_results_list, string_search)

    # save renamed file
    new_filename = input("\nEnter a name for the new file: ")
    save_new_file(filename, new_filename, replaced_words_list)

if __name__ == "__main__":
        main()