"""
=========================
Project -> File: leetcode -> 1301_Number_of_Paths_with_Max_Score.py
Author: zhangchao
=========================
You are given a square board of characters.
You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'.
The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'.
In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers:
the first integer is the maximum sum of numeric characters you can collect,
and the second is the number of such paths
that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

Example 1:

Input:
    board = ["E23","2X2","12S"]
Output:
    [7,1]

Example 2:

Input:
    board = ["E12","1X1","21S"]
Output:
    [4,2]

Example 3:

Input:
    board = ["E11","XXX","11S"]
Output:
    [0,0]


Constraints:

    2 <= board.length == board[i].length <= 100
"""


class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        base = 10 ** 9 + 7
        r, c = len(board), len(board[0])
        dp = [[[0, 1] for _ in range(c)] for _ in range(r)]
        # score, ways
        for i in range(r - 1)[::-1]:
            if board[i][-1] == 'X':
                dp[i][-1] = [0, 0]
            else:
                score, way = dp[i + 1][-1]
                dp[i][-1] = [score + int(board[i][-1]), 1] if way == 1 else [0, 0]
        for j in range(c - 1)[::-1]:
            if board[-1][j] == 'X':
                dp[-1][j] = [0, 0]
            else:
                score, way = dp[-1][j + 1]
                dp[-1][j] = [score + int(board[-1][j]), 1] if way == 1 else [0, 0]
        # for row in dp:
        #     print row
        for i in range(r - 1)[::-1]:
            for j in range(c - 1)[::-1]:
                if board[i][j] == 'X':
                    dp[i][j] = [0, 0]
                    continue
                pairs = [dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1]]
                pairs = [v for v in pairs if v[0] or board[i + 1][j + 1] == 'S']
                if not pairs:
                    dp[i][j] = [0, 0]
                    continue
                score = max([v[0] for v in pairs])
                way = 0
                for v in pairs:
                    if v[0] == score:
                        way += v[1]
                score += int(board[i][j]) if board[i][j] != 'E' else 0
                dp[i][j] = [score, way]
        res = [v % base for v in dp[0][0]]
        return res


examples = [
    {
        "input": {
            "board": [
                "E23",
                "2X2",
                "12S"
            ],
        },
        "output": [7, 1]
    }, {
        "input": {
            "board": ["E12", "1X1", "21S"],
        },
        "output": [4, 2]
    }, {
        "input": {
            "board": ["E11", "XXX", "11S"],
        },
        "output": [0, 0]
    }, {
        "input": {
            "board": ["EX", "XS"],
        },
        "output": [0, 1]
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
