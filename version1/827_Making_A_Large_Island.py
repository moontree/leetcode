"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input:
    [[1, 0], [0, 1]]
Output:
    3
Explanation:
    Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input:
    [[1, 1], [1, 0]]
Output:
    4
Explanation:
    Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input:
    [[1, 1], [1, 1]]
Output:
    4
Explanation:
    Can't change any 0 to 1, only one island with area = 4.


Notes:

    1 <= grid.length = grid[0].length <= 50.
    0 <= grid[i][j] <= 1.

"""


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        status = [[0 for _ in range(c)] for _ in range(r)]
        block = 1
        cache = {1: 0}

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c:
                pass
            else:
                return
            if status[i][j] == 0 and grid[i][j] == 1:
                status[i][j] = block
                cache[block] += 1
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] and status[i][j] == 0:
                    cache[block] = 0
                    dfs(i, j)
                    block += 1
        #
        # for row in status:
        #     print row
        # print cache
        if cache[1] == r * c:
            return cache[1]
        res = 0

        def helper(i, j):
            if 0 <= i < r and 0 <= j < c:
                if grid[i][j] == 0:
                    return 0, 0
                else:
                    return status[i][j], cache[status[i][j]]
            return 0, 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(r):
            for j in range(c):
                tmp = {}

                if grid[i][j] == 0:
                    for direction in directions:
                        k, v = helper(i + direction[0], j + direction[1])
                        tmp[k] = v
                    cc = sum(tmp.values()) + 1
                    if res < cc:
                        res = cc
        return res


examples = [
    {
        "input": {
            "grid": [[1, 0], [0, 1]]
        },
        "output": 3
    },  {
        "input": {
            "grid": [[1, 1], [1, 0]]
        },
        "output": 4
    },  {
        "input": {
            "grid": [[1, 1], [1, 1]]
        },
        "output": 4
    },  {
        "input": {
            "grid": [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 0],
                [0, 1, 1, 1, 1, 0, 0]
            ]
        },
        "output": 18
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
        v = func(**example['input'])
        print v, v == example['output']