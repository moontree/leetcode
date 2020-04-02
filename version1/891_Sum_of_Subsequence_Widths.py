"""
Given an array of integers A,
consider all non-empty subsequences of A.

For any sequence S,
let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.

As the answer may be very large,
return the answer modulo 10^9 + 7.



Example 1:

Input:
    [2,1,3]
Output:
    6
Explanation:
    Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
    The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
    The sum of these widths is 6.
Note:
    1 <= A.length <= 20000
    1 <= A[i] <= 20000
"""


class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        base = 10 ** 9 + 7
        A.sort()
        res, v = 0, 0
        for i in range(1, len(A)):
            diff = A[i] - A[i - 1]
            v = (2 * v + (diff << i) - diff) % base
            res = (res + v) % base
        return res


examples = [
    {
        "input": {
            "A": [2, 1, 3],
        },
        "output": 6
    }, {
        "input": {
            "A": [1, 3, 5],
        },
        "output": 12
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
