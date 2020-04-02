"""
Think about Zuma Game. You have a row of balls on the table,
colored red(R), yellow(Y), blue(B), green(G), and white(W).
 You also have several balls in your hand.

Each time, you may choose a ball in your hand,
and insert it into the row (including the leftmost place and rightmost place).
Then, if there is a group of 3 or more balls in the same color touching,
remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table.
 If you cannot remove all the balls, output -1.

Examples:

Input:
    "WRRBBW", "RB"
Output:
    -1
Explanation:
    WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input:
    "WWRRBBWW", "WRBRW"
Output:
    2
Explanation:
    WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:
    "G", "GGGGG"
Output:
    2
Explanation:
    G -> G[G] -> GG[G] -> empty

Input:
    "RBYYBBRRB", "YRBGB"
Output:
    3
Explanation:
    RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty
"""
import json

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        self.res = 7

        def remove(s):
            l, r = 0, 0
            while r < len(s):
                if s[r] == s[l]:
                    r += 1
                else:
                    if r - l > 2:
                        s = s[:l] + s[r:]
                        return remove(s)
                    else:
                        l, r = r, r
            if r == len(s) and r - l > 2:
                return s[:l]
            return s

        def dfs(bb, h, used):
            # print bb, h, used
            if used > self.res:
                return
            b = remove(bb)
            if len(b) == 0:
                self.res = min(self.res, used)
            for i in range(len(h)):
                for j in range(len(b)):
                    if b[j] == h[i] and ((j + 1 < len(b) and b[j] != b[j + 1]) or j == len(b) - 1):
                        nb = b[:j + 1] + h[i] + b[j + 1:]
                        hh = h[:i] + h[i + 1:]
                        dfs(nb, hh, used + 1)

        dfs(board, hand, 0)
        if self.res == 7:
            return -1
        return self.res
        # def remove(_arr):
        #     arr = _arr[:]
        #     for i, (c, n) in enumerate(arr):
        #         if n > 2:
        #             if i + 1 < len(arr) and i > 0 and arr[i + 1][0] == arr[i - 1][0]:
        #                 arr[i - 1][1] += arr[i + 1][1]
        #                 arr = arr[: i] + arr[i + 2:]
        #             else:
        #                 arr = arr[: i] + arr[i + 1:]
        #             return remove(arr)
        #     return arr
        #
        # self.res = len(hand) + 1
        # q = []
        # c, n = None, 0
        # for cur in board:
        #     if cur == c:
        #         n += 1
        #     else:
        #         if c is not None:
        #             q.append([c, n])
        #         c, n = cur, 1
        # q.append([c, n])
        #
        # def helper(_arr, h):
        #     arr = remove(_arr)
        #     # print(_arr, arr, h)
        #     if len(arr) == 0:
        #         self.res = min(self.res, len(hand) - len(h))
        #     for i in range(len(arr)):
        #         tmp = [v[:] for v in arr]
        #         for j in range(len(h)):
        #             if tmp[i][0] == h[j]:
        #                 tmp[i][1] += 1
        #                 hh = h[:j] + h[j + 1:]
        #                 helper(tmp, hh)
        #                 tmp[i][1] -= 1
        #                 break
        #
        # helper(q, hand)
        # if self.res > len(hand):
        #     return -1
        # return self.res


examples = [
    {
        "input": {
            "board": "WRRBBW",
            "hand": "RB",
        },
        "output": -1
    }, {
        "input": {
            "board": "WWRRBBWW",
            "hand": "WRBRW",
        },
        "output": 2
    }, {
        "input": {
            "board": "G",
            "hand": "GGGGG",
        },
        "output": 2
    }, {
        "input": {
            "board": "RRWWRRW",
            "hand": "RR",
        },
        "output": 2
    }, {
        "input": {
            "board": "RRWWRRW",
            "hand": "WR",
        },
        "output": -1
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

