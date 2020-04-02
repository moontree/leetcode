"""
In a 1 million by 1 million grid,
the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.
Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.


Example 1:

Input:
    blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output:
    false
Explanation:
    The target square is inaccessible starting from the source square, because we can't walk outside the grid.

Example 2:

Input:
    blocked = [], source = [0,0], target = [999999,999999]
Output:
    true
Explanation:
    Because there are no blocked cells, it's possible to reach the target square.

Note:
    0 <= blocked.length <= 200
    blocked[i].length == 2
    0 <= blocked[i][j] < 10^6
    source.length == target.length == 2
    0 <= source[i][j], target[i][j] < 10^6
    source != target
"""


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        # block is small, change to s or t in block wrap
        nn = 10 ** 6
        blocks = {(i, j): True for i, j in blocked}
        n = len(blocked)
        end = n * n

        def helper(s, t):
            c = 1
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            used = {}
            q = [s]
            while q:
                i, j = q.pop(0)
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if (ni == t[0] and nj == t[1]) or (c > end):
                        return True
                    if 0 <= ni < nn and 0 <= nj < nn and (ni, nj) not in blocks and (ni, nj) not in used:
                        c += 1
                        q.append([ni, nj])
                        used[(ni, nj)] = True
            if len(q) == 0:
                return False

        return helper(source, target) and helper(target, source)


examples = [
    {
        "input": {
            "blocked": [[0, 1], [1, 0]],
            "source": [0, 0],
            "target": [0, 2]
        },
        "output": False
    }, {
        "input": {
            "blocked": [],
            "source": [0, 0],
            "target": [999999, 999999]
        },
        "output": True
    }, {
        "input": {
            "blocked": [[100059,100063],[100060,100064],[100061,100065],[100062,100066],[100063,100067],[100064,100068],[100065,100069],[100066,100070],[100067,100071],[100068,100072],[100069,100073],[100070,100074],[100071,100075],[100072,100076],[100073,100077],[100074,100078],[100075,100079],[100076,100080],[100077,100081],[100078,100082],[100079,100083],[100080,100082],[100081,100081],[100082,100080],[100083,100079],[100084,100078],[100085,100077],[100086,100076],[100087,100075],[100088,100074],[100089,100073],[100090,100072],[100091,100071],[100092,100070],[100093,100069],[100094,100068],[100095,100067],[100096,100066],[100097,100065],[100098,100064],[100099,100063],[100098,100062],[100097,100061],[100096,100060],[100095,100059],[100094,100058],[100093,100057],[100092,100056],[100091,100055],[100090,100054],[100089,100053],[100088,100052],[100087,100051],[100086,100050],[100085,100049],[100084,100048],[100083,100047],[100082,100046],[100081,100045],[100080,100044],[100079,100043],[100078,100044],[100077,100045],[100076,100046],[100075,100047],[100074,100048],[100073,100049],[100072,100050],[100071,100051],[100070,100052],[100069,100053],[100068,100054],[100067,100055],[100066,100056],[100065,100057],[100064,100058],[100063,100059],[100062,100060],[100061,100061],[100060,100062]],
            "source": [100079,100063],
            "target": [999948,999967]
        },
        "output": False
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
