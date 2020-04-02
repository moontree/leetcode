"""
Given a string S, count the number of distinct, non-empty subsequences of S .
Since the result may be large, return the answer modulo 10^9 + 7.

Example 1:
Input:
    "abc"
Output:
    7
Explanation:
    The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:
Input:
    "aba"
Output:
    6
Explanation:
    The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".

Example 3:
Input:
    "aaa"
Output:
    3
Explanation:
    The 3 distinct subsequences are "a", "aa" and "aaa".

Note:
    S contains only lowercase letters.
    1 <= S.length <= 2000
"""


class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(S)
        dp = [1 for _ in range(n + 1)]
        cache = {}
        for i, c in enumerate(S):
            if c not in cache:
                dp[i + 1] = dp[i] * 2
            else:
                dp[i + 1] = 2 * dp[i] - dp[cache[c] - 1]
            dp[i + 1] %= mod
            cache[c] = i + 1
        return (dp[-1] - 1) % mod


examples = [
    {
        "input": {
            "S": "abc",
        },
        "output": 7
    }, {
        "input": {
            "S": "aba",
        },
        "output": 6
    }, {
        "input": {
            "S": "aaa",
        },
        "output": 3
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
