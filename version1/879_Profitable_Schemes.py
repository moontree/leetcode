"""
There are G people in a gang, and a list of various crimes they could commit.

The i-th crime generates a profit[i] and requires group[i] gang members to participate.

If a gang member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least P profit,
and the total number of gang members participating in that subset of crimes is at most G.

How many schemes can be chosen?
Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input:
    G = 5, P = 3, group = [2,2], profit = [2,3]
Output:
    2
Explanation:
    To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
    In total, there are 2 schemes.

Example 2:

Input:
    G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output:
    7
Explanation:
    To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
    There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

Note:

    1 <= G <= 100
    0 <= P <= 100
    1 <= group[i] <= 100
    0 <= profit[i] <= 100
    1 <= group.length = profit.length <= 100
"""


class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(G + 1)] for _ in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            tmp = [row[:] for row in dp]
            for p1 in range(P + 1):
                p2 = min(p1 + p, P)
                for g1 in range(G - g + 1):
                    g2 = g1 + g
                    tmp[p2][g2] += dp[p1][g1]
                    tmp[p2][g2] %= mod
            dp = tmp
        return sum(dp[-1]) % mod


examples = [
    {
        "input": {
            "G": 5,
            "P": 3,
            "group": [2, 2],
            "profit": [2, 3]
        },
        "output": 2
    }, {
        "input": {
            "G": 10,
            "P": 5,
            "group": [2, 3, 5],
            "profit": [6, 7, 8]
        },
        "output": 7
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
