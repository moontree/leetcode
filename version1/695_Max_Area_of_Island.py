"""
Given a non-empty 2D array grid of 0's and 1's,
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        used = [[False for _ in range(c)] for _ in range(r)]
        cache = {0: 0}
        
        def helper(i, j, p):
            # print i, j, p, grid[i][j], cache
            if 0 <= i < r and 0 <= j < c and not used[i][j] and grid[i][j] == 1:
                used[i][j] = True
                cache[p] += 1
                helper(i - 1, j, p)
                helper(i + 1, j, p)
                helper(i, j - 1, p)
                helper(i, j + 1, p)
        idx = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and not used[i][j]:
                    idx += 1
                    cache[idx] = 0
                    helper(i, j, idx)
                else:
                    used[i][j] = True
        
        return max(cache.values())
    

examples = [
    {
        "input": [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ], 
        "output": 6
    }
]


if __name__ == '__main__':
    solution = Solution()
    print(dir(solution))
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print func(example['input']) == example['output']