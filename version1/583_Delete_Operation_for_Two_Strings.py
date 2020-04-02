"""
Given two words word1 and word2,
find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.

Example 1:
Input:
    "sea", "eat"
Output:
    2
Explanation:
    You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
    The length of given words won't exceed 500.
    Characters in given words can only be lower-case letters.
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        dp[0] = range(l2 + 1)
        for i in range(1, l1 + 1):
            dp[i][0] = i
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + 1
        return dp[-1][-1]


examples = [
    {
        "input": {
            "word1": "sea",
            "word2": "eat"
        },
        "output": 2
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
