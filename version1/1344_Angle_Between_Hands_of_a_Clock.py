"""
=========================
Project -> File: leetcode -> 1344_Angle_Between_Hands_of_a_Clock.py
Author: zhangchao
=========================
Given two numbers, hour and minutes.
Return the smaller angle (in sexagesimal units) formed between the hour and the minute hand.

Example 1:

Input:
    hour = 12, minutes = 30
Output:
    165

Example 2:

Input:
    hour = 3, minutes = 30
Output:
    75

Example 3:

Input:
    hour = 3, minutes = 15
Output:
    7.5

Example 4:

Input:
    hour = 4, minutes = 50
Output:
    155

Example 5:

Input:
    hour = 12, minutes = 0
Output:
    0

Constraints:

    1 <= hour <= 12
    0 <= minutes <= 59
    Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        h = (hour % 12) * 30 + minutes / 2.
        m = minutes * 6
        angle = abs(h - m)
        return min(angle, 360 - angle)


examples = [
    {
        "input": {
            "hour": 12,
            "minutes": 30
        },
        "output": 165
    }, {
        "input": {
            "hour": 3,
            "minutes": 30
        },
        "output": 75
    }, {
        "input": {
            "hour": 3,
            "minutes": 15
        },
        "output": 7.5
    }, {
        "input": {
            "hour": 4,
            "minutes": 50
        },
        "output": 155
    }, {
        "input": {
            "hour": 12,
            "minutes": 0
        },
        "output": 0
    }, {
        "input": {
            "hour": 1,
            "minutes": 57
        },
        "output": 76.5
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
