"""
Given an array A of positive integers (not necessarily distinct),
return the lexicographically largest permutation that is smaller than A,
that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).
If it cannot be done, then return the same array.



Example 1:

Input:
    [3,2,1]
Output:
    [3,1,2]
Explanation:
    Swapping 2 and 1.

Example 2:

Input:
    [1,1,5]
Output:
    [1,1,5]
Explanation:
    This is already the smallest permutation.

Example 3:

Input:
    [1,9,4,6,7]
Output:
    [1,7,4,6,9]
Explanation:
    Swapping 9 and 7.

Example 4:

Input:
    [3,1,1,3]
Output:
    [1,3,1,3]
Explanation:
    Swapping 1 and 3.

Note:
    1 <= A.length <= 10000
    1 <= A[i] <= 10000
"""


class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l, r = -1, -1
        n = len(A)
        for i in range(n - 1)[::-1]:
            if A[i] > A[i + 1]:
                l = i
                break
        if l == -1:
            return A
        for i in range(l, n)[::-1]:
            if A[i] < A[l]:
                r = i
                break
        while l < r and A[r] == A[r - 1]:
            r -= 1
        A[l], A[r] = A[r], A[l]
        return A


examples = [
    {
        "input": {
            "A": [3, 2, 1],
        },
        "output": [3, 1, 2]
    }, {
        "input": {
            "A": [1, 1, 5],
        },
        "output": [1, 1, 5]
    }, {
        "input": {
            "A": [1, 9, 4, 6, 7],
        },
        "output": [1, 7, 4, 6, 9]
    }, {
        "input": {
            "A": [3, 1, 1, 3],
        },
        "output": [1, 3, 1, 3]
    }, {
        "input": {
            "A": [4, 3, 1, 1, 3],
        },
        "output": [4, 1, 3, 1, 3]
    }, {
        "input": {
            "A": [3, 1, 1, 3, 2],
        },
        "output": [3, 1, 1, 2, 3]
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
