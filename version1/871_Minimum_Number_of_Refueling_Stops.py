"""
=========================
Project -> File: leetcode -> 871_Minimum_Number_of_Refueling_Stops.py
Author: zhangchao
=========================
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.
Each station[i] represents a gas station that is station[i][0] miles east of the starting position,
and has station[i][1] liters of gas.

The car starts with an infinite tank of gas,
which initially has startFuel liters of fuel in it.
It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel,
transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?
If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
If the car reaches the destination with 0 fuel left, it is still considered to have arrived.



Example 1:

Input:
    target = 1, startFuel = 1, stations = []
Output:
    0
Explanation:
    We can reach the target without refueling.

Example 2:

Input:
    target = 100, startFuel = 1, stations = [[10,100]]
Output:
    -1
Explanation:
    We can't reach the target (or even the first gas station).

Example 3:

Input:
    target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output:
    2
Explanation:
    We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.


Note:

    1 <= target, startFuel, stations[i][1] <= 10^9
    0 <= stations.length <= 500
    0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
"""
import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        q = []
        total = startFuel
        res = 0
        stations.append([target, 0])
        for dis, fuel in stations:
            if total >= dis:
                heapq.heappush(q, -fuel)
            else:
                while q and total < dis:
                    total -= heapq.heappop(q)
                    res += 1
                if total < dis:
                    return -1
                heapq.heappush(q, -fuel)
        return res


examples = [
    {
        "input": {
            "target": 1,
            "startFuel": 1,
            "stations": []
        },
        "output": 0
    }, {
        "input": {
            "target": 100,
            "startFuel": 1,
            "stations": [[10, 100]]
        },
        "output": -1
    }, {
        "input": {
            "target": 100,
            "startFuel": 10,
            "stations": [[10, 60], [20, 30], [30, 30], [60, 40]]
        },
        "output": 2
    }, {
        "input": {
            "target": 100,
            "startFuel": 50,
            "stations": [[25, 25], [50, 50]]
        },
        "output": 1
    }, {
        "input": {
            "target": 100,
            "startFuel": 50,
            "stations": [[25, 50], [50, 25]]
        },
        "output": 1
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
