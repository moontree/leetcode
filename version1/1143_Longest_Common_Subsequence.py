"""
Given two strings text1 and text2,
return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none)
deleted without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.


Example 1:

Input:
    text1 = "abcde", text2 = "ace"
Output:
    3
Explanation:
    The longest common subsequence is "ace" and its length is 3.

Example 2:

Input:
    text1 = "abc", text2 = "abc"
Output:
    3
Explanation:
    The longest common subsequence is "abc" and its length is 3.

Example 3:

Input:
    text1 = "abc", text2 = "def"
Output:
    0
Explanation:
    There is no such common subsequence, so the result is 0.

Constraints:
    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    The input strings consist of lowercase English characters only.
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1, l2 = len(text1), len(text2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-2][-2]


examples = [
    {
        "input": {
            "text1": "abcde",
            "text2": "ace"
        },
        "output": 3
    }, {
        "input": {
            "text1": "abc",
            "text2": "abc"
        },
        "output": 3
    }, {
        "input": {
            "text1": "abc",
            "text2": "def"
        },
        "output": 0
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
