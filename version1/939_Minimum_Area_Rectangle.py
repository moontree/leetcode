"""
Given a set of points in the xy-plane,
determine the minimum area of a rectangle formed from these points,
with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.



Example 1:

Input:
    [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output:
    4

Example 2:

Input:
    [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Note:

    1 <= points.length <= 500
    0 <= points[i][0] <= 40000
    0 <= points[i][1] <= 40000
    All points are distinct.

"""


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cache = {}
        for x, y in points:
            if x not in cache:
                cache[x] = []
            cache[x].append(y)
        last_x = {}
        xx = cache.keys()
        xx.sort()
        res = float('inf')
        for x in xx:
            values = cache[x]
            values.sort()

            for i in range(len(values)):
                for j in range(1, len(values)):
                    y1, y2 = values[i], values[j]
                    if (y1, y2) in last_x:
                        area = (x - last_x[(y1, y2)]) * (y2 - y1)
                        if 0 < area < res:
                            res = area
                    last_x[(y1, y2)] = x
        if res == float('inf'):
            return 0
        return res


examples = [
    {
        "input": {
            "points": [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
        },
        "output": 4
    }, {
        "input": {
            "points": [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
        },
        "output": 2
    }, {
        "input": {
            "points": [[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]
        },
        "output": 2
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
