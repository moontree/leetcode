"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
return the day number of the year.

Example 1:
Input:
    date = "2019-01-09"
Output:
    9
Explanation:
    Given date is the 9th day of the year in 2019.

Example 2:

Input:
    date = "2019-02-10"
Output:
    41

Example 3:

Input:
    date = "2003-03-01"
Output:
    60

Example 4:

Input:
    date = "2004-03-01"
Output:
    61

Constraints:

    date.length == 10
    date[4] == date[7] == '-', and all other date[i]'s are digits
    date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        res = sum(months[:month]) + day
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and month > 2:
            res += 1
        return res


examples = [
    {
        "input": {
            "date": "2019-01-09",
        },
        "output": 9
    }, {
        "input": {
            "date": "2019-02-10",
        },
        "output": 41
    }, {
        "input": {
            "date": "2003-03-01",
        },
        "output": 60
    }, {
        "input": {
            "date": "2004-03-01",
        },
        "output": 61
    }, {
        "input": {
            "date": "1900-03-25",
        },
        "output": 84
    }, {
        "input": {
            "date": "2016-02-29",
        },
        "output": 60
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
