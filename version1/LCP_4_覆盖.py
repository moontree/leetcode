# --*-- encoding: utf-8 --*--
"""
你有一块棋盘，棋盘上有一些格子已经坏掉了。
你还有无穷块大小为1 * 2的多米诺骨牌，
你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？

这些骨牌可以横着或者竖着放。

输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。

输出：一个整数，代表最多能在棋盘上放的骨牌数。


示例 1：

输入：
    n = 2, m = 3, broken = [[1, 0], [1, 1]]
输出：
    2
解释：
    我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）

示例 2：

输入：
    n = 3, m = 3, broken = []
输出：
    4
解释：
    下图是其中一种可行的摆放方式

限制：

    1 <= n <= 8
    1 <= m <= 8
    0 <= b <= n * m

"""


class Solution(object):
    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """

        if len(broken) == 0:
            return n * m / 2
        grid = [[1 for _ in range(m)] for _ in range(n)]
        a, b = {}, {}
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    a[(i, j)] = 1
                else:
                    b[(i, j)] = 1
        # grid = [[0 for _ in range(m)] for _ in range(n)]
        for i, j in broken:
            grid[i][j] = 0
            if (i + j) % 2 == 0:
                del a[(i, j)]
            else:
                del b[(i, j)]
        used = {}
        visited = {}
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def find(key):
            # print('-----find -----', i, j)
            for d in directions:
                ni, nj = key[0] + d[0], key[1] + d[1]
                value = (ni, nj)
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] and (not visited.get(value, False)):
                    visited[value] = True
                    if (not used.get(value, None)) or find(used[value]):
                        used[value] = key
                        return True
            return False

        res = 0

        for i, j in a:
            visited = {}
            if find((i, j)):
                res += 1
        return res


examples = [
    {
        "input": {
            "n": 2,
            "m": 3,
            "broken": [[1, 0], [1, 1]]
        },
        "output": 2
    },
    {
        "input": {
            "n": 3,
            "m": 3,
            "broken": []
        },
        "output": 4
    }, {
        "input": {
            "n": 4,
            "m": 4,
            "broken": []
        },
        "output": 8
    }, {
        "input": {
            "n": 8,
            "m": 8,
            "broken": [[0, 1], [2, 0], [4, 3], [4, 7], [5, 4]]

        },
        "output": 28
    }, {
        "input": {
            "n": 8,
            "m": 8,
            "broken": []

        },
        "output": 32
    }, {
        "input": {
            "n": 8,
            "m": 8,
            "broken": [
                [1, 0], [2, 5], [3, 1], [3, 2], [3, 4],
                [4, 0], [4, 3], [4, 6], [4, 7], [5, 3],
                [5, 5], [5, 6], [6, 3], [7, 2], [7, 7]
            ]
        },
        "output": 23
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
