"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved.
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input:
    board = [[1,2,3],[4,0,5]]
Output:
    1
Explanation:
    Swap the 0 and the 5 in one move.

Input:
    board = [[1,2,3],[5,4,0]]
Output:
    -1
Explanation:
    No number of moves will make the board solved.

Input:
    board = [[4,1,2],[5,0,3]]
Output:
    5
Explanation:
    5 is the smallest number of moves that solves the board.
    An example path:
    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]

Input:
    board = [[3,2,4],[1,5,0]]
Output:
    14
Note:

    board will be a 2 x 3 array as described above.
    board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        b = board[0] + board[1]
        cache = {}
        steps = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        cur = -1
        for i in range(6):
            if b[i] == 0:
                cur = i
        step = 0
        target = tuple([1, 2, 3, 4, 5, 0])
        q = [[b, cur]]
        cache[tuple(b)] = 1
        while True:
            tmp = []
            for b, cur in q:
                if tuple(b) == target:
                    return step
                for nx in steps[cur]:
                    nb = b[:]
                    nb[nx], nb[cur] = nb[cur], nb[nx]
                    nxt = tuple(nb)
                    if nxt not in cache:
                        tmp.append([nb, nx])
                        cache[nxt] = True
            q = tmp
            if not q:
                break
            step += 1
        return -1


examples = [
    {
        "input": {
            "board": [
                [1, 2, 3],
                [4, 0, 5]
            ]
        },
        "output": 1
    }, {
        "input": {
            "board": [
                [1, 2, 3],
                [5, 4, 0]
            ]
        },
        "output": -1
    }, {
        "input": {
            "board": [
                [4, 1, 2],
                [5, 0, 3]
            ]
        },
        "output": 5
    }, {
        "input": {
            "board": [
                [3, 2, 4],
                [1, 5, 0]
            ]
        },
        "output": 14
    }
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
