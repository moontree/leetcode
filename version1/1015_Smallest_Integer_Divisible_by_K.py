"""
Given a positive integer K,
you need find the smallest positive integer N such that N is divisible by K,
and N only contains the digit 1.

Return the length of N.
If there is no such N, return -1.



Example 1:

Input:
    1
Output:
    1
Explanation:
    The smallest answer is N = 1, which has length 1.

Example 2:

Input:
    2
Output:
    -1
Explanation:
    There is no such positive integer N divisible by 2.

Example 3:

Input:
    3
Output:
    3
Explanation:
    The smallest answer is N = 111, which has length 3.

Note:
    1 <= K <= 10^5
"""


class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0 or K % 5 == 0:
            return -1
        v = 1
        res = 1
        while v % K != 0:
            v %= K
            v = v * 10 + 1
            res += 1
        return res
        # map = {
        #     1: {
        #         1: 1,
        #         2: 2,
        #         3: 3,
        #         4: 4,
        #         5: 5,
        #         6: 6,
        #         7: 7,
        #         8: 8,
        #         9: 9
        #     },
        #     3: {
        #         1: 7,
        #         2: 4,
        #         3: 1,
        #         4: 8,
        #         5: 5,
        #         6: 2,
        #         7: 9,
        #         8: 6,
        #         9: 3
        #     },
        #     7: {
        #         1: 3,
        #         2: 6,
        #         3: 9,
        #         4: 2,
        #         5: 5,
        #         6: 8,
        #         7: 1,
        #         8: 4,
        #         9: 7
        #     },
        #     9: {
        #         1: 9,
        #         2: 8,
        #         3: 7,
        #         4: 6,
        #         5: 5,
        #         6: 4,
        #         7: 3,
        #         8: 2,
        #         9: 1
        #     }
        # }
        # res = 0
        # b = K % 10
        # cur = K
        # while cur:
        #     if cur % 10 == 1:
        #         cur /= 10
        #         res += 1
        #
        #     else:
        #         v = cur % 10
        #         rest = 1 - v
        #         if rest < 0:
        #             rest += 10
        #         cur = cur + map[b][rest] * K
        #         cur /= 10
        #         res += 1
        #
        # return res


examples = [
    {
        "input": {
            "K": 1,
        },
        "output": 1
    }, {
        "input": {
            "K": 2,
        },
        "output": -1
    }, {
        "input": {
            "K": 3,
        },
        "output": 3
    }, {
        "input": {
            "K": 7,
        },
        "output": 6
    }, {
        "input": {
            "K": 13,
        },
        "output": 6
    }, {
        "input": {
            "K": 21,
        },
        "output": 6
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
