"""
You are given a map of a server center,
represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:

Input:
    grid = [[1,0],[0,1]]
Output:
    0
Explanation:
    No servers can communicate with others.

Example 2:

Input:
    grid = [[1,0],[1,1]]
Output:
    3
Explanation:
    All three servers can communicate with at least one other server.

Example 3:

Input:
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output:
    4
Explanation:
    The two servers in the first row can communicate with each other.
    The two servers in the third column can communicate with each other.
    The server at right bottom corner can't communicate with any other server.


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1
"""


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        r, c = len(grid), len(grid[0])
        cn = [0 for _ in range(c)]
        cache = {}

        for i in range(r):
            rc, jx = 0, -1
            for j in range(c):
                if grid[i][j]:
                    total += 1
                    rc += 1
                    cn[j] += 1
                    jx = j
            if rc == 1:
                cache[jx] = 1

        for j in cache:
            if cn[j] == 1:
                total -= 1
        return total


examples = [
    {
        "input": {
            "grid": [
                [1, 0],
                [0, 1]
            ],
        },
        "output": 0
    }, {
        "input": {
            "grid": [
                [1, 0],
                [1, 1]
            ],
        },
        "output": 3
    }, {
        "input": {
            "grid": [
                [1, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ],
        },
        "output": 4
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
