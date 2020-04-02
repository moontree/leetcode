"""
=========================
Project -> File: leetcode -> 1185_Day_of_the_Week.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/7 6:15 PM
=========================
"""
"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values 
{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 
Example 1:

Input: 
    day = 31, month = 8, year = 2019
Output: 
    "Saturday"
    
Example 2:

Input: 
    day = 18, month = 7, year = 1999
Output: 
    "Sunday"
    
Example 3:

Input: 
    day = 15, month = 8, year = 1993
Output: 
    "Sunday"
 

Constraints:

    The given dates are valid dates between the years 1971 and 2100.
"""


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def helper(year):
            return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)

        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        idx = 4

        diffs = 0
        for yy in range(1971, year):
            diffs += 366 if helper(yy) else 365

        diffs += sum(days[:month]) + day
        if month > 2 and helper(year):
            diffs += 1
        idx = (idx + diffs) % 7
        return week_days[idx]


examples = [
    {
        "input": {
            "year": 1972,
            "month": 3,
            "day": 1,
        },
        "output": "Wednesday"
    }, {
        "input": {
            "year": 2019,
            "month": 8,
            "day": 31,
        },
        "output": "Saturday"
    }, {
        "input": {
            "year": 1999,
            "month": 7,
            "day": 18,
        },
        "output": "Sunday"
    }, {
        "input": {
            "year": 1993,
            "month": 8,
            "day": 15,
        },
        "output": "Sunday"
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
