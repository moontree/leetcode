"""
There are some trees,
where each tree is represented by (x,y) coordinate in a two-dimensional garden.
Your job is to fence the entire garden using the minimum length of rope as it is expensive.
The garden is well fenced only if all the trees are enclosed.
Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.


Example 1:

Input:
    [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output:
    [[1,1],[2,0],[4,2],[3,3],[2,4]]


Example 2:

Input:
    [[1,2],[2,2],[4,2]]
Output:
    [[1,2],[2,2],[4,2]]

Even you only have trees in a line, you need to use rope to enclose them.

Note:
    All trees should be enclosed together.
    You cannot cut the rope to enclose trees that will separate them in more than one group.
    All input integers will range from 0 to 100.
    The garden has at least one tree.
    All coordinates are distinct.
    Input points have NO order. No order required for output.
"""


class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(points)
        if n < 3:
            return points
        pts = [(x, y) for x, y in points]
        pts.sort()
        cross = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        low = []
        for p in pts:
            while len(low) > 1 and cross(low[-2], low[-1], p) < 0:
                low.pop()
            low.append(p)

        up = []
        for p in reversed(pts):
            while len(up) > 1 and cross(up[-2], up[-1], p) < 0:
                up.pop()
            up.append(p)

        return list(set(low[:-1] + up[:-1]))


examples = [
    {
        "input": {
            "points": [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
        },
        "output": [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]
    }, {
        "input": {
            "points": [[1, 2], [2, 2], [4, 2]]
        },
        "output": [[1, 2], [2, 2], [4, 2]]
    }, {
        "input": {
            "points": [[0, 2], [1, 1], [2, 2], [2, 4], [4, 2], [3, 3]]
        },
        "output": [[2, 4], [3, 3], [4, 2], [0, 2], [1, 1]]
    }, {
        "input": {
            "points": [
                [3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5],
                [4, 5], [3, 5], [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]
            ]
        },
        "output": [[0, 3], [6, 1], [3, 5], [7, 2], [5, 0], [1, 4], [1, 2], [7, 3], [4, 5],
                   [5, 5], [6, 5], [4, 0], [3, 0], [2, 1], [2, 5], [7, 4]]
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
