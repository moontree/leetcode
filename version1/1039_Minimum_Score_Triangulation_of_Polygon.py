"""
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.
For each triangle, the value of that triangle is the product of the labels of the vertices,
and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.


Example 1:

Input:
    [1,2,3]
Output:
    6
Explanation:
    The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:

Input:
    [3,7,4,5]
Output:
    144
Explanation:
    There are two triangulations,
    with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
    The minimum score is 144.

Example 3:

Input:
    [1,3,1,4,1,5]
Output:
    13
Explanation:
    The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.


Note:

    3 <= A.length <= 50
    1 <= A[i] <= 100
"""


class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0
            if i + 1 < n:
                dp[i][i + 1] = 0
        for l in range(2, n):
            for i in range(n - l):
                j = l + i
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])
        return dp[0][-1]


examples = [
    {
        "input": {
            "A": [1, 2, 3],
        },
        "output": 6
    }, {
        "input": {
            "A": [3, 7, 4, 5],
        },
        "output": 144
    }, {
        "input": {
            "A": [1, 3, 1, 4, 1, 5],
        },
        "output": 13
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
