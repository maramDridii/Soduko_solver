M = 9


def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True





def Suduko(grid, row, col):

    # Base case 1: If we have reached the last row and last column, the puzzle is solved.
    if (row == M - 1 and col == M):
        return True

    # Base case 2: If we have reached the end of a row, move to the next row and start from the first column.
    if col == M:
        row += 1
        col = 0

    # If the cell is already filled, move to the next cell.
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)

    # Try filling the cell with numbers from 1 to 9 and check if it is a valid move.
    for num in range(1, M + 1, 1):

        if solve(grid, row, col, num):

            # If the number is valid, fill the cell with the number and proceed to the next cell.
            grid[row][col] = num

            # Recursively call Suduko function on the next cell.
            if Suduko(grid, row, col + 1):
                return True

        # If the number is not valid or the puzzle cannot be solved with the current number,
        # reset the cell to 0 (undoing the choice) and try the next number in the loop.
        grid[row][col] = 0

    # If no number from 1 to 9 leads to a solution, backtrack to the previous cell and try a different number.
    return False







'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]
grid_easy = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]
grid_medium = [
    [3, 0, 0, 8, 0, 0, 0, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 8, 0, 3, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]
grid_hard = [
    [0, 0, 0, 0, 0, 0, 6, 8, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 9],
    [3, 0, 9, 0, 0, 0, 0, 4, 5],
    [4, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 9, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [9, 6, 0, 0, 0, 0, 3, 0, 8],
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [0, 2, 8, 0, 0, 0, 0, 0, 0]
]
grid_expert = [
    [0, 9, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 6, 0, 0, 3, 0, 9, 0],
    [7, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [8, 0, 1, 0, 0, 0, 0, 0, 2],
    [4, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0]
]


if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")