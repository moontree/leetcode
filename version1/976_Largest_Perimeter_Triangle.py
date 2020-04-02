"""
Given an array A of positive lengths,
return the largest perimeter of a triangle with non-zero area,
formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.


Example 1:
Input:
    [2,1,2]
Output:
    5

Example 2:
Input:
    [1,2,1]
Output:
    0

Example 3:
Input:
    [3,2,3,4]
Output:
    10

Example 4:
Input:
    [3,6,2,3]
Output:
    8

Note:

    3 <= A.length <= 10000
    1 <= A[i] <= 10^6
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        l = len(A) - 3
        while l >= 0:
            if A[l] + A[l + 1] > A[l + 2]:
                return A[l] + A[l + 1] + A[l + 2]
            else:
                l -= 1
        return 0


examples = [
    {
        "input": {
            "A": [2, 1, 2],
        },
        "output": 5
    }, {
        "input": {
            "A": [1, 2, 1],
        },
        "output": 0
    }, {
        "input": {
            "A": [3, 2, 3, 4],
        },
        "output": 10
    }, {
        "input": {
            "A": [3, 6, 2, 3],
        },
        "output": 8
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

