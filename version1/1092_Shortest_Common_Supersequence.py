"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)



Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.


Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""


class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1, l2 = len(str1), len(str2)
        dp = [['' for _ in range(l2)] for _ in range(l1)]
        for j in range(l2):
            if str1[0] == str2[j]:
                dp[0][j] = str1[0]
            else:
                dp[0][j] = dp[0][j - 1]
        for i in range(l1):
            if str1[i] == str2[0]:
                dp[i][0] = str2[0]
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, l1):
            for j in range(1, l2):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        lcs = dp[-1][-1]
        for row in dp:
            print row
        res = ''
        i, j, k = 0, 0, 0
        while i < len(lcs) and j < l1 and k < l2:
            while j < l1 and str1[j] != lcs[i]:
                res += str1[j]
                j += 1
            while k < l2 and str2[k] != lcs[i]:
                res += str2[k]
                k += 1
            res += lcs[i]
            i += 1
            j += 1
            k += 1
        while j < l1:
            res += str1[j]
            j += 1
        while k < l2:
            res += str2[k]
            k += 1
        return res


examples = [
    {
        "input": {
            "str1": "abac",
            "str2": "cab"
        },
        "output": "cabac"
    }, {
        "input": {
            "str1": "bbbaaaba",
            "str2": "bbababbb"
        },
        "output": "bbabaaabbba"
    }, {
        "input": {
            "str1": "bcacaaab",
            "str2": "bbabaccc"
        },
        "output": "bbabacacaaabc"
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

