"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices,
and for each string, we delete all the characters in those indices.

For example,
if we have an array A = ["babca","bbazb"]
and deletion indices {0, 1, 4},
then the final array after deletions is ["bc","az"].

Suppose we chose a set of deletion indices D such that after deletions,
the final array has every element (row) in lexicographic order.

For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]),
A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

Return the minimum possible value of D.length.



Example 1:

Input:
    ["babca","bbazb"]
Output:
    3
Explanation:
    After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
    Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
    Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.

Example 2:

Input:
    ["edcba"]
Output:
    4
Explanation:
    If we delete less than 4 columns, the only row won't be lexicographically sorted.

Example 3:

Input:
    ["ghi","def","abc"]
Output:
    0
Explanation:
    All rows are already lexicographically sorted.


Note:

    1 <= A.length <= 100
    1 <= A[i].length <= 100
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        r, c = len(A), len(A[0])
        dp = [1 for _ in range(c)]
        for j in range(c - 1)[::-1]:
            for k in range(j + 1, c):
                if all([A[i][j] <= A[i][k] for i in range(r)]):
                    dp[j] = max(dp[j], dp[k] + 1)
        return c - max(dp)


examples = [
    {
        "input": {
            "A": ["babca", "bbazb"],
        },
        "output": 3
    }, {
        "input": {
            "A":  ["edcba"],
        },
        "output": 4
    }, {
        "input": {
            "A": ["ghi", "def", "abc"],
        },
        "output": 0
    }, {
        "input": {
            "A": ["aabbaa", "baabab", "aaabab"],
        },
        "output": 3
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
