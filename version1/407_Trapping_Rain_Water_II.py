"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""
import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        res = 0
        r, c = len(heightMap), len(heightMap[0])
        if r < 3 or c < 3:
            return 0
        cache = {}
        q = []
        for i in range(r):
            cache[(i, 0)] = 1
            cache[(i, c - 1)] = 1
            q.append([heightMap[i][0], i, 0])
            q.append([heightMap[i][c - 1], i, c - 1])
        for j in range(1, c - 1):
            cache[(0, j)] = 1
            cache[(r - 1, j)] = 1
            q.append([heightMap[0][j], 0, j])
            q.append([heightMap[r - 1][j], r - 1, j])
        heapq.heapify(q)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            h, i, j = heapq.heappop(q)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in cache:
                    cache[(ni, nj)] = 1
                    if h < heightMap[ni][nj]:
                        heapq.heappush(q, [heightMap[ni][nj], ni, nj])
                    else:
                        res += h - heightMap[ni][nj]
                        heapq.heappush(q, [h, ni, nj])
        return res


examples = [
    {
        "input": {
            "heightMap": [
                [1, 4, 3, 1, 3, 2],
                [3, 2, 1, 3, 2, 4],
                [2, 3, 3, 2, 3, 1]
            ],
        },
        "output": 4
    }, {
        "input": {
            "heightMap": [
                [1, 4, 3, 1, 3, 2],
                [3, 2, 1, 1, 2, 4],
                [2, 3, 3, 2, 3, 1]
            ],
        },
        "output": 0
    }, {
        "input": {
            "heightMap": [
                [5, 8, 7, 7],
                [5, 2, 1, 5],
                [7, 1, 7, 1],
                [8, 9, 6, 9],
                [9, 8, 9, 9]
            ],
        },
        "output": 12
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
