"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain,
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input:
    [0,1,0]
Output:
    1

Example 2:

Input:
    [0,2,1,0]
Output:
    1
Note:
    3 <= A.length <= 10000
    0 <= A[i] <= 10^6
    A is a mountain, as defined above.
"""

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) / 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid
        print l, r
        return l


examples = [
    {
        "input": {
            "A": [0, 1, 0],
        },
        "output": 1
    }, {
        "input": {
            "A": [0, 1, 2, 0],
        },
        "output": 2
    }, {
        "input": {
            "A": [0, 3, 2, 0],
        },
        "output": 1
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']