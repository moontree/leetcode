# --*-- encoding: utf-8 --*--
"""
Given a positive integer N,
return the number of positive integers less than or equal to N that have at least 1 repeated digit.



Example 1:

Input:
    20
Output:
    1
Explanation:
    The only positive number (<= 20) with at least 1 repeated digit is 11.

Example 2:

Input:
    100
Output:
    10
Explanation:
    The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:

Input:
    1000
Output:
    262

Note:

    1 <= N <= 10^9
"""


class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 10:
            return 0
        nums = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        nr = [0, 9, 81, 648, 4536, 27216, 136080, 544320, 1632960, 3265920]
        s = str(N)
        cache = {}

        def helper(s, is_first):
            if len(s) == 0:
                return 1
            n = int(s[0])
            res = 0
            for i in range(is_first, n):
                if i in cache:
                    res += 0
                else:
                    cache[i] = True
                    l = len(s) - 1
                    c = 10 - len(cache)
                    if c - l < 1:
                        res += 0
                    res += nums[c] / nums[c - l]
                    del cache[i]

            if n not in cache:
                cache[n] = True
                l = len(s) - 1
                c = 10 - len(cache)
                if c - l < 1:
                    res += 0
                v = helper(s[1:], False)
                res += v
            return res

        not_repeat = helper(s, True)
        ss = sum(nr[:len(s)])
        return N - not_repeat - ss


examples = [
    {
        "input": {
            "N": 32,
        },
        "output": 2
    },{
        "input": {
            "N": 20,
        },
        "output": 1
    }, {
        "input": {
            "N": 100,
        },
        "output": 10
    }, {
        "input": {
            "N": 1000,
        },
        "output": 262
    }, {
        "input": {
            "N": 10000,
        },
        "output": 4726
    }, {
        "input": {
            "N": 10 ** 9,
        },
        "output": 994388230
    }, {
        "input": {
            "N": 10,
        },
        "output": 0
    }, {
        "input": {
            "N": 22,
        },
        "output": 2
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
