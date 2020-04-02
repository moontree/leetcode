"""
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.
The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.



Example 1:

Input:
    bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output:
    [10,55,45,25,25]

Constraints:

    1 <= bookings.length <= 20000
    1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
    1 <= bookings[i][2] <= 10000
"""


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        flags = [0 for _ in range(n + 1)]
        for s, e, v in bookings:
            flags[s] += v
            if e + 1 <= n:
                flags[e + 1] -= v
        for i in range(1, n + 1):
            flags[i] += flags[i - 1]
        return flags[1:]


examples = [
    {
        "input": {
            "bookings": [[1, 2, 10], [2, 3, 20], [2, 5, 25]],
            "n": 5
        },
        "output": [10, 55, 45, 25, 25]
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
