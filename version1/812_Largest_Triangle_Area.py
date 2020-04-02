"""
You have a list of points in the plane.
Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input:
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output:
    2
Explanation:
    The five points are show in the figure below. The red triangle is the largest.

Notes:
    3 <= points.length <= 50.
    No points will be duplicated.
     -50 <= points[i][j] <= 50.
    Answers within 10^-6 of the true value will be accepted as correct.
"""


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def areatri(a, b, c):
            return 0.5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[0] * c[1] + c[0] * b[1] + b[0] * a[1]))
        n = len(points)
        res = 0
        for i in range(n - 2):
            for j in range(i, n - 1):
                for k in range(j, n):
                    v = areatri(points[i], points[j], points[k])
                    if res < v:
                        res = v
        return res



examples = [
    {
        "input": {
            "points": [
                [0, 0],
                [0, 1],
                [1, 0],
                [0, 2],
                [2, 0]
            ]
        },
        "output": 2
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']