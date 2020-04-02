"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input:
    [-4,-1,0,3,10]
Output:
    [0,1,9,16,100]

Example 2:

Input:
    [-7,-3,2,3,11]
Output:
    [4,9,9,49,121]

Note:
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [item * item for item in A]
        res.sort()
        return res


examples = [
    {
        "input": {
            "A": [-4, -1, 0, 3, 10],
        },
        "output": [0, 1, 9, 16, 100]
    }, {
        "input": {
            "A": [-7, -3, 2, 3, 11],
        },
        "output": [4, 9, 9, 49, 121]
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
