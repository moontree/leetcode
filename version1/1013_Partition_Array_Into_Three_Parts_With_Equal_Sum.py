"""
Given an array A of integers,
return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])



Example 1:

Input:
    [0,2,1,-6,6,-7,9,1,2,0,1]
Output:
    true
Explanation:
    0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

Input:
    [0,2,1,-6,6,7,9,-1,2,0,1]
Output:
    false

Example 3:

Input:
    [3,3,6,5,-2,2,5,1,-9,4]
Output:
    true
Explanation:
    3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Note:

    3 <= A.length <= 50000
    -10000 <= A[i] <= 10000
"""


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        target, cur, c = s / 3, 0, 0
        for v in A:
            cur += v
            if cur == target:
                cur = 0
                c += 1
        if cur == target:
            c += 1
        if c == 3:
            return True
        return False


examples = [
    {
        "input": {
            "A": [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1],
        },
        "output": True
    }, {
        "input": {
            "A": [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1],
        },
        "output": False
    }, {
        "input": {
            "A": [3, 3, 6, 5, -2, 2, 5, 1, -9, 4],
        },
        "output": True
    }, {
        "input": {
            "A": [1, 0, -1],
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
