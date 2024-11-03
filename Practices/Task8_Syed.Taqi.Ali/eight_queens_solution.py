# Eight Queens using Pipes-and-Filters in Python

def generate_empty_board(size=8):
    return [['.' for _ in range(size)] for _ in range(size)]

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q' or \
           (col - row + i >= 0 and board[i][col - row + i] == 'Q') or \
           (col + row - i < len(board) and board[i][col + row - i] == 'Q'):
            return False
    return True

def place_queens(board, row=0):
    if row == len(board):
        solutions.append([row[:] for row in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            place_queens(board, row + 1)
            board[row][col] = '.'

solutions = []
board = generate_empty_board()
place_queens(board)

for solution in solutions:
    for row in solution:
        print(' '.join(row))
    print()
