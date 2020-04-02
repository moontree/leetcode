"""
On an N x N board, the numbers from 1 to N*N are written boustrophedonically
starting from the bottom left of the board,
and alternating direction each row.  For example, for a 6 x 6 board,
the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).
Each move, starting from square x, consists of the following:

36 35 34 33 32 31
25 26 27 28 29 30
24 23 22 21 20 19
13 14 15 16 17 18
12 11 10  9  8  7
 1  2  3  4  5  6
 
You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll:
ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.
Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.
The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move:
if the destination to a snake or ladder is the start of another snake or ladder,
you do not continue moving.
(For example,
if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`,
then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.


Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output:
4
Explanation:
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and N*N or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number N*N has no snake or ladder.
"""


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        skip = {}
        N = len(board)
        nums = N ** 2
        for i in range(nums):
            r, c = divmod(i, N)
            if r % 2 == N % 2:
                start = nums - N * r
                flag = -1
            else:
                start = nums - N + 1 - N * r
                flag = 1
            vv = start + flag * c
            if board[r][c] != -1:
                skip[vv] = board[r][c]
        q = [[1, 0]]

        meet = {1: 0}
        while q:
            idx, _step = q.pop(0)

            for i in range(1, 7):
                v = idx + i
                if v in skip:
                    v = skip[v]
                step = _step + 1
                if v <= nums and (v not in meet):
                    meet[v] = step
                    q.append([v, step])

        return meet.get(nums, -1)


examples = [
    {
        "input": {
            "board": [
                [-1, -1, -1, -1, -1, -1], 
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1], 
                [-1, 35, -1, -1, 13, -1], 
                [-1, -1, -1, -1, -1, -1], 
                [-1, 15, -1, -1, -1, -1]
            ],
        },
        "output": 4
    }, {
        "input": {
            "board": [
                [-1, -1],
                [-1, 3],
            ],
        },
        "output": 1
    }, {
        "input": {
            "board": [[-1,-1,-1],[-1,9,8],[-1,8,9]]
        },
        "output": 1
    }, {
        "input": {
            "board": [[-1,7,-1],[-1,6,9],[-1,-1,2]]
        },
        "output": 1
    }, {
        "input": {
            "board": [[1,1,-1],[1,1,1],[-1,1,1]]
        },
        "output": -1
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