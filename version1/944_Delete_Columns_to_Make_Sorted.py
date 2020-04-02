"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices,
and for each string, we delete all the characters in those indices.

For example,
if we have an array A = ["abcdef","uvwxyz"] and
deletion indices {0, 2, 3},
then the final array after deletions is ["bef", "vyz"],
and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
(Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

Suppose we chose a set of deletion indices D such that after deletions,
each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.



Example 1:

Input:
    ["cba","daf","ghi"]
Output:
    1
Explanation:
    After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
    If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.

Example 2:

Input:
    ["a","b"]
Output:
    0
Explanation:
    D = {}

Example 3:

Input:
    ["zyx","wvu","tsr"]
Output:
    3
Explanation:
    D = {0, 1, 2}


Note:
    1 <= A.length <= 100
    1 <= A[i].length <= 1000
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        r, c = len(A), len(A[0])
        res = 0
        for j in range(c):
            for i in range(1, r):
                if A[i - 1][j] > A[i][j]:
                    res += 1
                    break
        return res


examples = [
    {
        "input": {
            "A": ["cba", "daf", "ghi"],
        },
        "output": 1
    }, {
        "input": {
            "A": ["a", "b"],
        },
        "output": 0
    }, {
        "input": {
            "A": ["zyx", "wvu", "tsr"],
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
