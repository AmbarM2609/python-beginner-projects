board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
  print("  0 1 2")
  for i, row in enumerate(board):
    print(i, *row)

def make_move(player):
  while True:
    try:
      row = int(input("Enter row (0, 1, or 2): "))
      col = int(input("Enter column (0, 1, or 2): "))
      if row in [0, 1, 2] and col in [0, 1, 2]:
        if board[row][col] == " ":
          board[row][col] = player
          return
        else:
          print("That space is already occupied. Try again.")
      else:
        print("Invalid input. Try again.")
    except ValueError:
      print("Invalid input. Try again.")

def game_won(player):
  # check rows
  for row in board:
    if row == [player, player, player]:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  # check diagonals
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def game_tied():
  for row in board:
    if " " in row:
      return False
  return True

print("Welcome to Tic-Tac-Toe!")

while True:
  draw_board()
  make_move("X")
  if game_won("X"):
    print("X wins!")
    break
  if game_tied():
    print("It's a tie!")
    break
  draw_board()
  make_move("O")
  if game_won("O"):
    print("O wins!")
    break
  if game_tied():
    print("It's a tie!")
    break
