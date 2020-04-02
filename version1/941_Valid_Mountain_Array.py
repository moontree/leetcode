"""
Given an array A of integers,
return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

    A.length >= 3

There exists some i with 0 < i < A.length - 1 such that:
    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:

Input:
    [2,1]
Output:
    false

Example 2:

Input:
    [3,5,5]
Output:
    false

Example 3:

Input:
    [0,3,2,1]
Output:
    true


Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        convert = False
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                return False
            elif A[i] > A[i - 1] :
                if convert:
                    return False
            else:
                if i == 1:
                    return False
                if not convert:
                    convert = True
        return convert


examples = [
    {
        "input": {
            "A": [2, 1],
        },
        "output": False
    }, {
        "input": {
            "A": [3, 5, 5],
        },
        "output": False
    }, {
        "input": {
            "A": [0, 3, 2, 1],
        },
        "output": True
    }, {
        "input": {
            "A": [1, 2, 3, 4, 5],
        },
        "output": False
    }, {
        "input": {
            "A": [3, 2, 1],
        },
        "output": False
    }, {
        "input": {
            "A": [1, 3, 2, 1, 2],
        },
        "output": False
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
