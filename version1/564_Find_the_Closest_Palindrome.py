"""
Given an integer n,
find the closest integer (not including itself),
which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input:
    "123"
Output:
    "121"
Note:
    The input n is a positive integer represented by string, whose length will not exceed 18.
    If there is a tie, return the smaller one as answer.
"""


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            return str(int(n) - 1)
        nums = '0123456789'
        res, diff = float('inf'), float('inf')
        p = len(n) / 2
        left = int(n[: p])
        mid = '' if len(n) % 2 == 0 else n[p]
        if not mid:
            target = [
                str(left) + str(left)[::-1],
                str(left + 1) + str(left + 1)[::-1],
                str(left - 1) + str(left - 1)[::-1],
                str(10 ** (len(n) - 1) - 1),
                str(10 ** (len(n)) + 1)
            ]
        else:
            target = [
                str(left) + mid + str(left)[::-1],
                str(left) + nums[(int(mid) + 1) % 10] + str(left)[::-1],
                str(left) + nums[(int(mid) - 1) % 10]  + str(left)[::-1],
                str(left + 1) + nums[(int(mid) + 1) % 10] + str(left + 1)[::-1],
                str(left - 1) + nums[(int(mid) - 1) % 10] + str(left - 1)[::-1],
                str(10 ** (len(n) - 1) - 1),
                str(10 ** (len(n)) + 1)
            ]
        for v in target:
            d = abs(int(n) - int(v))
            if d != 0:
                if d < diff:
                    diff, res = d, int(v)
                elif d == diff:
                    res = min(res, int(v))

        return str(res)


examples = [
    {
        "input": {
            "n": "123"
        },
        "output": "121"
    }, {
        "input": {
            "n": "181"
        },
        "output": "171"
    },  {
        "input": {
            "n": "11"
        },
        "output": "9"
    }, {
        "input": {
            "n": "1111"
        },
        "output": "1001"
    }, {
        "input": {
            "n": "21"
        },
        "output": "22"
    }, {
        "input": {
            "n": "9900"
        },
        "output": "9889"
    }, {
        "input": {
            "n": "5199"
        },
        "output": "5225"
    }, {
        "input": {
            "n": "12120"
        },
        "output": "12121"
    }, {
        "input": {
            "n": "12989"
        },
        "output": "13031"
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
