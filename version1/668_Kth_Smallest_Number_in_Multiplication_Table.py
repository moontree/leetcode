"""
Nearly every one have used the Multiplication Table.
But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table,
and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input:
    m = 3, n = 3, k = 5
Output:
    3
Explanation:
    The Multiplication Table:
    1	2	3
    2	4	6
    3	6	9

    The 5-th smallest number is 3 (1, 2, 2, 3, 3).

Example 2:
Input:
    m = 2, n = 3, k = 6
Output:
    6
Explanation:
    The Multiplication Table:
    1	2	3
    2	4	6

    The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
    The m and n will be in the range [1, 30000].
    The k will be in the range [1, m * n]
"""


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def helper(v):
            c = 0
            for i in range(1, m + 1):
                c += min(n, v / i)
            return c

        ll, rr = 1, m * n
        while ll < rr:
            mid = (ll + rr) / 2
            v = helper(mid)
            if v < k:
                ll = mid + 1
            else:
                rr = mid
        return rr


examples = [
    {
        "input": {
            "m": 3,
            "n": 3,
            "k": 5
        },
        "output": 3
    }, {
        "input": {
            "m": 2,
            "n": 3,
            "k": 6
        },
        "output": 6
    }, {
        "input": {
            "m": 42,
            "n": 34,
            "k": 401
        },
        "output": 126
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
