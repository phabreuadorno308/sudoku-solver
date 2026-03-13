import sys


def main():
    # Welcome!
    print(f"Welcome!\nWrite your Sudoku's 9x9 board below. For any blank space, write '#'.\nAfter each line, press enter:")

    # Check user's input
    board = get_sudoku()
    if not validate_sudoku(board):
        sys.exit("Invalid Sudoku's board. Try again")

    # Sudoku's solver
    state, solved_board = solver(board)
    if state:
        print("Finished! Here's the solution:")
        for row in solved_board:
            print(row)
    else:
        print("Sudoku impossible to solve")


def check_repetition(iterable):
    for value in iterable:
        value = value.replace("#", "")
        for number in value:
            if value.count(number) > 1:
                return False
    return True


def get_sudoku():
    board = []
    # Get each line
    for _ in range(9):
        # Validate lenght and numbers written
        while True:
            row = input()
            if len(row) != 9:
                print("Invalid row. Write again")
            else:
                valid = True
                for number in row:
                    if not number in "123456789#":
                        valid = False
                if valid:
                    board.append(row)
                    break
                else:
                    print("Invalid row. Write again")
    return board


def validate_sudoku(board):
    # Validate lines (check repetition)
    if not check_repetition(board):
        return False

    # Validate columns (check repetition)
    columns = []
    for i in range(9):
        column = ""
        for row in board:
            column += row[i]
        columns.append(column)

    if not check_repetition(columns):
        return False

    # Validate blocks (check repetition)
    blocks = []
    for i in [0, 3, 6]:
        make_blocks = ["", "", ""]
        for j in range(3):
            for k in range(3):
                make_blocks[k] += board[i + j][k*3:((k+1)*3)]
        blocks.extend(make_blocks)

    if not check_repetition(blocks):
        return False

    # All right
    return True


def solver(board):
    # Find empty space
    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == "#":
                    return i, j
        return None

    # Backtracking
    def backtrack(board):
        empty = find_empty(board)

        if not empty:
            return True, board

        row, column = empty

        for number in "123456789":
            # Create new line (with number instead of #)
            new_row = board[row][:column] + number + board[row][column+1:]

            # Copy original board to not destroy actual state
            new_board = board.copy()
            new_board[row] = new_row

            # Validate Sudoku
            if validate_sudoku(new_board):
                solved, result = backtrack(new_board)
                if solved:
                    return True, result

        return False, board

    return backtrack(board)


if __name__ == "__main__":
    main()
