"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and
 the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
import collections


def pacific_atlantic(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    pacific = [[0 for _ in xrange(n)] for _ in xrange(m)]
    atlantic = [[0 for _ in xrange(n)] for _ in xrange(m)]
    pacific_start = [(i, 0) for i in xrange(m)] + [(0, j) for j in xrange(1, n)]
    atlantic_start = [(i, n - 1) for i in xrange(m)] + [(m - 1, j) for j in xrange(n - 1)]


    def dfs(reached, i, j):
        if reached[i][j]:
            return
        reached[i][j] = 1
        if i - 1 >= 0 and not reached[i - 1][j] and matrix[i - 1][j] >= matrix[i][j]:
            dfs(reached, i - 1, j)
        if i + 1 < m and not reached[i + 1][j] and matrix[i + 1][j] >= matrix[i][j]:
            dfs(reached, i + 1, j)
        if j - 1 >= 0 and not reached[i][j - 1] and matrix[i][j - 1] >= matrix[i][j]:
            dfs(reached, i, j - 1)
        if j + 1 < n and not reached[i][j + 1] and matrix[i][j + 1] >= matrix[i][j]:
            dfs(reached, i, j + 1)

    for i, j in pacific_start:
        dfs(pacific, i, j)
    for i, j in atlantic_start:
        dfs(atlantic, i, j)


    # def bfs(start):
    #     res = set(start)
    #     q = start[:]
    #     while q:
    #         i, j = q.pop(0)
    #         for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    #             ni, nj = i + di, j + dj
    #             if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] >= matrix[i][j] and (ni, nj) not in res:
    #                 q.append((ni, nj))
    #                 res.add((ni, nj))
    #     return res
    #
    # pacific_set = bfs(pacific_start)
    # atlantic_set = bfs(atlantic_start)
    # return list(pacific_set & atlantic_set)

    return [[i, j] for i in xrange(m) for j in xrange(n) if pacific[i][j] and atlantic[i][j]]


examples = [
    {
        "matrix": [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ],
        "res": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    }, {
        "matrix": [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ],
        "res": [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 2], [2, 1]]
    }, {
        "matrix": [[19,12,0,19,17,4,13,10,6,1,7,18,2,17,0,18,0,18,8,9,19,4,5,4,12,18,17,8,3,15,12,4,11],[5,9,10,19,4,8,5,4,9,14,16,5,7,16,6,19,12,9,1,5,18,8,3,19,8,11,15,11,15,19,13,13,14],[4,1,18,13,7,1,16,11,11,18,5,7,10,8,9,17,10,12,17,11,13,3,18,10,17,6,3,16,13,13,5,7,12],[11,5,19,15,16,19,14,15,6,10,17,5,19,19,17,16,12,12,19,13,3,18,0,4,7,3,12,2,16,6,17,19,18],[4,7,16,12,9,11,15,10,16,5,2,4,12,6,1,14,12,18,7,4,3,17,17,11,5,1,19,19,1,0,4,4,7],[19,8,16,9,14,5,15,11,15,12,5,10,19,14,10,11,13,15,8,8,2,14,6,2,2,7,1,5,19,10,14,3,4]],
        "res": [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 2], [2, 1]]
    }
]


for example in examples:
    print "---"
    print pacific_atlantic(example["matrix"])