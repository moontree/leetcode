"""
Alex and Lee continue their games with piles of stones.
There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.



Example 1:

Input:
    piles = [2,7,9,4,4]
Output:
    10
Explanation:
    If Alex takes one pile at the beginning, Lee takes two piles,
    then Alex takes 2 piles again.
    Alex can get 2 + 4 + 4 = 10 piles in total.
    If Alex takes two piles at the beginning, then Lee can take all three piles left.
    In this case, Alex get 2 + 7 = 9 piles in total.
    So we return 10 since it's larger.


Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        cache = {}
        s = [0 for _ in range(n + 1)]
        for i in range(n):
            s[i] = s[i - 1] + piles[i]

        def helper(i, m):  # start from i, m is m
            mx = 2 * m
            if mx >= (n - i):
                cache[(i, m)] = s[-2] - s[i - 1]
                return cache[(i, m)]
            else:
                res = 0
                if (i, m) not in cache:
                    for j in range(1, mx + 1): # choose 1 and x
                        r = i + j  # [l, r) s[-2] - s[l - 1] - helper(r, m)
                        mr = max(m, j)
                        if (r, mr) not in cache:
                            cache[(r, mr)] = helper(r, mr)
                        res = max(res, s[-2] - s[i - 1] - cache[(r, mr)])
                    cache[(i, m)] = res
                return cache[(i, m)]
        v = helper(0, 1)
        print cache
        return v


examples = [
    {
        "input": {
            "piles": [2, 7, 9, 4, 4],
        },
        "output": 10
    }, {
        "input": {
            "piles": [8, 6, 9, 1, 7, 9],
        },
        "output": 25
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
