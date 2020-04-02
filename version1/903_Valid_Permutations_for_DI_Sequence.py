"""
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.



Example 1:

Input:
    "DID"
Output:
    5
Explanation:
    The 5 valid permutations of (0, 1, 2, 3) are:
    (1, 0, 3, 2)
    (2, 0, 3, 1)
    (2, 1, 3, 0)
    (3, 0, 2, 1)
    (3, 1, 2, 0)


Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.
"""


class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S) + 1

        mod = 10 ** 9 + 7
        q = [1 for _ in range(n)]

        for i in range(1, n):  # i is max_num
            c, tmp = S[i - 1], [0 for _ in range(n)]
            if c == 'I':
                for j in range(1, i + 1):  # j is last num
                    for k in range(j):  # previous can be 0 to j - 1
                        tmp[j] += q[k]
                    tmp[j] %= mod
            else:
                for j in range(i):  # j is last num
                    for k in range(j, i):  # previous can be j to i - 1
                        tmp[j] += q[k]
                    tmp[j] %= mod
            q = tmp
        return sum(q) % mod
        # n = len(S) + 1
        # # dp[i][j]: len(s) == i and last num is j
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        #
        # mod = 10 ** 9 + 7
        # dp[0] = [1 for _ in range(n)]
        #
        # for i in range(1, n):  # i is max_num
        #     c = S[i - 1]
        #     if c == 'I':
        #         for j in range(1, i + 1):  # j is last num
        #             for k in range(j):  # previous can be 0 to j - 1
        #                 dp[i][j] += dp[i - 1][k]
        #                 dp[i][j] %= mod
        #     else:
        #         for j in range(i):  # j is last num
        #             for k in range(j, i):  # previous can be j to i - 1
        #                 dp[i][j] += dp[i - 1][k]
        #                 dp[i][j] %= mod
        # return sum(dp[-1]) % mod


examples = [
    {
        "input": {
            "S": "DID",
        },
        "output": 5
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
