"""
You are given K eggs, and you have access to a building with N floors from 1 to N.

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break,
and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is,
regardless of the initial value of F?



Example 1:

Input:
    K = 1, N = 2
Output:
    2
Explanation:
    Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
    Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
    If it didn't break, then we know with certainty F = 2.
    Hence, we needed 2 moves in the worst case to know what F is with certainty.

Example 2:

Input:
    K = 2, N = 6
Output:
    3

Example 3:

Input:
    K = 3, N = 14
Output:
    4


Note:

    1 <= K <= 100
    1 <= N <= 10000
"""


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        """
        dp by eggs and moves
        dp[m][k] means m move and k eggs can check floor dp[m][k]
        
        then :
            dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            
            if egg breaks, dp[m - 1][k - 1] # lower
            else: dp[m - 1][k]  # higher
            total: dp[m - 1][k - 1] + 1 + dp[m - 1][k]
        """
        dp = [[0] * (K + 1) for n in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][k] >= N:
                return m
        """
            dp by eggs and floors
            for i in range(1, N / 2 + 4)[::-1]:
               tmp = max(helper(K - 1, i - 1), helper(K, N - i)) + 1
               v = min(v, tmp)
        """
        a, b = range(N + 1), range(N + 1)

        for r in range(2, K + 1):
            c = 2
            i = 1
            while c <= N:
                v = c
                while i < c:
                    if a[i - 1] <= b[c - i]:
                        v = min(v, b[c - i] + 1)
                        i += 1
                    else:
                        break
                b[c] = v
                c += 1
                i -= 1
            a, b = b, range(N + 1)
        return a[-1]


examples = [
    {
        "input": {
            "K": 1,
            "N": 2
        },
        "output": 2
    }, {
        "input": {
            "K": 2,
            "N": 6
        },
        "output": 3
    }, {
        "input": {
            "K": 3,
            "N": 14
        },
        "output": 4
    }, {
        "input": {
            "K": 4,
            "N": 2000
        },
        "output": 16
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