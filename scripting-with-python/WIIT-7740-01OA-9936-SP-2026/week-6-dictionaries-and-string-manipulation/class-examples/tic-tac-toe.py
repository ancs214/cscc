import random

def print_board(board):
    """Display the current game board"""
    print("\n")
    for i in range(3):
        print(f"  {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print(" -----------")
    print("\n")


def check_winner(board):
    """Check if there is a winner on the board"""
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def get_available_moves(board):
    """Return a dictionary of available positions on the board"""
    available_moves = {}
    move_number = 1

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves[move_number] = (row, col)
                move_number += 1

    return available_moves

def display_available_positions(board):
    """Display available positions for the player to choose from"""
    available_moves = get_available_moves(board)

    if not available_moves:
        return

    print("Available positions:")
    for move_num, (row, col) in available_moves.items():
        print(f"  {move_num}: Position ({row}, {col})", end="  ")
        if move_num % 3 == 0:
            print()
    print("\n")

def is_board_full(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def computer_move(board):
    """Make the computer's move using smart strategy"""
    available_moves = get_available_moves(board)

    # Try to win if possible
    for move_num, (row, col) in available_moves.items():
        board[row][col] = "O"
        if check_winner(board) == "O":
            print(f"Computer chose position ({row}, {col})\n")
            return
        board[row][col] = " "

    # Try to block the player from winning
    for move_num, (row, col) in available_moves.items():
        board[row][col] = "X"
        if check_winner(board) == "X":
            board[row][col] = "O"
            print(f"Computer chose position ({row}, {col})\n")
            return
        board[row][col] = " "

    # Take the center if available
    if (1, 1) in available_moves.values():
        board[1][1] = "O"
        print("Computer chose position (1, 1)\n")
        return

    # Take a corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in corners:
        if corner in available_moves.values():
            board[corner[0]][corner[1]] = "O"
            print(f"Computer chose position {corner}\n")
            return

    # Take any remaining available move
    if available_moves:
        move_num = random.choice(list(available_moves.keys()))
        row, col = available_moves[move_num]
        board[row][col] = "O"
        print(f"Computer chose position ({row}, {col})\n")

def game_info():
        # While loop for multiple games
        playing = True
        while playing:
            tic_tac_toe()
            playing = play_again()

        """Display information and description about tic-tac-toe"""
        print("\n" + "=" * 70)
        print(" " * 20 + "TIC-TAC-TOE GAME INFO")
        print("=" * 70)

        print("\nGAME DESCRIPTION:")
        print("-" * 70)
        print("Tic-Tac-Toe is a classic two-player strategy game, also known as")
        print("Noughts and Crosses. The game is played on a 3x3 grid board.")
        print("In this version, YOU play against the COMPUTER!")

        print("\nOBJECTIVE:")
        print("-" * 70)
        print("Be the first player to get three of your marks (X) in a row,")
        print("column, or diagonal line. The computer plays as O and will try")
        print("to win while blocking your moves.")

        print("\nThanks for playing Tic-Tac-Toe! Goodbye! 👋\n")

        print("\nHOW TO PLAY:")
        print("-" * 70)
        print("1. You play as 'X' and go first")
        print("2. The computer plays as 'O'")
        print("3. The board has positions numbered 1-9 (available positions)")
        print("4. When prompted, enter the number of the position where you")
        print("   want to place your mark")
        print("5. Board layout with row and column positions:")
        print("   (0,0) | (0,1) | (0,2)")
        print("   (1,0) | (1,1) | (1,2)")
        print("   (2,0) | (2,1) | (2,2)")

        print("\nWINNING CONDITIONS:")
        print("-" * 70)
        print("• Get 3 of your marks in a horizontal row")
        print("• Get 3 of your marks in a vertical column")
        print("• Get 3 of your marks in a diagonal line")
        print("• If all 9 squares are filled with no winner, it's a draw")
        print("\nSTRATEGY TIPS:")
        print("-" * 70)
        print("• The center square (1,1) is the most valuable position")
        print("• Corner squares (0,0), (0,2), (2,0), (2,2) are strong positions")
        print("• Always watch for the computer's winning moves and block them")
        print("• Try to create multiple winning opportunities at once")

        print("\nCOMPUTER STRATEGY:")
        print("-" * 70)
        print("The computer will:")
        print("• Win if it can on its next move")
        print("• Block your winning moves")
        print("• Take the center or corners when possible")
        print("• Make random strategic moves otherwise")

        print("=" * 70 + "\n")

def tic_tac_toe():
    # main game loop for player vs computer
    # list to store the game board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print("\n" + "=" * 70)
    print(" " * 25 + "GAME STARTED!")
    print("=" * 70)
    print("You are X and the computer is O")
    print("You go first!\n")

    # while loop for the main game
    while True:
        print_board(board)

        # player's turn with input validation
        while True:
            display_available_positions(board)

            try:
                position = int(input("Enter position number(1-9): "))
                available_moves = get_available_moves(board)

                if position in available_moves:
                    row, col = available_moves[position]
                    board[row][col] = "X"
                    break
                else:
                    print("That position is not available! Choose another one.\n")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.\n")

        # Check if player won
        winner = check_winner(board)
        if winner == "X":
            print_board(board)
            print("🎉 Congratulations! You win! 🎉\n")
            return

        # Check if board is full
        if is_board_full(board):
            print_board(board)
            print("It's a draw!\n")
            return

        # Computer's turn
        print("Computer is thinking...\n")
        computer_move(board)

        # Check if computer won
        winner = check_winner(board)
        if winner == "O":
            print_board(board)
            print("The computer wins! Better luck next time!\n")
            return

        # Check if board is full
        if is_board_full(board):
            print_board(board)
            print("It's a draw!\n")
            return

def play_again():
    """Ask if the player wants to play again"""
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.\n")

# kicks off everything for python program
if __name__ == "__main__":
    game_info()

    # While loop for multiple games
    playing = True
    while playing:
        tic_tac_toe()
        playing = play_again()

    print("\nThanks for playing Tic-Tac-Toe! Goodbye! 👋\n")