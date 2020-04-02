"""
=========================
Project -> File: leetcode -> 1383_Maximum_Performance_of_a_Team.py
Author: zhangchao
=========================
There are n engineers numbered from 1 to n and two arrays:
speed and efficiency, where speed[i] and efficiency[i]
represent the speed and efficiency for the i-th engineer respectively.
Return the maximum performance of a team composed of at most k engineers,
since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds
multiplied by the minimum efficiency among their engineers.

Example 1:

Input:
    n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output:
    60
Explanation:
    We have the maximum performance of the team by selecting engineer 2
    (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
    That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:

Input:
    n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output:
    68
Explanation:
    This is the same example as the first but k = 3.
    We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team.
    That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:

Input:
    n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output:
    72


Constraints:

    1 <= n <= 10^5
    speed.length == n
    efficiency.length == n
    1 <= speed[i] <= 10^5
    1 <= efficiency[i] <= 10^8
    1 <= k <= n
"""
import heapq


class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        pairs = [[e, s] for s, e in zip(speed, efficiency)]
        pairs.sort(key=lambda x: [-x[0], x[1]])

        q = []
        speed_sum = 0
        res = 0
        # print pairs, q, speed_sum, res
        for e, s in pairs:
            heapq.heappush(q, s)
            speed_sum +=s
            if len(q) > k:
                speed_sum -= heapq.heappop(q)
            res = max(res, e * speed_sum)
            # print pairs[i], speed_sum, res
        return res % (10 ** 9 + 7)


examples = [
    {
        "input": {
            "n": 6,
            "speed": [2, 10, 3, 1, 5, 8],
            "efficiency": [5, 4, 3, 9, 7, 2],
            "k": 2
        },
        "output": 60
    }, {
        "input": {
            "n": 6,
            "speed": [2, 10, 3, 1, 5, 8],
            "efficiency": [5, 4, 3, 9, 7, 2],
            "k": 3
        },
        "output": 68
    }, {
        "input": {
            "n": 6,
            "speed": [2, 10, 3, 1, 5, 8],
            "efficiency": [5, 4, 3, 9, 7, 2],
            "k": 4
        },
        "output": 72
    }, {
        "input": {
            "n": 3,
            "speed": [2, 8, 2],
            "efficiency": [2, 7, 1],
            "k": 2
        },
        "output": 56
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
