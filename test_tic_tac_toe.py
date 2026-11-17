"""
Automated Test Suite for Tic-Tac-Toe
Verifies all 4 Test Cases from Problem Statement 56.
"""

import sys
import io
import unittest
from tic_tac_toe import check_win, check_draw, take_move, main


class TestTicTacToeCases(unittest.TestCase):

    def test_case_1_normal_input(self):
        """
        Test Case 1: Normal Input
        Moves: X:1, O:4, X:2, O:5, X:3
        Expected Output:
        Player X wins!
        Winning line: 1-2-3
        """
        inputs = iter(['1', '4', '2', '5', '3', 'n'])
        captured_output = io.StringIO()
        sys.stdin = io.StringIO('\n'.join(['1', '4', '2', '5', '3', 'n']) + '\n')
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Player X wins!", output)
        self.assertIn("Winning line: 1-2-3", output)

    def test_case_2_boundary_draw(self):
        """
        Test Case 2: Boundary / Minimum Input (Draw after 9 moves)
        Moves: X:1, O:2, X:3, O:5, X:4, O:6, X:8, O:7, X:9
        Expected Output:
        Board is full after 9 moves.
        It's a draw! No moves left.
        """
        test_inputs = ['1', '2', '3', '5', '4', '6', '8', '7', '9', 'n']
        captured_output = io.StringIO()
        sys.stdin = io.StringIO('\n'.join(test_inputs) + '\n')
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Board is full after 9 moves.", output)
        self.assertIn("It's a draw! No moves left.", output)

    def test_case_3_invalid_input(self):
        """
        Test Case 3: Invalid Input
        (a) Position: 10 -> Invalid position. Enter a number from 1 to 9.
        (b) Position: abc -> Invalid position. Enter a number from 1 to 9.
        (c) X plays 1, then O plays 1 -> Position 1 is already taken. Choose another position. (turn does not change)
        """
        board = [' ' for _ in range(9)]
        captured_output = io.StringIO()
        # Test 10 and abc
        sys.stdin = io.StringIO('10\nabc\n1\n')
        sys.stdout = captured_output
        try:
            move = take_move(board, 'X')
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertEqual(move, 1)
        self.assertEqual(board[0], 'X')
        self.assertIn("Invalid position. Enter a number from 1 to 9.", output)

        # Test position already taken (O attempts position 1, then chooses 2)
        captured_output_2 = io.StringIO()
        sys.stdin = io.StringIO('1\n2\n')
        sys.stdout = captured_output_2
        try:
            move_2 = take_move(board, 'O')
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

        output_2 = captured_output_2.getvalue()
        self.assertEqual(move_2, 2)
        self.assertEqual(board[1], 'O')
        self.assertIn("Position 1 is already taken. Choose another position.", output_2)

    def test_case_4_different_valid_scenario(self):
        """
        Test Case 4: Different Valid Scenario
        Moves: X:1, O:4, X:2, O:5, X:9, O:6
        Play again? n
        Expected Output:
        Player O wins!
        Winning line: 4-5-6
        Thanks for playing!
        """
        test_inputs = ['1', '4', '2', '5', '9', '6', 'n']
        captured_output = io.StringIO()
        sys.stdin = io.StringIO('\n'.join(test_inputs) + '\n')
        sys.stdout = captured_output

        try:
            main()
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Player O wins!", output)
        self.assertIn("Winning line: 4-5-6", output)
        self.assertIn("Thanks for playing!", output)


if __name__ == '__main__':
    unittest.main()
