"""
Given an array A of 0s and 1s,
divide the array into 3 non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i+1 < j, such that:

A[0], A[1], ..., A[i] is the first part;
A[i+1], A[i+2], ..., A[j-1] is the second part, and
A[j], A[j+1], ..., A[A.length - 1] is the third part.
All three parts have equal binary value.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.
For example, [1,1,0] represents 6 in decimal, not 3.
Also, leading zeros are allowed,
so [0,1,1] and [1,1] represent the same value.



Example 1:
Input:
    [1,0,1,0,1]
Output:
    [0,3]

Example 2:
Input:
    [1,1,0,1,1]
Output:
    [-1,-1]

Note:
    3 <= A.length <= 30000
    A[i] == 0 or A[i] == 1
"""


class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        counts = sum(A)
        if counts % 3 != 0:
            return [-1, -1]
        if counts == 0:
            return [0, 2]
        cc = counts / 3
        c = 0
        i, j = 0, len(A) - 1
        while j > 0 and c < cc:
            if A[j] == 1:
                c += 1
            j -= 1
        # S = ''.join([str(v) for v in A])
        tmp = A[j + 1:]
        cc = len(tmp)
        l = 0
        while l < len(A) and A[l] == 0:
            l += 1
        if A[l: l + cc] != tmp:
            return [-1, -1]
        i = l + cc
        l = i
        while l < len(A) and A[l] == 0:
            l += 1
        if A[l: l + cc] != tmp:
            return [-1, -1]
        for v in A[l + cc: -cc]:
            if v == '1':
                return [-1, -1]
        return [i - 1, l + cc]


examples = [
    {
        "input": {
            "A": [1, 0, 1, 0, 1],
        },
        "output": [0, 3]
    }, {
        "input": {
            "A": [1, 1, 0, 1, 1],
        },
        "output": [-1, -1]
    }, {
        "input": {
            "A": [1, 0, 1, 0, 1, 0],
        },
        "output": [1, 4]
    }, {
        "input": {
            "A": [0, 0, 0],
        },
        "output": [0, 2]
    }, {
        "input": {
            "A": [0, 1, 0, 1, 1],
        },
        "output": [1, 4]
    }, {
        "input": {
            "A": [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        },
        "output": [2, 6]
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

