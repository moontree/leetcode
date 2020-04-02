"""
=========================
Project -> File: leetcode -> 1363_Largest_Multiple_of_Three.py
Author: zhangchao
=========================
Given an integer array of digits,
return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

Example 1:

Input:
    digits = [8,1,9]
Output:
    "981"

Example 2:

Input:
    digits = [8,6,7,1,0]
Output:
    "8760"

Example 3:

Input:
    digits = [1]
Output:
    ""

Example 4:

Input:
    digits = [0,0,0,0,0,0]
Output:
    "0"


Constraints:

    1 <= digits.length <= 10^4
    0 <= digits[i] <= 9
    The returning answer must not contain unnecessary leading zeros.
"""


class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """

        digits.sort()
        ds = [[] for _ in range(3)]
        s = 0
        for d in digits:
            s += d
            ds[d % 3].append(d)
        if s % 3 == 0:
            arrs = digits[::-1]
        elif s % 3 == 1:
            if ds[1]:
                arrs = sorted(ds[0] + ds[1][1:] + ds[2], reverse=True)
            else:
                arrs = sorted(ds[0] + ds[2][2:], reverse=True)
        else:
            if ds[2]:
                arrs = sorted(ds[0] + ds[1] + ds[2][1:], reverse=True)
            else:
                arrs = sorted(ds[0] + ds[1][2:], reverse=True)
        i = 0
        while i < len(arrs) - 1 and arrs[i] == 0:
            i += 1
        return ''.join([str(v) for v in arrs[i:]])


examples = [
    {
        "input": {
            "digits": [8, 1, 9],
        },
        "output": "981"
    }, {
        "input": {
            "digits": [8, 6, 7, 1, 0],
        },
        "output": "8760"
    }, {
        "input": {
            "digits": [1],
        },
        "output": ""
    }, {
        "input": {
            "digits": [0, 0, 0],
        },
        "output": "0"
    }, {
        "input": {
            "digits": [5, 8],
        },
        "output": ""
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
