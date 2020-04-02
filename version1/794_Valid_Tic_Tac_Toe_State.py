"""
A Tic-Tac-Toe board is given as a string array board.
Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array,
and consists of characters " ", "X", and "O".
The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").

The first player always places "X" characters,
while the second player always places "O" characters.

"X" and "O" characters are always placed into empty squares, never filled ones.

The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Example 1:
Input:
    board = ["O  ", "   ", "   "]
Output:
    false
Explanation:
    The first player always plays "X".

Example 2:
Input:
    board = ["XOX", " X ", "   "]
Output:
    false
Explanation:
    Players take turns making moves.

Example 3:
Input:
    board = ["XXX", "   ", "OOO"]
Output:
    false

Example 4:
Input:
    board = ["XOX", "O O", "XOX"]
Output:
    true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""


class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def valid(c):
            for row in board:
                if row == c * 3:
                    return True
            for j in range(3):
                if board[0][j] == board[1][j] == board[2][j] == c:
                    return True
            if board[0][0] == board[1][1] == board[2][2] == c:
                return True
            if board[0][2] == board[1][1] == board[2][0] == c:
                return True
            return False

        xc, oc = 0, 0
        for row in board:
            for c in row:
                if c == 'X':
                    xc += 1
                elif c == 'O':
                    oc += 1
        if oc > xc or oc < xc - 1:
            return False
        xv, ov = valid('X'), valid('O')
        if xv and xc == oc:
            return False
        if ov and xc > oc:
            return False
        return True



examples = [
    {
        "input": {
            "board": [
                'O  ',
                '   ',
                '   '
            ],
        },
        "output": False
    }, {
        "input": {
            "board": [
                'O  ',
                '   ',
                '   '
            ],
        },
        "output": False
    }, {
        "input": {
            "board": [
                'XXX',
                '   ',
                'OOO'
            ],
        },
        "output": False
    }, {
        "input": {
            "board": [
                'XOX',
                'O O',
                'XOX'
            ],
        },
        "output": True
    }, {
        "input": {
            "board": [
                'XOX',
                ' O ',
                'XOX'
            ],
        },
        "output": False
    }, {
        "input": {
            "board": [
                'XOX',
                'X  ',
                '   '
            ],
        },
        "output": False
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']
