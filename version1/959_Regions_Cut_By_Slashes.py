"""
n a N x N grid composed of 1 x 1 squares,
each 1 x 1 square consists of a /, \, or blank space.
These characters divide the square into contiguous regions.

(Note that backslash characters are escaped,
so a \ is represented as "\\".)

Return the number of regions.



Example 1:

Input:
    [
      " /",
      "/ "
    ]
Output:
    2


Example 2:

    Input:
    [
      " /",
      "  "
    ]
Output:
    1

Example 3:

Input:
    [
      "\\/",
      "/\\"
    ]
Output:
    4

Example 4:

Input:
    [
      "/\\",
      "\\/"
    ]
Output:
    5

Example 5:

Input:
    [
      "//",
      "/ "
    ]
Output:
    3


Note:

    1 <= grid.length == grid[0].length <= 30
    grid[i][j] is either '/', '\', or ' '.
"""
class DSU:

    def __init__(self, n):
        self.cache = {i: i for i in xrange(n)}

    def find(self, x):
        if self.cache[x] != x:
            self.cache[x] = self.find(self.cache[x])
        return self.cache[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.cache[b] = a


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m = len(grid)
        n = m * m * 4
        dsu = DSU(n)
        d = 4 * m
        for i in range(m):
            for j in range(m):
                start = i * d + 4 * j
                if grid[i][j] == ' ':
                    dsu.union(start, start + 1)
                    dsu.union(start, start + 2)
                    dsu.union(start, start + 3)
                elif grid[i][j] == '\\':
                    dsu.union(start, start + 3)
                    dsu.union(start + 1, start + 2)
                elif grid[i][j] == '/':
                    dsu.union(start, start + 2)
                    dsu.union(start + 1, start + 3)
                if j > 0:
                    dsu.union(start - 1, start + 2)
                if i > 0:
                    dsu.union(start, start - d + 1)
        res = 0
        for k in dsu.cache:
            if k == dsu.cache[k]:
                res += 1
        return res


examples = [
    {
        "input": {
            "grid": [
                " /",
                "/ "
            ],
        },
        "output": 2
    }, {
        "input": {
            "grid": [
                " /",
                "  "
            ],
        },
        "output": 1
    }, {
        "input": {
            "grid": [
                "\\/",
                "/\\"
            ],
        },
        "output": 4
    }, {
        "input": {
            "grid": [
                "/\\",
                "\\/"
            ],
        },
        "output": 5
    }, {
        "input": {
            "grid": [
                "//",
                "/ "
            ],
        },
        "output": 3
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
