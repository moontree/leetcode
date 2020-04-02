"""
Given an array of 4 digits,
return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00,
and the largest is 23:59.
Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.
If no valid time can be made, return an empty string.


Example 1:

Input:
    [1,2,3,4]
Output:
    "23:41"

Example 2:

Input:
    [5,5,5,5]
Output:
    ""
"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        permulations = [
            [0, 1, 2, 3],
            [0, 1, 3, 2],
            [0, 2, 1, 3],
            [0, 2, 3, 1],
            [0, 3, 1, 2],
            [0, 3, 2, 1],
            [1, 2, 3, 0],
            [1, 2, 0, 3],
            [1, 3, 2, 0],
            [1, 3, 0, 2],
            [1, 0, 2, 3],
            [1, 0, 3, 2],
            [2, 3, 0, 1],
            [2, 3, 1, 0],
            [2, 0, 3, 1],
            [2, 0, 1, 3],
            [2, 1, 3, 0],
            [2, 1, 0, 3],
            [3, 0, 1, 2],
            [3, 0, 2, 1],
            [3, 1, 0, 2],
            [3, 1, 2, 0],
            [3, 2, 0, 1],
            [3, 2, 1, 0],
        ]
        res = ''
        t = -1
        for i1, i2, i3, i4 in permulations:
            h = A[i1] * 10 + A[i2]
            m = A[i3] * 10 + A[i4]
            if h < 24 and m < 60:
                tmp = h * 60 + m
                if t < tmp < 1440:
                    t = tmp
                    res = '%02d:%02d' % (h, m)
        return res


examples = [
    {
        "input": {
            "A": [1, 2, 3, 4],
        },
        "output": "23:41"
    }, {
        "input": {
            "A": [5, 5, 5, 5],
        },
        "output": ""
    }, {
        "input": {
            "A": [2, 0, 6, 6],
        },
        "output": "06:26"
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
