# ACADEMIC PROJECT REPORT

## PROJECT TITLE: SENIOR ARCHITECTURE TIC-TAC-TOE CONSOLE APPLICATION
**Problem Statement No.:** 56  
**Course:** Bachelor of Technology - Computer Science and Engineering  
**Department:** School of Computer Science and Engineering  
**Institution:** Rungta International Skills University  
**Language:** Python 3 (Single-File Architecture)  

---

### 1. ABSTRACT
This document details the engineering specifications, architectural design, mathematical modeling, and rigorous test results of a two-player console Tic-Tac-Toe system. Developed under strict Senior Engineering guidelines, the complete program is delivered as an isolated, zero-dependency single Python file (`tic_tac_toe.py`). The application enforces strict typing conventions, explicit conditional logic for 8 winning paths, collision safety, robust error containment, and an integrated self-verification harness.

---

### 2. ARCHITECTURAL DECISIONS (SENIOR ENGINEERING STANDARD)
1. **Zero External Dependencies:** Implemented exclusively with Python 3 Standard Library primitives to guarantee portability and fast execution across any operating system.
2. **Strict Single-File Constraint:** Fulfills Problem Statement 56 Requirement 1 (*"Write the solution in Python 3 (one .py file) and run it from the console"*). All runtime routines, game loops, and test harnesses are self-contained.
3. **Type Safety & Static Typing:** Decorated with explicit Python type annotations (`typing.List`, `typing.Tuple`, `typing.Optional`) preventing runtime type coercion bugs.
4. **Input Sanitization & Buffer Clearing:** Handles input strings defensively, stripping UTF-8 Byte Order Marks (`\ufeff`) and leading/trailing whitespace, and providing clean recovery for `KeyboardInterrupt` / `EOFError`.
5. **State Invariance:** Board state is managed as a fixed-size 9-element list initialized to empty space delimiters, guaranteeing O(1) cell lookup and O(1) state updates.

---

### 3. FORMAL SPECIFICATIONS & FUNCTIONS

| Function Signature | Domain Responsibility | Algorithmic Complexity |
| :--- | :--- | :--- |
| `display_board(board: List[str]) -> None` | Renders the 3x3 ASCII grid | Time: O(1), Space: O(1) |
| `display_guide() -> None` | Displays position map (1 through 9) | Time: O(1), Space: O(1) |
| `check_win(board: List[str], player: str) -> Tuple[bool, Optional[str]]` | Evaluates all 8 winning lines via explicit conditions | Time: O(1), Space: O(1) |
| `check_draw(board: List[str]) -> bool` | Validates board saturation | Time: O(1), Space: O(1) |
| `take_move(board: List[str], player: str) -> int` | Validates range, type, and cell vacancy | Time: O(1) per attempt |
| `play_game() -> None` | Orchestrates a single match round | Time: O(1) total moves <= 9 |
| `play_interactive_session() -> None` | Manages session replay loops (`y/n`) | Dynamic session loop |
| `run_self_tests() -> None` | Built-in verification executing all 4 test cases | Deterministic test runner |

---

### 4. WINNING COMBINATIONS TRUTH TABLE

```
  Rows:                 Columns:               Diagonals:
  [0, 1, 2] -> 1-2-3    [0, 3, 6] -> 1-4-7     [0, 4, 8] -> 1-5-9
  [3, 4, 5] -> 4-5-6    [1, 4, 7] -> 2-5-8     [2, 4, 6] -> 3-5-7
  [6, 7, 8] -> 7-8-9    [2, 5, 8] -> 3-6-9
```

---

### 5. VERIFICATION & TEST MATRIX

All 4 test cases mandated by Problem Statement 56 were executed directly via `python tic_tac_toe.py --test`:

```text
--- Running Built-in Senior Verification Suite (4 Test Cases) ---
  [PASS] Test Case 1: Normal Input (Player X Wins 1-2-3)
  [PASS] Test Case 2: Boundary Draw (Full 9 Moves)
  [PASS] Test Case 3: Validation & Collision Handling
  [PASS] Test Case 4: Alternate Scenario (Player O Wins 4-5-6)

All 4 Test Cases Successfully Verified! Status: 100% PASSED
```

---

### 6. CONCLUSION
The developed single-file solution represents an optimal balance between academic compliance and senior-level software engineering quality. All functional criteria, validation behaviors, and documentation deliverables are completely satisfied.
