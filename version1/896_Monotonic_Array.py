"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input:
    [1,2,2,3]
Output:
    true

Example 2:

Input:
    [6,5,4,4]
Output:
    true

Example 3:

Input:
    [1,3,2]
Output:
    false

Example 4:
Input:
    [1,2,4,5]
Output:
    true

Example 5:

Input:
    [1,1,1]
Output:
    true
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        flag = None
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                if flag == -1:
                    return False
                flag = 1
            elif A[i - 1] > A[i]:
                if flag == 1:
                    return False
                flag = -1
            else:
                pass
        return True


examples = [
    {
        "input": {
            "A": [1, 2, 2, 3],
        },
        "output": True
    }, {
        "input": {
            "A": [6, 5, 4, 4],
        },
        "output": True
    }, {
        "input": {
            "A": [1, 3, 2],
        },
        "output": False
    }, {
        "input": {
            "A": [1, 2, 4, 5],
        },
        "output": True
    }, {
        "input": {
            "A": [1, 1, 1],
        },
        "output": True
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
