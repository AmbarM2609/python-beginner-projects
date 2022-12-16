def solve(board):
  # find an empty cell
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        # try every number from 1 to 9
        for n in range(1, 10):
          # if the number is valid for the current cell, place it and recursively try to solve the rest of the board
          if is_valid(board, i, j, n):
            board[i][j] = n
            if solve(board):
              return True
            # if it leads to an invalid solution, backtrack and try the next number
            board[i][j] = 0
        # if no number works, return False to trigger backtracking
        return False
  # if the board is full, it is a valid solution
  return True

def is_valid(board, row, col, num):
  # check if the number is already used in the row
  if num in board[row]:
    return False
  # check if the number is already used in the column
  if num in [board[i][col] for i in range(9)]:
    return False
  # check if the number is already used in the 3x3 block
  block_row = (row // 3) * 3
  block_col = (col // 3) * 3
  for i in range(3):
    for j in range(3):
      if board[block_row + i][block_col + j] == num:
        return False
  # if the number is not used in the row, column, or block, it is valid
  return True

# test the solver with a sample board
board = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(board):
  for row in board:
    print(row)
else:
  print("No solution found.")
