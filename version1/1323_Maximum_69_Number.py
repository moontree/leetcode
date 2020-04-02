"""
=========================
Project -> File: leetcode -> 1323_Maximum_69_Number.py
Author: zhangchao
=========================
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit
(6 becomes 9, and 9 becomes 6).


Example 1:

Input:
    num = 9669
Output:
    9969
Explanation:
    Changing the first digit results in 6669.
    Changing the second digit results in 9969.
    Changing the third digit results in 9699.
    Changing the fourth digit results in 9666.
    The maximum number is 9969.

Example 2:

Input:
    num = 9996
Output:
    9999
Explanation:
    Changing the last digit 6 to 9 results in the maximum number.

Example 3:

Input:
    num = 9999
Output:
    9999
Explanation:
    It is better not to apply any change.


Constraints:

    1 <= num <= 10^4
    num's digits are 6 or 9.
"""


class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        chars = [c for c in str(num)]
        for i, c in enumerate(chars):
            if c == '6':
                chars[i] = '9'
                break
        return int(''.join(chars))


examples = [
    {
        "input": {
            "num": 9669,
        },
        "output": 9969
    }, {
        "input": {
            "num": 9996,
        },
        "output": 9999
    }, {
        "input": {
            "num": 9999,
        },
        "output": 9999
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
