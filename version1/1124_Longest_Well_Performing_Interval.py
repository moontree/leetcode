"""
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which
the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.


Example 1:

Input:
    hours = [9,9,6,0,6,6,9]
Output:
    3
Explanation:
    The longest well-performing interval is [9,9,6].

Constraints:

    1 <= hours.length <= 10000
    0 <= hours[i] <= 16
"""


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        l, r, res = 0, 0, 0
        flags = [0 for _ in range(len(hours) + 1)]
        for i, v in enumerate(hours):
            if v > 8:
                flags[i + 1] = flags[i] + 1
            else:
                flags[i + 1] = flags[i] - 1
        # print flags
        q = []
        for i, v in enumerate(flags):
            if not q or flags[q[-1]] > v:
                q.append(i)
        for i in range(len(hours) + 1)[::-1]:
            while q and flags[q[-1]] < flags[i]:
                res = max(res, i - q[-1])
                q.pop()
        return res


examples = [
    {
        "input": {
            "hours": [9, 9, 6, 0, 6, 6, 9],
        },
        "output": 3
    }, {
        "input": {
            "hours": [9, 9, 6, 0, 9, 6, 9],
        },
        "output": 7
    }, {
        "input": {
            "hours": [6, 9, 9],
        },
        "output": 3
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
