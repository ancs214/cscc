from pathlib import Path


# ---------------------------
# 1. Read and clean text
# ---------------------------
def read_text(file_path):
    """Read file and return a list of words in lowercase, punctuation removed."""
    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist.")
        return []

    contents = file_path.read_text(encoding='utf-8').lower()

    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”‘’'
    # replace every punctuation mark in contents with a space
    for char in punctuation:
        contents = contents.replace(char, " ")

    # split words now that our text is cleaned up
    words = contents.split()
    return words


# ---------------------------
# 2. Count words and proportions
# ---------------------------
def count_words(words_list, ignore_words=None):
    """Count words, excluding ignore_words, and calculate proportions."""
    if ignore_words is None:
        ignore_words = []

    counts = {}
    for word in words_list:
        if word in ignore_words:
            # skip the rest of the loop and move to next item
            continue

        if word in counts:
            # if word is already a key, increase value in key/value pair by 1
            counts[word] += 1
        else:
            # if word is new, create key and set value to 1
            counts[word] = 1

    total_words = len(words_list)

    proportion = {}
    for word in counts:
        count = counts[word]
        prop = round(count / total_words, 4)
        proportion[word] = prop

    return total_words, counts, proportion


# ---------------------------
# 3. Search for a word
# ---------------------------
def search_word(word, counts, proportion):
    """Return count and proportion of word or message if not found."""
    if word in counts:
        word_count = counts[word]
        word_prop = proportion[word]
        word_percentage = round(word_prop * 100, 2)
        return f'"{word}" appears in the text {word_count} times with a proportion of {word_prop} ({word_percentage}%)'
    else:
        return f'"{word}" not found in the text.'


# ---------------------------
# 4. Top N words
# ---------------------------
def top_n_words(counts, proportion, n):
    """Return top n words sorted by count with their proportions."""
    # sort counts dictionary and convert to list of pairs (each item in list is a tuple)
    # (key=lambda tells python to look at the value as a number for sorting)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # get top n number of words
    top_words = sorted_counts[:n]

    results = []
    for word, count in top_words:
        prop = proportion[word]
        results.append(f'Word: {word}\nCount: {count}\nProportion: {prop}\n')
    return results


# ---------------------------
# 5. Find positions and replace
# ---------------------------
def find_positions(words_list, target_word):
    """Return a list of positions where the target_word appears."""
    positions = []
    for i in range(len(words_list)):
        if words_list[i] == target_word:
            positions.append(i + 1)  # +1 to make it "1-based" and more natural for humans
    return positions

def replace_word(words_list, target_word, replacement, replace_all=True, specific_positions=None):
    """Replace word at specified positions; returns modified list."""
    if replace_all:
        # Replace every occurrence of target_word
        for i in range(len(words_list)):
            if words_list[i] == target_word:
                words_list[i] = replacement
    else:
        # Replace only at specific positions
        for pos in specific_positions:
            words_list[pos - 1] = replacement  # -1 because list is 0-indexed
    return words_list


# ---------------------------
# 6. Save new file
# ---------------------------
def save_new_file(words_list, new_file_path, original_file_path):
    """Save words_list to a new file. New file name must be different from the original."""
    try:
        if new_file_path == original_file_path:
            print("New file name must be different from the original file.")
            return

        text = " ".join(words_list)
        Path(new_file_path).write_text(text, encoding='utf-8')
        print(f"Modified file saved as {new_file_path}")

    except Exception as e:
        # Catch any other unexpected errors
        print("An error occurred while saving the file:", e)

# ---------------------------
# Interactive workflow
# ---------------------------
def main():
    # --- File input ---
    original_filename = input("Enter the name of the text file to analyze: ").strip()
    file_path = Path(original_filename)

    words = read_text(file_path)

    # --- Ignore words ---
    ignore_input = input("Enter words to ignore separated by spaces (or press Enter to skip): ")
    ignore_words = ignore_input.lower().split() if ignore_input else []

    # --- Word counts ---
    # count_words returns a tuple with total_words, counts, proportion
    total_words, counts, proportion = count_words(words, ignore_words)
    print(f'\nTotal words: {total_words}\n')

    # --- Search for a word ---
    search_for = input("Enter a word to search for in the text: ").strip().lower()
    print(search_word(search_for, counts, proportion))

    # --- Top N words ---
    top_n = int(input("How many top words do you want to see? "))
    print(f"\n--- Top {top_n} Words ---")
    top_words_list = top_n_words(counts, proportion, top_n)
    for line in top_words_list:
        print(line)

    # --- Find positions ---
    positions = find_positions(words, search_for)
    if positions:
        print(f'Positions of "{search_for}" in the text: {positions}')
        # --- Replace word ---
        replacement = input(f"Enter a replacement for '{search_for}': ").strip().lower()
        replace_choice = input("Replace all instances? (yes/no): ").strip().lower()
        replace_all = replace_choice == 'yes'
        words = replace_word(words, positions, replacement, replace_all)
    else:
        print(f'Word "{search_for}" not found. No replacement will be made.')

    # --- Save modified file ---
    # new_filename = input("Enter a new filename to save the modified text: ").strip()
    # save_new_file(words, new_filename, original_filename)


# Run the interactive program
if __name__ == "__main__":
    main()