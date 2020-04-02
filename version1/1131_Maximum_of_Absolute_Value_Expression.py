"""
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.


Example 1:

Input:
    arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output:
    13

Example 2:

Input:
    arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output:
    20


Constraints:

    2 <= arr1.length == arr2.length <= 40000
    -10^6 <= arr1[i], arr2[i] <= 10^6
"""


class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        A, B, C, D = [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)

        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)
        return max(a, b, c, d)


examples = [
    {
        "input": {
            "arr1": [1, -2, -5, 0, 10],
            "arr2": [0, -2, -1, -7, -4],
        },
        "output": 20
    }, {
        "input": {
            "arr1": [1, 2, 3, 4],
            "arr2": [-1, 4, 5, 6],
        },
        "output": 13
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
