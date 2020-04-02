"""
You are driving a vehicle that has capacity empty seats initially available for passengers.
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips,
trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip:
the number of passengers that must be picked up,
and the locations to pick them up and drop them off.
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.


Example 1:

Input:
    trips = [[2,1,5],[3,3,7]], capacity = 4
Output:
    false

Example 2:

Input:
    trips = [[2,1,5],[3,3,7]], capacity = 5
Output:
    true

Example 3:

Input:
    trips = [[2,1,5],[3,5,7]], capacity = 3
Output:
    true

Example 4:

Input:
    trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output:
    true


Constraints:

    trips.length <= 1000
    trips[i].length == 3
    1 <= trips[i][0] <= 100
    0 <= trips[i][1] < trips[i][2] <= 1000
    1 <= capacity <= 100000
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        cache = {}
        for n, s, e in trips:
            cache[s] = cache.get(s, 0) + n
            cache[e] = cache.get(e, 0) - n
        pairs = [[key, cache[key]] for key in cache]
        pairs.sort()
        cur = 0
        for _, v in pairs:
            cur += v
            if cur > capacity:
                return False
        return True


examples = [
    {
        "input": {
            "trips": [[2, 1, 5], [3, 3, 7]],
            "capacity": 4
        },
        "output": False
    }, {
        "input": {
            "trips": [[2, 1, 5], [3, 3, 7]],
            "capacity": 5
        },
        "output": True
    }, {
        "input": {
            "trips": [[2, 1, 5], [3, 5, 7]],
            "capacity": 3
        },
        "output": True
    }, {
        "input": {
            "trips": [[3, 2, 7], [3, 7, 9], [8, 3, 9]],
            "capacity": 11
        },
        "output": True
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
