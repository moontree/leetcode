"""
Given an array A of 0s and 1s,
consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number
(from most-significant-bit to least-significant-bit.)

Return a list of booleans answer,
where answer[i] is true if and only if N_i is divisible by 5.

Example 1:

Input:
    [0,1,1]
Output:
    [true,false,false]
Explanation:
    The input numbers in binary are 0, 01, 011;
     which are 0, 1, and 3 in base-10.
     Only the first number is divisible by 5, so answer[0] is true.

Example 2:

Input:
    [1,1,1]
Output:
    [false,false,false]

Example 3:

Input:
    [0,1,1,1,1,1]
Output:
    [true,false,false,false,true,false]

Example 4:

Input:
    [1,1,1,0,1]
Output:
    [false,false,false,false,false]

Note:
    1 <= A.length <= 30000
    A[i] is 0 or 1
"""


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        cur = 0
        res = []
        for v in A:
            cur = cur * 2 + v
            res.append(cur % 5 == 0)
        return res


examples = [
    {
        "input": {
            "A": [0, 1, 1],
        },
        "output": [True, False, False]
    }, {
        "input": {
            "A": [1, 1, 1],
        },
        "output": [False, False, False]
    }, {
        "input": {
            "A": [0, 1, 1, 1, 1, 1],
        },
        "output": [True, False, False, False, True, False]
    }, {
        "input": {
            "A": [1, 1, 1, 0, 1],
        },
        "output": [False, False, False, False, False]
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
