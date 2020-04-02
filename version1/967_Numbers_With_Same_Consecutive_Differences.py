# --*-- encoding: utf-8 --*--
"""
Return all non-negative integers of length N
such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself.

or example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input:
    N = 3, K = 7
Output:
    [181,292,707,818,929]
Explanation:
    Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input:
    N = 2, K = 1
Output:
    [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:
    1 <= N <= 9
    0 <= K <= 9
"""


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return range(10)
        res = []
        for n in self.numsSameConsecDiff(N - 1, K):
            if n == 0:
                continue
            else:
                v = n % 10
                if v - K >= 0:
                    res.append(n * 10 + v - K)
                if K != 0 and v + K < 10:
                    res.append(n * 10 + v + K)
        return res


examples = [
    {
        "input": {
            "N": 3,
            "K": 7
        },
        "output": [181, 292, 707, 818, 929]
    }, {
        "input": {
            "N": 2,
            "K": 1
        },
        "output": [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
    }, {
        "input": {
            "N": 2,
            "K": 0
        },
        "output": [11, 22, 33, 44, 55, 66, 77, 88, 99]
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
