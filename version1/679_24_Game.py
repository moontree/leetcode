"""
You have 4 cards each containing a number from 1 to 9.
You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input:
    [4, 1, 8, 7]
Output:
    True
Explanation:
    (8-4) * (7-1) = 24

Example 2:
Input:
    [1, 2, 1, 2]
Output:
    False
Note:
    The division operator / represents real division, not integer division.
    For example, 4 / (1 - 2/3) = 12.
    Every operation done is between two numbers.
    In particular, we cannot use - as a unary operator.
    For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
    You cannot concatenate numbers together.
    For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
from operator import truediv, mul, add, sub


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(A):
            if not A:
                return False
            if len(A) == 1:
                return abs(A[0] - 24) < 1e-6

            for i in xrange(len(A)):
                for j in xrange(len(A)):
                    if i != j:
                        B = [A[k] for k in xrange(len(A)) if i != k != j]
                        for op in (truediv, mul, add, sub):
                            if (op is add or op is mul) and j > i:
                                continue
                            if op is not truediv or A[j]:
                                B.append(op(A[i], A[j]))
                                if helper(B):
                                    return True
                                B.pop()
            return False

        return helper(nums)


examples = [
    {
        "input": {
            "nums": [4, 1, 8, 7],
        },
        "output": True
    }, {
        "input": {
            "nums": [1, 2, 1, 2],
        },
        "output": False
    }, {
        "input": {
            "nums": [1, 9, 1, 2],
        },
        "output": True
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
