# --*-- encoding: utf-8 --*--
"""
For a non-negative integer X,
the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.


Example 1:

Input:
    A = [1,2,0,0], K = 34
Output:
    [1,2,3,4]
Explanation:
    1200 + 34 = 1234

Example 2:

Input:
    A = [2,7,4], K = 181
Output:
    [4,5,5]
Explanation:
    274 + 181 = 455

Example 3:

Input:
    A = [2,1,5], K = 806
Output:
    [1,0,2,1]
Explanation:
    215 + 806 = 1021

Example 4:

Input:
    A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output:
    [1,0,0,0,0,0,0,0,0,0,0]
Explanation:
    9999999999 + 1 = 10000000000


Note：
    1 <= A.length <= 10000
    0 <= A[i] <= 9
    0 <= K <= 10000
    If A.length > 1, then A[0] != 0
"""


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        a = A[::-1]
        a[0] += K
        c = 0
        for i in range(len(A)):
            c, a[i] = divmod(a[i] + c, 10)
        while c:
            a.append(c % 10)
            c /= 10
        return a[::-1]


examples = [
    {
        "input": {
            "A": [1, 2, 0, 0],
            "K": 34
        },
        "output": [1, 2, 3, 4]
    }, {
        "input": {
            "A": [2, 7, 4],
            "K": 181
        },
        "output": [4, 5, 5]
    }, {
        "input": {
            "A": [2, 1, 5],
            "K": 806
        },
        "output": [1, 0, 2, 1]
    }, {
        "input": {
            "A": [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            "K": 1
        },
        "output": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }, {
        "input": {
            "A": [0],
            "K": 1000
        },
        "output": [1, 0, 0, 0]
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
