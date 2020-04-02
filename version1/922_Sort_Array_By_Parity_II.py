"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

"""


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = 0, 1
        while l < len(A) and r < len(A):
            while l < len(A) and A[l] % 2 == 0:
                l += 2
            while l < len(A) and A[r] % 2 == 1:
                r += 2
            if l < len(A) and r < len(A):
                A[l], A[r] = A[r], A[l]
            l += 2
            r += 2
        return A


examples = [
    {
        "input": {
            "A": [4, 2, 5, 7],
        },
        "output": [4, 5, 2, 7]
    }, {
        "input": {
            "A": [2, 3, 1, 1, 4, 0, 0, 4, 3, 3],
        },
        "output": [2, 3, 0, 1, 4, 1, 0, 3, 4, 3]
    }, {
        "input": {
            "A": [2, 3],
        },
        "output": [2, 3]
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
