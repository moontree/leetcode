"""
You have N gardens, labelled 1 to N.
In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that,
for any two gardens connected by a path,
they have different types of flowers.

Return any such a choice as an array answer,
where answer[i] is the type of flower planted in the (i+1)-th garden.
The flower types are denoted 1, 2, 3, or 4.
It is guaranteed an answer exists.

Example 1:

Input:
    N = 3, paths = [[1,2],[2,3],[3,1]]
Output:
    [1,2,3]

Example 2:

Input:
    N = 4, paths = [[1,2],[3,4]]
Output:
    [1,2,1,2]

Example 3:

Input:
    N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output:
    [1,2,3,4]

Note:

    1 <= N <= 10000
    0 <= paths.size <= 20000
    No garden has 4 or more paths coming into or leaving it.
    It is guaranteed an answer exists.
"""


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        cache = {i + 1: [] for i in range(N)}
        for s, t in paths:
            cache[s].append(t)
            cache[t].append(s)
        colors = [[0, 0, 0, 0] for _ in range(N + 1)]
        res = [0 for _ in range(N + 1)]
        nodes = [[i, len(cache[i])] for i in range(1, N + 1)]
        nodes.sort(key=lambda x: -x[1])
        for i, l in nodes:
            if res[i] == 0:
                for c in range(4):
                    if colors[i][c] == 0:
                        res[i] = c + 1
                        colors[i][c] = 1
                        for t in cache[i]:
                            colors[t][c] = 1
                        break
        return res[1:]


examples = [
    {
        "input": {
            "N": 3,
            "paths": [[1, 2], [2, 3], [3, 1]],
        },
        "output": [1, 2, 3]
    }, {
        "input": {
            "N": 4,
            "paths": [[1, 2], [3, 4]],
        },
        "output": [1, 2, 1, 2]
    }, {
        "input": {
            "N": 4,
            "paths": [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]],
        },
        "output": [1, 2, 3, 4]
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
