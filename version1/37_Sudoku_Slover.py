'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


'''



examples = [
    {
        "board" : [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    }
]
import numpy as np
row_group = np.zeros([9, 10])
col_group = np.zeros([9, 10])
box_group = np.zeros([3, 3, 10])

def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            c = board[i][j]
            if c != '.':
                row_group[i][int(c)] = 1
                col_group[j][int(c)] = 1
                box_group[i / 3][j / 3][int(c)] = 1
    if tryIndex(board, 0):
        return board

def tryIndex(board, index):
    if index > 80:
        return True
    else:
        i = index / 9
        j = index % 9
        if board[i][j] != '.':
            return tryIndex(board, index + 1)
        else:
            for k in range(1, 10):
                if row_group[i][k] or col_group[j][k] or box_group[i/3][j/3][k]:
                    continue
                else:
                    board[i][j] = str(k)
                    row_group[i][k] = 1
                    col_group[j][k] = 1
                    box_group[i / 3][j / 3][k] = 1
                    if tryIndex(board, index + 1):
                        return True
                    else:
                        board[i][j] = '.'
                        row_group[i][k] = 0
                        col_group[j][k] = 0
                        box_group[i / 3][j / 3][k] = 0
            # board[i][j] = '.'
            return False


for example in examples:
    print solveSudoku(example['board'])