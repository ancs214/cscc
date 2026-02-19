import random

# --- Configuration ---
BOARD_SIZE = 10
NUM_SHIPS = 3
SHIP_SIZE = 3  # All ships are this size for simplicity


# Helper for displaying coordinates (A1, B2, etc.)
def get_coord_label(row, col):
    return f"{chr(65 + row)}{col + 1}"


# Helper function to print the board with row/column labels
def print_board(board, show_ships=False):
    # Print column headers (1 to 10)
    header = "   " + " ".join([str(i + 1) for i in range(BOARD_SIZE)])
    print(header)
    print("  " + "-" * (BOARD_SIZE * 2 - 1))

    # Print each row with its letter label (A to J)
    for row in range(BOARD_SIZE):
        row_label = chr(65 + row)
        row_display = row_label + " |"
        for column in range(BOARD_SIZE):
            cell_value = board[row][column]
            # Mask the ship 'S' symbol unless explicitly told to show
            if cell_value == 'S' and not show_ships:
                row_display += " ~"  # Show water in the hidden board view
            else:
                row_display += f" {cell_value}"
        print(row_display)


# Helper function to create a blank board
def create_blank_board():
    # A simple way for beginners: a list of lists, all filled with water (~)
    board = []
    for board_row in range(BOARD_SIZE):
        row = []
        for board_column in range(BOARD_SIZE):
            row.append('~')  # Use '~' for water
        board.append(row)
    return board


# --- Game Logic ---

# 1. Set up the boards
player_board = create_blank_board()
computer_ships_board = create_blank_board()  # This board holds ship locations
guesses_board = create_blank_board()  # This board tracks player's guesses


# 2. Place Ships (randomly, horizontally)
def place_ships_randomly(board):
    for ship_id in range(NUM_SHIPS):
        placed = False
        while not placed:
            # Pick a random starting row and column
            start_row = random.randint(0, BOARD_SIZE - 1)
            # Ensure the ship doesn't go off the right edge
            start_col = random.randint(0, BOARD_SIZE - SHIP_SIZE)

            # Check if all spots are free before placing
            can_place = True
            for i in range(SHIP_SIZE):
                if board[start_row][start_col + i] == 'S':
                    can_place = False
                    break  # Stop checking if any part is occupied

            if can_place:
                # Place the ship using simple indexing
                for i in range(SHIP_SIZE):
                    board[start_row][start_col + i] = 'S'
                placed = True


place_ships_randomly(computer_ships_board)

# 3. The Main Game Loop
print("--- Welcome to Battleship! ---")
turns = 0

while True:
    turns += 1
    print(f"\n--- Turn {turns} ---")
    print("Your Guesses Board (H = Hit, M = Miss, ~ = Unknown):")
    print_board(guesses_board)
    # Optional: uncomment the line below to cheat and see the computer's ships
    # print("\nComputer's Ships (Cheating View):")
    # print_board(computer_ships_board, show_ships=True)

    # Get Player Input
    while True:
        guess_input = input("Enter your guess (e.g., A1, J10): ").strip().upper()
        if len(guess_input) < 2 or len(guess_input) > 3:
            print("Invalid format. Please use a letter (A-J) and number (1-10).")
            continue

        try:
            # Convert input into list/tuple indices (integers)
            guess_row_char = guess_input[0]
            guess_col_str = guess_input[1:]

            guess_row = ord(guess_row_char) - ord('A')
            guess_col = int(guess_col_str) - 1

            if not (0 <= guess_row < BOARD_SIZE and 0 <= guess_col < BOARD_SIZE):
                print("Coordinates are out of bounds (A1 to J10).")
                continue

            if guesses_board[guess_row][guess_col] in ('H', 'M'):
                print(f"You already guessed {guess_input}. Try again.")
                continue

            # Valid guess received, break the input loop
            break

        except ValueError:
            print("Invalid input. Check your format (e.g., C5).")
            continue
        except IndexError:
            print("Invalid coordinates.")
            continue

    # 4. Check the Guess against the computer's actual ship board
    if computer_ships_board[guess_row][guess_col] == 'S':
        print(f"*** HIT! *** You hit a ship at {guess_input}!")
        guesses_board[guess_row][guess_col] = "\033[43;30mH\033[m"  # Mark as Hit on guess board
        computer_ships_board[guess_row][guess_col] = "\033[43;30mH\033[m" # Mark as Hit on actual board (useful for win condition check)
    else:
        print(f"MISS. You missed the ships at {guess_input}.")
        guesses_board[guess_row][guess_col] = "\033[41;10mM\033[m" # Mark as Miss on guess board
        # No need to update the computer's ship board for a miss

    # 5. Check for Win Condition (check if all 'S' are gone from the actual board)
    ships_remaining = False
    # Use nested loops (simplified for beginners) to check every cell
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if computer_ships_board[r][c] == 'S':
                ships_remaining = True
                break  # Stop searching the inner loop
        if ships_remaining:
            break  # Stop searching the outer loop if found

    if not ships_remaining:
        print(f"\n🎉 CONGRATULATIONS! You sank all {NUM_SHIPS} ships in {turns} turns! 🎉")
        print("Final Board:")
        print_board(guesses_board)
        break  # End the game loop