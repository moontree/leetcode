"""
On an alphabet board,
we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"],
as shown in the diagram below.


We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
You may return any path that does so.



Example 1:

Input:
    target = "leet"
Output:
    "DDR!UURRR!!DDD!"

Example 2:

Input:
    target = "code"
Output:
    "RR!DDRR!UUL!R!"



Constraints:

    1 <= target.length <= 100
    target consists only of English lowercase letters.
"""


class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        cache = {}
        for i in range(6):
            for j in range(len(board[i])):
                cache[board[i][j]] = [i, j]

        def helper(a, b):
            lr, ud = '', ''
            if a[1] < b[1]:
                lr += 'R' * (b[1] - a[1])
            else:
                lr += 'L' * (a[1] - b[1])
            if a[0] < b[0]:
                ud += 'D' * (b[0] - a[0])
            else:
                ud += 'U' * (a[0] - b[0])
            if lr and lr[0] == 'L':
                return lr + ud
            if ud and ud[0] == 'U':
                return ud + lr
            return lr + ud

        res = ""
        cur = 'a'
        for v in target:
            res += helper(cache[cur], cache[v]) + '!'
            cur = v
        return res


examples = [
    {
        "input": {
            "target": "leet",
        },
        "output": "DDR!UURRR!!DDD!"
    }, {
        "input": {
            "target": "code",
        },
        "output": "RR!DDRR!UUL!R!"
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
