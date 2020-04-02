"""
Given a set of points in the xy-plane,
determine the minimum area of any rectangle formed from these points,
with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:
Input:
    [[1,2],[2,1],[1,0],[0,1]]
Output:
    2.00000
Explanation:
    The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:

Input:
    [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output:
    1.00000
Explanation: T
    he minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:

Input:
    [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output:
    0
Explanation:
    There is no possible rectangle to form from these points.

Example 4:

Input:
    [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output:
    2.00000
Explanation:
    The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.

Note:
    1 <= points.length <= 50
    0 <= points[i][0] <= 40000
    0 <= points[i][1] <= 40000
    All points are distinct.
    Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def dis(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        res = float('inf')
        cache = {}
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                l = dis(points[i], points[j])
                key = (l, points[i][0] + points[j][0], points[i][1] + points[j][1])
                if key not in cache:
                    cache[key] = []
                cache[key].append(points[i])
        for key in cache:
            if len(cache[key]) < 2:
                continue
            mid_x, mid_y = key[1], key[2]
            pairs = cache[key]
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    x1, y1 = pairs[i]
                    # x2, y2 = pairs[j]
                    x3, y3 = mid_x - x1, mid_y - y1
                    area = dis(pairs[i], pairs[j]) * dis(pairs[j], [x3, y3])
                    res = min(res, area)
        if res == float('inf'):
            return 0
        return res


examples = [
    {
        "input": {
            "points": [[1, 2], [2, 1], [1, 0], [0, 1]],
        },
        "output": 2.0
    }, {
        "input": {
            "points": [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]],
        },
        "output": 1.0
    }, {
        "input": {
            "points": [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]],
        },
        "output": 0.0
    }, {
        "input": {
            "points": [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]],
        },
        "output": 2.0
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
