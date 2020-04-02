"""
=========================
Project -> File: leetcode -> 1360_Number_of_Days_Between_Two_Dates.py
Author: zhangchao
=========================
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input:
    date1 = "2019-06-29", date2 = "2019-06-30"
Output:
    1

Example 2:

Input:
    date1 = "2020-01-15", date2 = "2019-12-31"
Output:
    15

Constraints:

    The given dates are valid dates between the years 1971 and 2100.
"""


class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        monthes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def helper(date):
            year, month, day = [int(v) for v in date.split('-')]
            days = 0
            for y in range(1971, year):
                if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                    days += 366
                else:
                    days += 365
            for m in range(month):
                days += monthes[m]
            days += day
            if month > 2 and (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                days += 1
            return days

        d1, d2 = helper(date1), helper(date2)
        print d1, d2
        return abs(d1 - d2)


examples = [
    {
        "input": {
            "date1": "2019-06-29",
            "date2": "2019-06-30"
        },
        "output": 1
    }, {
        "input": {
            "date1": "2020-01-15",
            "date2": "2019-12-31"
        },
        "output": 15
    }, {
        "input": {
            "date1": "2008-03-21",
            "date2": "2041-05-08"
        },
        "output": 12101
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
