# Sudoku 9x9 Solver with Python
## Description:

This project consists of a 9×9 Sudoku solver implemented in Python,
using a backtracking algorithm that recursively traverses the board
until a valid solution is found.

The solver was developed as the final project for the CS50P course
by Pedro Henrique Abreu Adorno.


### Algorithm

The solver uses a classic **backtracking approach**:

1. Find an empty cell in the Sudoku grid;
2. Try inserting numbers from 1 to 9;
3. Check whether the number satisfies Sudoku constraints:
   - Unique in the row
   - Unique in the column
   - Unique in the 3×3 subgrid
4. If valid, move to the next empty cell recursively;
5. If no number works, backtrack and try a different number.

This process continues until the puzzle is solved.

### Example

Example of an input Sudoku board:

```text
53##7####
6##195###
#98####6#
8###6###3
4##8#3##1
7###2###6
#6####28#
###419##5
####8##79
```

Solution produced by the solver:

```text
534678912
672195348
198342567
859761423
426853791
713924856
961537284
287419635
345286179
```

## How to run

Make sure you have Python 3 installed, then run:

```bash
python solver.py
