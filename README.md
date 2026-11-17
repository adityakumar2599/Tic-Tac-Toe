# 🎮 Tic-Tac-Toe Console Game (Python 3)

**Rungta International Skills University**  
**School of Computer Science and Engineering**  
**Bachelor of Technology - Computer Science and Engineering**  
**Problem Statement No.:** 56  
**Project Title:** Tic-Tac-Toe  

---

## 📌 Project Overview
A robust, interactive two-player console Tic-Tac-Toe game developed in Python 3. Players take alternate turns on a standard 3x3 grid, starting with **Player X**. The board dynamically renders after every move, continuously validating moves, tracking occupied squares, verifying 8 distinct winning conditions, and checking for draw states.

---

## 🧠 Core Programming Concepts Applied
- **Lists**: 1D list of length 9 representing the 3x3 game board (`board = [' ' for _ in range(9)]`).
- **Functions**: Clean modular architecture (`display_board`, `take_move`, `check_win`, `check_draw`, `play_game`, `main`).
- **Conditional Logic (`if-elif-else`)**: Evaluates all 8 winning lines (3 horizontal rows, 3 vertical columns, 2 diagonals).
- **Game Logic & State Loops**: Turn switching, input validation, replay prompt (`Play again? (y/n)`).

---

## 🔢 Board Layout & Numbering Convention
Positions are numbered 1 through 9:
```text
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```
- **Top row:** 1, 2, 3
- **Middle row:** 4, 5, 6
- **Bottom row:** 7, 8, 9

---

## 🏆 Winning Conditions Checked (8 Lines)
1. **Row 1:** Positions `1-2-3` (indices `0, 1, 2`)
2. **Row 2:** Positions `4-5-6` (indices `3, 4, 5`)
3. **Row 3:** Positions `7-8-9` (indices `6, 7, 8`)
4. **Column 1:** Positions `1-4-7` (indices `0, 3, 6`)
5. **Column 2:** Positions `2-5-8` (indices `1, 4, 7`)
6. **Column 3:** Positions `3-6-9` (indices `2, 5, 8`)
7. **Main Diagonal:** Positions `1-5-9` (indices `0, 4, 8`)
8. **Anti-Diagonal:** Positions `3-5-7` (indices `2, 4, 6`)

---

## 🧪 Verified Test Cases

### Test Case 1: Normal Input (Player X Wins)
- **Moves:** `X: 1`, `O: 4`, `X: 2`, `O: 5`, `X: 3`
- **Output:**
  ```text
  Player X wins!
  Winning line: 1-2-3
  ```

### Test Case 2: Boundary / Minimum Input (Draw)
- **Moves:** `X: 1`, `O: 2`, `X: 3`, `O: 5`, `X: 4`, `O: 6`, `X: 8`, `O: 7`, `X: 9`
- **Output:**
  ```text
  Board is full after 9 moves.
  It's a draw! No moves left.
  ```

### Test Case 3: Invalid Input & Turn Integrity
- **Inputs & Responses:**
  - `Position: 10` ➔ `Invalid position. Enter a number from 1 to 9.`
  - `Position: abc` ➔ `Invalid position. Enter a number from 1 to 9.`
  - `X plays 1, then O plays 1` ➔ `Position 1 is already taken. Choose another position.`
  *(Note: Turn does not advance upon invalid or occupied input).*

### Test Case 4: Different Valid Scenario (Player O Wins + Replay)
- **Moves:** `X: 1`, `O: 4`, `X: 2`, `O: 5`, `X: 9`, `O: 6`
- **Output:**
  ```text
  Player O wins!
  Winning line: 4-5-6
  Play again? n
  Thanks for playing!
  ```

---

## 🚀 How to Run

### Run the Game:
```bash
python tic_tac_toe.py
```

### Run Automated Unit Tests:
```bash
python test_tic_tac_toe.py
```
*(All 4 unit tests execute and pass out-of-the-box).*

---

## 📂 Project Structure
```text
tic-tac-toe/
├── tic_tac_toe.py        # Complete console game application
├── test_tic_tac_toe.py   # Automated unit tests covering all 4 test cases
├── PROJECT_REPORT.md     # Formal academic project documentation & analysis
└── README.md             # Project summary and instructions
```
