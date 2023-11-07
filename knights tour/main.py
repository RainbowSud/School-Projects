import random
import time

# 2d list to represent the board
# 0 - empty (unvisited)
# positive integer - step number

DIM = 4
I = 0
J = 0

def printBoard(board):
    print("\n\n\n\n\n")
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                print(" .", end=" ")
            else:
                print(format(board[i][j], "2.0f"), end=" ")
        print()
    print()

def setup(board):
    for i in range(0, DIM):
        board.append([])
        for j in range(0, DIM):
            board[i].append(0)

def knight(board, i, j, num):
    if num > DIM*DIM:return True
    if i < 0: return False
    if j < 0: return False
    if i >= DIM: return False
    if j >= DIM: return False
    if board[i][j] != 0: return False

    board[i][j] = num

    if knight(board, i + 1, j + 2, num+1): return True
    if knight(board, i + 1, j - 2, num+1): return True
    if knight(board, i - 1, j + 2, num+1): return True
    if knight(board, i - 1, j - 2, num+1): return True
    if knight(board, i + 2, j + 1, num+1): return True
    if knight(board, i + 2, j - 1, num+1): return True
    if knight(board, i - 2, j + 1, num+1): return True
    if knight(board, i - 2, j - 1, num+1): return True

    board[i][j] = 0
    printBoard(board)
    time.sleep(0.1)

    return False





def main():
    board = []
    setup(board)
    knight(board, I, J, 1)
    printBoard(board)





main()

