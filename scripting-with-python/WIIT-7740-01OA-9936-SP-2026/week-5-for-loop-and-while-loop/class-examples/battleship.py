"""
FILE_NAME: battleship.py
AUTHOR: Ashley-Noel Swarn
DATE: 02-15-2026
PURPOSE: Create a replica of the game Battleship.
"""
import random

# ---Configuration Values --
BOARD_SIZE = 10
NUM_SHIPS = 3
SHIP_SIZE = 3

# Function that displays the coordinates

# Function to create a blank board

# Function that places ships randomly

# Function to print the board with row/columns labels
def print_board(board, show_ships=False):
    header = " " + " ".join([str(i + 1) for i in range(BOARD_SIZE)])
    print(header)
    print(" " + "-" * (BOARD_SIZE * 2 - 1))

    for row in range(BOARD_SIZE):
        row_label = chr(65 + row)
        row_display = row_label + " |"
        for column in range(BOARD_SIZE):
            cell_value = board[row][column]
            if cell_value == 'S' and not show_ships:
                row_display += ' ~'
            else:
                row_display += f" {cell_value}"
        print(row_display)



# Gameplay logic
print('---Welcome to Battleship! ---')
turns = 0

while True:
    turns += 1
    print(f'\n--- Turn {turns} ---')
    print('Your Guesses Board (H = Hit, M = Miss, ~ = Water):')
    print_board(guesses_board)

    while True:
        guess_input = input('Enter your guess (e.g. A1, J10): ').strip().upper()
        if len(guess_input) < 2 or len(guess_input) > 3:
            print('Invalid format. Please use a letter (A-J) and a number (1-10).')
            continue

        try:
            guess_row_char = guess_input[0]
            guess_col_str = guess_input[1:]

            guess_row = ord(guess_row_char) - ord('A')
            guess_col = int(guess_col_str) - 1

            if not(0 <= guess_row < BOARD_SIZE and 0 <= guess_col < BOARD_SIZE):
                print(f'Coordinates are out of bounds (A1 - J10).')
                continue

        except ValueError:
            print('Invalid input. Check your format (e.g. C5).')
            continue
        except IndexError:
            print('Invalid coordinates.')
            continue


