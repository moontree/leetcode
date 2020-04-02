"""
On a 2D plane, we place stones at some integer coordinate points.
Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Note: move can from different nodes



Example 1:

Input:
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output:
    5

Example 2:

Input:
    stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output:
    3

Example 3:

Input:
    stones = [[0,0]]
Output:
    0

Note:
    1 <= stones.length <= 1000
    0 <= stones[i][j] < 10000
"""


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        cx, cy = {}, {}
        for x, y in stones:
            if x not in cx:
                cx[x] = []
            if y not in cy:
                cy[y] = []
            cx[x].append(y)
            cy[y].append(x)
        meet = {}

        def dfs(x, y):
            if (x, y) in meet:
                return
            meet[(x, y)] = True
            for yy in cx[x]:
                if (x, yy) not in meet:
                    dfs(x, yy)
            for xx in cy[y]:
                if (xx, y) not in meet:
                    dfs(xx, y)

        nodes = 0
        for x, y in stones:
            if (x, y) not in meet:
                dfs(x, y)
                nodes += 1

        return len(stones) - nodes


examples = [
    {
        "input": {
            "stones": [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],
        },
        "output": 5
    }, {
        "input": {
            "stones": [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]],
        },
        "output": 3
    }, {
        "input": {
            "stones": [[0, 0]],
        },
        "output": 0
    }, {
        "input": {
            "stones": [[0, 0], [0, 1]],
        },
        "output": 1
    }, {
        "input": {
            "stones": [[1, 1], [1, 3], [2, 0], [2, 2], [2, 3], [4, 2], [3, 0], [5, 0]],
        },
        "output": 7
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
