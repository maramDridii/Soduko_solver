import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def solve_sudoku(grid):
    M = 9

    def solve(grid, row, col, num):
        for x in range(M):
            if grid[row][x] == num:
                return False

        for x in range(M):
            if grid[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def suduko(grid, row, col):
        if row == M - 1 and col == M:
            return True
        if col == M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return suduko(grid, row, col + 1)
        for num in range(1, M + 1, 1):
            if solve(grid, row, col, num):
                grid[row][col] = num
                if suduko(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    if suduko(grid, 0, 0):
        return grid
    else:
        return None

def display_sudoku(grid):
    for i in range(9):
        for j in range(9):
            cell_value = grid[i][j]
            if cell_value == 0:
                cell_value_str = " "
            else:
                cell_value_str = str(cell_value)
            label = tk.Label(root, text=cell_value_str, width=4, height=2, relief=tk.RIDGE)
            label.grid(row=i, column=j)

def start_game():
    input_grid = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = entry_grid[i][j].get()
            if cell_value.isdigit():
                row.append(int(cell_value))
            else:
                row.append(0)
        input_grid.append(row)

    solution = solve_sudoku(input_grid)
    if solution:
        display_sudoku(solution)
    else:
        messagebox.showerror("Error", "No solution exists for this puzzle.")



root = tk.Tk()
root.title("Sudoku Game")

entry_grid = []
for i in range(9):
    row = []
    for j in range(9):
        entry = ttk.Entry(root, width=4, justify="center")
        entry.grid(row=i, column=j)
        row.append(entry)
    entry_grid.append(row)

solve_button = ttk.Button(root, text="Solve", command=start_game)
solve_button.grid(row=9, column=0, columnspan=9)

root.mainloop()







