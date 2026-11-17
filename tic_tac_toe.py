"""
Rungta International Skills University
School of Computer Science and Engineering
Bachelor of Technology - Computer Science and Engineering

PS No.: 56
Project Title: Tic-Tac-Toe
Language: Python 3
Concepts: Lists, Functions, Conditions, Game Logic

Problem Statement:
Develop a two-player console Tic-Tac-Toe game on a 3 x 3 board where players take
turns, the board is displayed after every move, and the winner or a draw is announced.
Positions are numbered 1 to 9 (1-2-3 top row, 4-5-6 middle row, 7-8-9 bottom row).
Player X always plays first.
"""


def display_board(board):
    """
    Displays the 3x3 game board stored in a list of 9 cells.
    """
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def display_guide():
    """
    Displays the reference guide showing cell positions 1 through 9.
    """
    print("\nPositions Guide (1-9):")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")


def check_win(board, player):
    """
    Checks all 8 winning lines (3 rows, 3 columns, 2 diagonals) using conditions.
    Returns (True, winning_line) if player wins, else (False, None).
    """
    # 3 Horizontal Rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True, "1-2-3"
    elif board[3] == player and board[4] == player and board[5] == player:
        return True, "4-5-6"
    elif board[6] == player and board[7] == player and board[8] == player:
        return True, "7-8-9"

    # 3 Vertical Columns
    elif board[0] == player and board[3] == player and board[6] == player:
        return True, "1-4-7"
    elif board[1] == player and board[4] == player and board[7] == player:
        return True, "2-5-8"
    elif board[2] == player and board[5] == player and board[8] == player:
        return True, "3-6-9"

    # 2 Diagonals
    elif board[0] == player and board[4] == player and board[8] == player:
        return True, "1-5-9"
    elif board[2] == player and board[4] == player and board[6] == player:
        return True, "3-5-7"

    return False, None


def check_draw(board):
    """
    Checks if the board is full with no empty cells.
    Returns True if draw, False otherwise.
    """
    return ' ' not in board


def take_move(board, player):
    """
    Prompts the current player for move input and validates:
    - Input must be a valid integer between 1 and 9
    - Selected cell must not already be taken
    Repeats prompt for the same player without advancing turn if invalid.
    """
    while True:
        user_input = input(f"Player {player}, enter your move (1-9): ").strip().strip('\ufeff')

        # Validate input format and range
        if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        pos = int(user_input)
        index = pos - 1

        # Check if cell is occupied
        if board[index] != ' ':
            print(f"Position {pos} is already taken. Choose another position.")
            continue

        board[index] = player
        return pos


def play_game():
    """
    Runs a single full game session of Tic-Tac-Toe.
    """
    # Board stored as a list of 9 cells
    board = [' ' for _ in range(9)]
    current_player = 'X'  # Player X always plays first
    moves_count = 0

    display_guide()
    display_board(board)

    while True:
        take_move(board, current_player)
        moves_count += 1
        display_board(board)

        # Check for win condition
        is_win, winning_line = check_win(board, current_player)
        if is_win:
            print(f"Player {current_player} wins!")
            print(f"Winning line: {winning_line}")
            break

        # Check for draw condition
        if check_draw(board):
            print(f"Board is full after {moves_count} moves.")
            print("It's a draw! No moves left.")
            break

        # Switch turn to the other player
        current_player = 'O' if current_player == 'X' else 'X'


def main():
    """
    Main loop: manages consecutive games and prompts 'Play again? (y/n)'.
    """
    while True:
        play_game()

        while True:
            play_again = input("Play again? (y/n): ").strip().strip('\ufeff').lower()
            if play_again in ['y', 'yes']:
                print("\nStarting a new game...")
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing!")
                return
            else:
                print("Please enter 'y' or 'n'.")


if __name__ == '__main__':
    main()
