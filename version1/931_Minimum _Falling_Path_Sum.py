"""
Given a square array of integers A,
we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row,
and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.



Example 1:

Input:
    [[1,2,3],[4,5,6],[7,8,9]]
Output:
    12
Explanation:
    The possible falling paths are:
    [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
    [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
    [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
    The falling path with the smallest sum is [1,4,7], so the answer is 12.



Note:

    1 <= A.length == A[0].length <= 100
    -100 <= A[i][j] <= 100

"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A)):
                if j > 0:
                    if j < len(A) - 1:
                        A[i][j] += min(A[i - 1][j - 1:j + 2])
                    else:
                        A[i][j] += min(A[i - 1][j - 1:j + 1])
                else:
                    if j < len(A) - 1:
                        A[i][j] += min(A[i - 1][j:j + 2])
                    else:
                        A[i][j] += min(A[i - 1][j:j + 1])
        return min(A[-1])


examples = [
    {
        "input": {
            "A": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
        },
        "output": 12
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
