"""
According to the Wikipedia's article:
 "The Game of Life, also known simply as Life,
 is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place?
Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array.
 In principle, the board is infinite,
 which would cause problems when the active area encroaches the border of the array.
 How would you address these problems?
"""


def game_of_life(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def is_valid(r, c):
        return 0 <= r < m and 0 <= c < n
    m, n = len(board), len(board[0])
    for i in xrange(m):
        for j in xrange(n):
            neighbors = 0
            for I in xrange(-1, 2):
                for J in xrange(-1, 2):
                    if is_valid(i + I, j + J):
                        val = board[i + I][j + J]
                        if val > 3:  # next live
                            val = val - 4
                        elif val > 1:  # next die
                            val = val - 2
                        neighbors += val

            neighbors -= board[i][j]
            if neighbors < 2 or neighbors > 3:
                board[i][j] += 2
            elif neighbors == 2:
                if board[i][j] == 1:
                    board[i][j] += 4
                else:
                    board[i][j] += 2
            else:
                board[i][j] += 4
    for i in xrange(m):
        for j in xrange(n):
            if board[i][j] > 3:
                board[i][j] = 1
            else:
                board[i][j] = 0
    for l in board:
        print l


examples = [
    {
        "board": [
            [0, 1, 1, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0]
        ]
    }
]


for example in examples:
    print game_of_life(example["board"])
