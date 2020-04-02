"""
=========================
Project -> File: leetcode -> 1342_Number_of_Steps_to_Reduce_a_Number_to_Zero.py
Author: zhangchao
=========================
Given a non-negative integer num,
return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2,
otherwise, you have to subtract 1 from it.



Example 1:

Input:
    num = 14
Output:
    6
Explanation:
    Step 1) 14 is even; divide by 2 and obtain 7.
    Step 2) 7 is odd; subtract 1 and obtain 6.
    Step 3) 6 is even; divide by 2 and obtain 3.
    Step 4) 3 is odd; subtract 1 and obtain 2.
    Step 5) 2 is even; divide by 2 and obtain 1.
    Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:

Input:
    num = 8
Output:
    4
Explanation:
    Step 1) 8 is even; divide by 2 and obtain 4.
    Step 2) 4 is even; divide by 2 and obtain 2.
    Step 3) 2 is even; divide by 2 and obtain 1.
    Step 4) 1 is odd; subtract 1 and obtain 0.

Example 3:

Input:
    num = 123
Output:
    12
"""


class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while num:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2
            res += 1
        return res


examples = [
    {
        "input": {
            "num": 14,
        },
        "output": 6
    }, {
        "input": {
            "num": 8,
        },
        "output": 4
    }, {
        "input": {
            "num": 123,
        },
        "output": 12
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
