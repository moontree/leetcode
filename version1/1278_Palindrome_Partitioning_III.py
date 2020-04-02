"""
=========================
Project -> File: leetcode -> 1278_Palindrome_Partitioning_III.py
Author: zhangchao
=========================
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
Return the minimal number of characters that you need to change to divide the string.



Example 1:

Input:
    s = "abc", k = 2
Output:
    1
Explanation:
    You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2:

Input:
    s = "aabbc", k = 3
Output:
    0
Explanation:
    You can split the string into "aa", "bb" and "c", all of them are palindrome.

Example 3:

Input:
    s = "leetcode", k = 8
Output:
    0

Constraints:

    1 <= k <= s.length <= 100.
    s only contains lowercase English letters.
"""


class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def helper(ss):
            l, r, res = 0, len(ss) - 1, 0
            while l < r:
                if ss[l] != ss[r]:
                    res += 1
                l += 1
                r -= 1
            return res

        n = len(s)
        cache = {}
        for i in range(n + 1):
            for j in range(i, n + 1):
                cache[(i, j)] = helper(s[i: j])

        dp = [[n for _ in range(k + 1)] for _ in range(n + 1)]
        # split s[: i] to kk parts
        for i in range(1, n + 1):
            dp[i][1] = helper(s[: i])
            for kk in range(2, k + 1):
                if i == kk:  # 0 to i, i + 1 parts
                    dp[i][kk] = 0
                elif i + 1 < kk:  # i + 1 < kk: impossible
                    continue
                else:  # last part, last part can start from kk - 1
                    for j in range(kk - 1, i + 1):
                        dp[i][kk] = min(dp[i][kk], dp[j][kk - 1] + cache[(j, i)])

        return dp[-1][-1]


examples = [
    {
        "input": {
            "s": "abc",
            "k": 2
        },
        "output": 1
    }, {
        "input": {
            "s": "aabbc",
            "k": 3
        },
        "output": 0
    }, {
        "input": {
            "s": "leetcode",
            "k": 8
        },
        "output": 0
    }, {
        "input": {
            "s": "uyskbebqrhfoythvwazswib",
            "k": 2
        },
        "output": 9
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
