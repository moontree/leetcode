"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""


def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if len(board) == 0:
        return
    m, n = len(board), len(board[0])
    for i in range(m):
        if board[i][0] == 'O':
            find_o(board, i, 0)
        if board[i][n - 1] == 'O':
            find_o(board, i, n - 1)
    for j in range(n):
        if board[0][j] == 'O':
            find_o(board, 0, j)
        if board[m - 1][j] == 'O':
            find_o(board, m - 1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == '*':
                board[i][j] = 'O'


def find_o(board, i, j):
    board[i][j] = '*'
    if valid(board, i - 1, j) and board[i - 1][j] == 'O':
        find_o(board, i - 1, j)
    if valid(board, i + 1, j) and board[i + 1][j] == 'O':
        find_o(board, i + 1, j)
    if valid(board, i, j - 1) and board[i][j - 1] == 'O':
        find_o(board, i, j - 1)
    if valid(board, i, j + 1) and board[i][j + 1] == 'O':
        find_o(board, i, j + 1)


def valid(board, i, j):
    m, n = len(board), len(board[0])
    if 0 <= i < m and 0 <= j < n:
        return True
    return False


examples = [
    {
        "board": [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O'],
        ]
    }
]


for example in examples:
    solve(example["board"])
    print example["board"]
