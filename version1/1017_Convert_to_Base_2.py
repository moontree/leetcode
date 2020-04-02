"""
Given a number N,
return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".



Example 1:

Input:
    2
Output:
    "110"
Explantion:
    (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:

Input:
    3
Output:
    "111"
Explantion:
    (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:
Input:
    4
Output:
    "100"
Explantion:
    (-2) ^ 2 = 4

Note:
    0 <= N <= 10^9
"""


class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return '0'
        res = []
        f = 1
        while N:
            r = N % 2
            res.append(r)
            if f == -1:
                N += r
                f = 1
            else:
                f = -1
            N /= 2
        res = res[::-1]
        return ''.join([str(i) for i in res])


examples = [
    {
        "input": {
            "N": 2,
        },
        "output": '110'
    }, {
        "input": {
            "N": 3,
        },
        "output": '111'
    }, {
        "input": {
            "N": 4,
        },
        "output": '100'
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
