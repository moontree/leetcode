"""
=========================
Project -> File: leetcode -> 730_Count_Different_Palindromic_Subsequences.py
Author: zhangchao
=========================
Given a string S,
find the number of different non-empty palindromic subsequences in S,
and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input:
    S = 'bccb'
Output:
    6
Explanation:
    The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
    Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:
Input:
    S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output:
    104860361
Explanation:
    There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:

    The length of S will be in the range [1, 1000].
    Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""


class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """

        def DFS(start, end, mem):
            if (start, end) in mem:
                return mem[(start, end)]
            if end <= start + 1:
                mem[(start, end)] = end - start + 1
                return mem[(start, end)]

            count = 0
            segment = S[start:end + 1]
            for x in 'abcd':
                i = segment.find(x)
                j = segment.rfind(x)
                if i == j == -1:
                    continue
                i += start
                j += start
                count += DFS(i + 1, j - 1, mem) + 2 if i != j else 1
            mem[(start, end)] = count % 1000000007
            return mem[(start, end)]

        mem = {}
        return DFS(0, len(S) - 1, mem)


examples = [
    {
        "input": {
            "S": 'bccb',
        },
        "output": 6
    }, {
        "input": {
            "S": 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba',
        },
        "output": 104860361
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
