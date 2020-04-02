"""
Given a string s.
In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.


Example 1:

Input:
    s = "zzazz"
Output:
    0
Explanation:
    The string "zzazz" is already palindrome we don't need any insertions.

Example 2:

Input:
    s = "mbadm"
Output:
    2
Explanation:
    String can be "mbdadbm" or "mdbabdm".

Example 3:

Input:
    s = "leetcode"
Output:
    5
Explanation:
    Inserting 5 characters the string becomes "leetcodocteel".

Example 4:
Input:
    s = "g"
Output:
    0

Example 5:

Input:
    s = "no"
Output:
    1

Constraints:

    1 <= s.length <= 500
    All characters of s are lower case English letters.
"""


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # dp[l][r]:
        # if s[l] == s[r]: dp[l][r] = dp[l + 1][r - 1] + 2
        # else:
        # dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                ll, rr = i, i + l - 1
                if s[ll] == s[rr]:
                    if ll == rr + 1:
                        dp[ll][rr] = 2
                    else:
                        dp[ll][rr] = dp[ll + 1][rr - 1] + 2
                else:
                    dp[ll][rr] = max(dp[ll + 1][rr], dp[ll][rr - 1])
        return n - dp[0][-1]


examples = [
    {
        "input": {
            "s": "zzazz",
        },
        "output": 0
    }, {
        "input": {
            "s": "mbadm",
        },
        "output": 2
    }, {
        "input": {
            "s": "leetcode",
        },
        "output": 5
    }, {
        "input": {
            "s": "g",
        },
        "output": 0
    }, {
        "input": {
            "s": "no",
        },
        "output": 1
    }, {
        "input": {
            "s": "zjveiiwvc",
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
