# ACADEMIC PROJECT REPORT

## PROJECT TITLE: TIC-TAC-TOE CONSOLE APPLICATION
**Problem Statement No.:** 56  
**Course:** Bachelor of Technology - Computer Science and Engineering  
**Department:** School of Computer Science and Engineering  
**Institution:** Rungta International Skills University  
**Language:** Python 3  

---

### 1. ABSTRACT
This report presents the design, architectural structure, implementation, and verification of a two-player console-based Tic-Tac-Toe game created in Python 3. The system enforces zero external dependencies, relying solely on core standard library data structures (lists, conditional statements, functional decompositions, and standard I/O). The game ensures strict turn alternations between Player X and Player O, interactive position validation (range and collision checks), instant 3x3 board rendering after each turn, verification of all 8 winning lines, boundary detection for 9-move draw states, and an interactive session loop.

---

### 2. PROBLEM DEFINITION & OBJECTIVES
The objective of Problem Statement 56 is to engineer an interactive, robust 3x3 Tic-Tac-Toe game in Python satisfying the following specifications:
1. **Single-File Execution:** Complete logic encapsulated cleanly within one executable Python file (`tic_tac_toe.py`).
2. **Board Representation:** Store the 3x3 board state within a 1-dimensional list of 9 elements.
3. **Turn Progression:** Player X always moves first, alternating turns with Player O upon every valid move.
4. **Input Sanitization & Error Handling:**
   - Detect and reject out-of-bounds positions (<1 or >9).
   - Detect and reject non-integer strings (e.g., "abc").
   - Reject attempts to overwrite already-occupied cells without toggling player turns.
5. **Winning & Draw Determination:** Check all 8 possible winning lines (3 horizontal, 3 vertical, 2 diagonal) via conditional statements, outputting the exact winning line identifier.
6. **Game Replay:** Ask the user `Play again? (y/n)` upon game conclusion.

---

### 3. SYSTEM ARCHITECTURE & FUNCTIONAL SPECIFICATION

The program is architected around functional decomposition:

```
                  +---------------------------+
                  |          main()           |
                  +-------------+-------------+
                                |
                  +-------------v-------------+
                  |        play_game()        |
                  +-------------+-------------+
                                |
        +-----------------------+-----------------------+
        |                       |                       |
+-------v-------+       +-------v-------+       +-------v-------+
| display_board |       |   take_move   |       |   check_win   |
+---------------+       +---------------+       +---------------+
                                |                       |
                                v                       v
                        +---------------+       +---------------+
                        |  check_draw   |       | display_guide |
                        +---------------+       +---------------+
```

#### Functions Description:
- **`display_board(board)`**: Formats and prints the 3x3 grid using ASCII layout dividers.
- **`display_guide()`**: Displays position reference mapping indices `1` to `9` to board cells.
- **`take_move(board, player)`**: Handles input extraction, validates integer format, checks cell vacancy, and marks cell.
- **`check_win(board, player)`**: Evaluates all 8 winning combinations using explicit `if-elif` conditional structures and returns a tuple `(is_win: bool, line_name: str)`.
- **`check_draw(board)`**: Evaluates whether all 9 cells are occupied with no winner.
- **`play_game()`**: Orchestrates a single match round.
- **`main()`**: Manages the continuous gaming loop and processes `Play again? (y/n)`.

---

### 4. WINNING COMBINATIONS MATRIX
Mapping between 1-based console inputs and 0-based Python list indices:

| Line Type | Positions | List Indices Checked | Identification String |
| :--- | :--- | :--- | :--- |
| Row 1 | 1, 2, 3 | `0, 1, 2` | `1-2-3` |
| Row 2 | 4, 5, 6 | `3, 4, 5` | `4-5-6` |
| Row 3 | 7, 8, 9 | `6, 7, 8` | `7-8-9` |
| Column 1 | 1, 4, 7 | `0, 3, 6` | `1-4-7` |
| Column 2 | 2, 5, 8 | `1, 4, 7` | `2-5-8` |
| Column 3 | 3, 6, 9 | `2, 5, 8` | `3-6-9` |
| Diagonal 1 | 1, 5, 9 | `0, 4, 8` | `1-5-9` |
| Diagonal 2 | 3, 5, 7 | `2, 4, 6` | `3-5-7` |

---

### 5. TEST EXECUTION & VERIFICATION

Automated testing was conducted using Python's `unittest` framework to execute the exact test cases outlined in Problem Statement 56:

#### Test Case 1: Normal Input (Player X Wins)
- **Input sequence:** `X: 1`, `O: 4`, `X: 2`, `O: 5`, `X: 3`
- **Observed Result:**
  ```text
  Player X wins!
  Winning line: 1-2-3
  ```
- **Status:** PASSED

#### Test Case 2: Boundary / Minimum Input (Draw)
- **Input sequence:** `X: 1`, `O: 2`, `X: 3`, `O: 5`, `X: 4`, `O: 6`, `X: 8`, `O: 7`, `X: 9`
- **Observed Result:**
  ```text
  Board is full after 9 moves.
  It's a draw! No moves left.
  ```
- **Status:** PASSED

#### Test Case 3: Invalid Input & Turn Integrity
- **Inputs & Output Observations:**
  - Input `10` -> `Invalid position. Enter a number from 1 to 9.`
  - Input `abc` -> `Invalid position. Enter a number from 1 to 9.`
  - Input `1` followed by `1` -> `Position 1 is already taken. Choose another position.`
  - Turn preservation: Player turn remained on the current player until a valid move was executed.
- **Status:** PASSED

#### Test Case 4: Different Valid Scenario (Player O Wins & Termination)
- **Input sequence:** `X: 1`, `O: 4`, `X: 2`, `O: 5`, `X: 9`, `O: 6`, `n`
- **Observed Result:**
  ```text
  Player O wins!
  Winning line: 4-5-6
  Thanks for playing!
  ```
- **Status:** PASSED

---

### 6. CONCLUSION
The application fulfills all requirements mandated by Problem Statement 56. The code is modular, adheres to Python PEP 8 conventions, performs rigorous input validation, and passes all required test cases.
