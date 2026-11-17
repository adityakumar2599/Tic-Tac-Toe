#!/usr/bin/env python3
"""
=============================================================================
Rungta International Skills University (RISU)
School of Computer Science and Engineering
Bachelor of Technology - Computer Science and Engineering

Project Code: PS-56
Project Title: Tic-Tac-Toe Console Application
Architecture: Single-file modular Python 3 architecture with integrated verification.
=============================================================================
"""

import sys
from typing import List, Tuple, Optional

# --- DOMAIN CONSTANTS ---
PLAYER_X: str = 'X'
PLAYER_O: str = 'O'
EMPTY_CELL: str = ' '
TOTAL_CELLS: int = 9
MAX_MOVES: int = 9


def display_board(board: List[str]) -> None:
    """
    Renders the current 3x3 game board to standard output.
    Uses list indexing (0 through 8) to format ASCII grid dividers.
    """
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def display_guide() -> None:
    """
    Renders the initial position reference mapping (1-9) to guide players.
    """
    print("\nPositions Guide (1-9):")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")


def check_win(board: List[str], player: str) -> Tuple[bool, Optional[str]]:
    """
    Evaluates all 8 winning lines (3 horizontal rows, 3 vertical columns,
    and 2 diagonals) using conditional structures as mandated by PS-56.

    Returns:
        Tuple[bool, Optional[str]]: (True, winning_line_label) if victorious,
                                    else (False, None).
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


def check_draw(board: List[str]) -> bool:
    """
    Checks if the board is completely filled without empty cells.
    """
    return EMPTY_CELL not in board


def take_move(board: List[str], player: str) -> int:
    """
    Prompts player for input, executes input validation and collision detection.
    Retains player turn upon invalid or collision entries.

    Returns:
        int: Validated 1-based board position (1 through 9).
    """
    while True:
        try:
            raw_input = input(f"Player {player}, enter your move (1-9): ")
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Exiting cleanly.")
            sys.exit(0)

        user_input = raw_input.strip().strip('\ufeff')

        # Format and range validation
        if not user_input.isdigit() or not (1 <= int(user_input) <= TOTAL_CELLS):
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        pos = int(user_input)
        index = pos - 1

        # Collision detection (cell occupied)
        if board[index] != EMPTY_CELL:
            print(f"Position {pos} is already taken. Choose another position.")
            continue

        board[index] = player
        return pos


def play_game() -> None:
    """
    Orchestrates a single complete match round from kickoff to termination.
    """
    # 9-cell board state initialization
    board: List[str] = [EMPTY_CELL for _ in range(TOTAL_CELLS)]
    current_player: str = PLAYER_X  # Player X always plays first
    moves_count: int = 0

    display_guide()
    display_board(board)

    while True:
        take_move(board, current_player)
        moves_count += 1
        display_board(board)

        # Check win condition
        is_won, winning_line = check_win(board, current_player)
        if is_won:
            print(f"Player {current_player} wins!")
            print(f"Winning line: {winning_line}")
            break

        # Check draw condition
        if check_draw(board):
            print(f"Board is full after {moves_count} moves.")
            print("It's a draw! No moves left.")
            break

        # Alternate turn
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


def play_interactive_session() -> None:
    """
    Manages continuous gaming sessions with replay prompt ('Play again? (y/n)').
    """
    while True:
        play_game()

        while True:
            try:
                raw_choice = input("Play again? (y/n): ")
            except (KeyboardInterrupt, EOFError):
                print("\nThanks for playing!")
                return

            choice = raw_choice.strip().strip('\ufeff').lower()
            if choice in ('y', 'yes'):
                print("\nStarting a new game...")
                break
            elif choice in ('n', 'no'):
                print("Thanks for playing!")
                return
            else:
                print("Please enter 'y' or 'n'.")


def run_self_tests() -> None:
    """
    Built-in self-test verification suite executing all 4 PS-56 Test Cases.
    Allows automated machine verification without requiring external files.
    """
    import io
    print("\n--- Running Built-in Senior Verification Suite (4 Test Cases) ---")

    # Test Case 1: Normal Win (Player X)
    captured = io.StringIO()
    sys.stdin = io.StringIO("1\n4\n2\n5\n3\nn\n")
    sys.stdout = captured
    try:
        play_interactive_session()
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    out1 = captured.getvalue()
    assert "Player X wins!" in out1 and "Winning line: 1-2-3" in out1
    print("  [PASS] Test Case 1: Normal Input (Player X Wins 1-2-3)")

    # Test Case 2: Draw after 9 moves
    captured = io.StringIO()
    sys.stdin = io.StringIO("1\n2\n3\n5\n4\n6\n8\n7\n9\nn\n")
    sys.stdout = captured
    try:
        play_interactive_session()
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    out2 = captured.getvalue()
    assert "Board is full after 9 moves." in out2 and "It's a draw! No moves left." in out2
    print("  [PASS] Test Case 2: Boundary Draw (Full 9 Moves)")

    # Test Case 3: Invalid Input and Occupied Collisions
    test_board = [EMPTY_CELL] * 9
    captured = io.StringIO()
    sys.stdin = io.StringIO("10\nabc\n1\n")
    sys.stdout = captured
    try:
        m1 = take_move(test_board, PLAYER_X)
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    out3 = captured.getvalue()
    assert m1 == 1 and "Invalid position. Enter a number from 1 to 9." in out3

    captured_col = io.StringIO()
    sys.stdin = io.StringIO("1\n2\n")
    sys.stdout = captured_col
    try:
        m2 = take_move(test_board, PLAYER_O)
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    out_col = captured_col.getvalue()
    assert m2 == 2 and "Position 1 is already taken. Choose another position." in out_col
    print("  [PASS] Test Case 3: Validation & Collision Handling")

    # Test Case 4: Player O Wins + Replay Termination
    captured = io.StringIO()
    sys.stdin = io.StringIO("1\n4\n2\n5\n9\n6\nn\n")
    sys.stdout = captured
    try:
        play_interactive_session()
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    out4 = captured.getvalue()
    assert "Player O wins!" in out4 and "Winning line: 4-5-6" in out4 and "Thanks for playing!" in out4
    print("  [PASS] Test Case 4: Alternate Scenario (Player O Wins 4-5-6)")

    print("\nAll 4 Test Cases Successfully Verified! Status: 100% PASSED\n")


def main() -> None:
    """
    Main entry point for console gameplay or automated self-testing.
    """
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test"):
        run_self_tests()
    else:
        play_interactive_session()


if __name__ == '__main__':
    main()
