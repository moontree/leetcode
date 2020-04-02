"""
On an 8 x 8 chessboard,
there is one white rook.
There also may be empty squares, white bishops, and black pawns.
These are given as characters 'R', '.', 'B', and 'p' respectively.
Uppercase characters represent white pieces,
and lowercase characters represent black pieces.

The rook moves as in the rules of Chess:
it chooses one of four cardinal directions (north, east, west, and south),
then moves in that direction until it chooses to stop,
reaches the edge of the board,
or captures an opposite colored pawn by moving to the same square it occupies.
Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.


Example 1:

Input: [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
Output:
    3
Explanation:
    In this example the rook is able to capture all the pawns.

Example 2:

Input: [
        [".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
Output:
    0
Explanation:
    Bishops are blocking the rook to capture any pawn.

Example 3:

Input: [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
Output:
    3
Explanation:
    The rook can capture the pawns at positions b5, d6 and f5.

Note:
    board.length == board[i].length == 8
    board[i][j] is either 'R', '.', 'B', or 'p'
    There is exactly one cell with board[i][j] == 'R'
"""


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        si, sj = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    si, sj = i, j
        res = 0
        for j in range(sj + 1, 8):
            if board[si][j] == 'p':
                res += 1
                break
            if board[si][j] == 'B':
                break
        for j in range(sj)[::-1]:
            if board[si][j] == 'p':
                res += 1
                break
            if board[si][j] == 'B':
                break
        for i in range(si)[::-1]:
            if board[i][sj] == 'p':
                res += 1
                break
            if board[i][sj] == 'B':
                break
        for i in range(si + 1, 8):
            if board[i][sj] == 'p':
                res += 1
                break
            if board[i][sj] == 'B':
                break
        return res


examples = [
    {
        "input": {
            "board": [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", "R", ".", ".", ".", "p"],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."]
            ],
        },
        "output": 3
    }, {
        "input": {
            "board": [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "p", "p", "p", "p", "p", ".", "."],
                [".", "p", "p", "B", "p", "p", ".", "."],
                [".", "p", "B", "R", "B", "p", ".", "."],
                [".", "p", "p", "B", "p", "p", ".", "."],
                [".", "p", "p", "p", "p", "p", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."]
            ],
        },
        "output": 0
    }, {
        "input": {
            "board": [
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                ["p", "p", ".", "R", ".", "p", "B", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", "B", ".", ".", ".", "."],
                [".", ".", ".", "p", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."]
            ],
        },
        "output": 3
    },
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
