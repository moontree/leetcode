"""
=========================
Project -> File: leetcode -> 1359_Count_All_Valid_Pickup_and_Delivery_Options.py
Author: zhangchao
=========================
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input:
    n = 1
Output:
    1
Explanation:
    Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:

Input:
    n = 2
Output:
    6
Explanation:
    All possible orders:
    (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
    This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:

Input:
    n = 3
Output:
    90

Constraints:
    1 <= n <= 500
"""


class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        base = 10 ** 9 + 7
        for i in range(2, n + 1):
            ans = ans * (i * 2 - 1) * i % base
        return ans


examples = [
    {
        "input": {
            "n": 1,
        },
        "output": 1
    }, {
        "input": {
            "n": 2,
        },
        "output": 6
    }, {
        "input": {
            "n": 3,
        },
        "output": 90
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
