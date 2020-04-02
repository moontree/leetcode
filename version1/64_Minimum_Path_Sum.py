"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1, 2, 1, 1, 1 minimizes the sum.

"""


def min_path_sum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    nums = [grid[0][0]] * n
    for j in range(1, n):
        nums[j] = nums[j - 1] + grid[0][j]
    for i in range(1, m):
        nums[0] += grid[i][0]
        for j in range(1, n):
            nums[j] = min(nums[j - 1], nums[j]) + grid[i][j]
    return nums[-1]


examples = [
    {
        "grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        "paths": 7
    }, {
        "grid": [[1, 2], [5, 6], [1, 1]],
        "paths": 7
    }
]


for example in examples:
    print min_path_sum(example["grid"])
