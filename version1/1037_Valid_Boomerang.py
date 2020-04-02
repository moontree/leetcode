"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.



Example 1:

Input:
    [[1,1],[2,3],[3,2]]
Output:
    true

Example 2:

Input:
    [[1,1],[2,2],[3,3]]
Output:
    false


Note:

    points.length == 3
    points[i].length == 2
    0 <= points[i][j] <= 100
"""


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        return (points[1][1] - points[0][1]) * (points[2][0] - points[0][0]) !=\
               (points[1][0] - points[0][0]) * (points[2][1] - points[0][1])


examples = [
    {
        "input": {
            "points":  [[1, 1], [2, 3], [3, 2]],
        },
        "output": True
    }, {
        "input": {
            "points": [[1, 1], [2, 2], [3, 3]],
        },
        "output": False
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
