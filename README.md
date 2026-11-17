<div align="center">

# 🎮 Tic-Tac-Toe Console Application
### Robust, Zero-Dependency Console Engine in Python 3

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Code Style: PEP 8](https://img.shields.io/badge/Code%20Style-PEP%208-brightgreen.svg)](https://pep8.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Verification: 100% Passed](https://img.shields.io/badge/Verification-100%25%20Passed-success.svg)](tic_tac_toe.py)

**Rungta International Skills University (RISU)**  
*School of Computer Science and Engineering*  
**Problem Statement No.:** 56 &nbsp;|&nbsp; **Academic Track:** B.Tech CSE

</div>

---

## 📌 Executive Summary
A production-grade, zero-dependency console-based implementation of the classic **Tic-Tac-Toe** game engineered in modern Python 3. The system is architected as a **pure single-file application (`tic_tac_toe.py`)** adhering strictly to Senior Engineering principles: strict type annotations (`typing`), deterministic state management, defensive input parsing, collision detection, and zero unhandled exceptions.

---

## 📐 Architectural Design & System Flow

The application follows clean functional decomposition:

```text
                     +----------------------------+
                     |           main()           |
                     +--------------+-------------+
                                    |
                     +--------------v-------------+
                     |  play_interactive_session  |
                     +--------------+-------------+
                                    |
                     +--------------v-------------+
                     |        play_game()         |
                     +--------------+-------------+
                                    |
        +---------------------------+---------------------------+
        |                           |                           |
+-------v-------+           +-------v-------+           +-------v-------+
| display_board |           |   take_move   |           |   check_win   |
| (ASCII Grid)  |           | (Sanitize/In) |           | (8 Conditions)|
+---------------+           +---------------+           +---------------+
                                    |                           |
                            +-------v-------+           +-------v-------+
                            |  check_draw   |           | display_guide |
                            |  (Exhaustion) |           | (Keypad 1-9)  |
                            +---------------+           +---------------+
```

---

## 🔢 Board Spatial Model & Grid Mapping
The board is represented internally as a 1-dimensional array of 9 cells indexed `[0..8]` and mapped to the standard 1-9 user keypad:

```text
 Reference Keypad           Rendered Board
   1 | 2 | 3                   X | O | X 
  ---+---+---                 ---+---+---
   4 | 5 | 6                   O | X |   
  ---+---+---                 ---+---+---
   7 | 8 | 9                     |   | O 
```

### Deterministic Winning Logic (8 Conditions):
1. **Horizontal Rows:** `1-2-3` `[0,1,2]`, `4-5-6` `[3,4,5]`, `7-8-9` `[6,7,8]`
2. **Vertical Columns:** `1-4-7` `[0,3,6]`, `2-5-8` `[1,4,7]`, `3-6-9` `[2,5,8]`
3. **Diagonals:** `1-5-9` `[0,4,8]`, `3-5-7` `[2,4,6]`

---

## 🧪 Automated Verification Suite (Built-in)
The application includes an embedded senior self-test engine capable of verifying all mandatory test cases autonomously without requiring secondary files or test frameworks:

| Test Case | Scenario Description | Inputs | Expected Output | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Case 1** | Normal Win (Player X) | `X:1, O:4, X:2, O:5, X:3` | `Player X wins!`<br>`Winning line: 1-2-3` | ✅ **PASS** |
| **Case 2** | Full 9-Move Draw | `X:1, O:2, X:3, O:5, X:4, O:6, X:8, O:7, X:9` | `Board is full after 9 moves.`<br>`It's a draw! No moves left.` | ✅ **PASS** |
| **Case 3** | Input Validation & Collisions | `10`, `abc`, cell overwrite | `Invalid position. Enter a number from 1 to 9.`<br>`Position 1 is already taken. Choose another position.` | ✅ **PASS** |
| **Case 4** | Alternate Win & Session Exit | `X:1, O:4, X:2, O:5, X:9, O:6`, `n` | `Player O wins!`<br>`Winning line: 4-5-6`<br>`Thanks for playing!` | ✅ **PASS** |

---

## 🚀 Execution & Usage

### 1. Launch Game:
```bash
python tic_tac_toe.py
```

### 2. Run Self-Test Suite:
```bash
python tic_tac_toe.py --test
```

---

## 📁 Repository Structure
```text
Tic-Tac-Toe/
├── tic_tac_toe.py       # Core single-file application with built-in test suite
├── PROJECT_REPORT.md    # Formal academic documentation for RISU CSE Department
├── README.md            # Architecture & execution guide
└── .gitignore           # Git ignore rules
```
