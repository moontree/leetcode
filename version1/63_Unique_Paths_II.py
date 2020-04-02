"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
"""


def unique_paths_with_obstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    paths = []
    for i in range(m):
        paths.append([0] * n)
    paths[0][0] = 1 - obstacleGrid[0][0]
    for i in range(1, m):
        paths[i][0] = (1 - obstacleGrid[i][0]) and paths[i - 1][0]
    for j in range(1, n):
        paths[0][j] = (1 - obstacleGrid[0][j]) and paths[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            paths[i][j] = (1 - obstacleGrid[i][j]) and paths[i - 1][j] + paths[i][j - 1]
    return paths[-1][-1]


examples = [
    {
        "grid": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        "paths": 2
    }, {
        "grid": [[0, 0, 0], [1, 1, 0], [0, 0, 0]],
        "paths": 1
    }, {
        "grid": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
        "paths": 0
    }
]


for example in examples:
    print unique_paths_with_obstacles(example["grid"])
