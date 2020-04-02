"""
On a plane there are n points with integer coordinates points[i] = [xi, yi].
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally
(it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.


Example 1:

Input:
    points = [[1,1],[3,4],[-1,0]]
Output:
    7
Explanation:
    One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
    Time from [1,1] to [3,4] = 3 seconds
    Time from [3,4] to [-1,0] = 4 seconds
    Total time = 7 seconds

Example 2:

Input:
    points = [[3,2],[-2,2]]
Output:
    5

Constraints:

    points.length == n
    1 <= n <= 100
    points[i].length == 2
    -1000 <= points[i][0], points[i][1] <= 1000
"""


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        cx, cy = points[0]
        for x, y in points:
            dx, dy = abs(x - cx), abs(y - cy)
            res += abs(dx - dy) + min(dx, dy)
            cx, cy = x, y
        return res


examples = [
    {
        "input": {
            "points": [[1, 1], [3, 4], [-1, 0]],
        },
        "output": 7
    }, {
        "input": {
            "points": [[3, 2], [-2, 2]],
        },
        "output": 5
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
