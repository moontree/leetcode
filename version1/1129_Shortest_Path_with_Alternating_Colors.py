"""
Consider a directed graph,
with nodes labelled 0, 1, ..., n-1.
In this graph, each edge is either red or blue,
and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.
Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n,
where each answer[X] is the length of the shortest path from node 0 to node X
such that the edge colors alternate along the path (or -1 if such a path doesn't exist).



Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]

Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]

Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]

Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]


Constraints:

    1 <= n <= 100
    red_edges.length <= 400
    blue_edges.length <= 400
    red_edges[i].length == blue_edges[i].length == 2
    0 <= red_edges[i][j], blue_edges[i][j] < n
"""


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        res = [[float('inf'), float('inf')] for _ in range(n)]
        res[0] = [0, 0]
        r = {i: [] for i in range(n)}
        b = {i: [] for i in range(n)}
        rb = [r, b]
        for s, t in red_edges:
            r[s].append(t)
        for s, t in blue_edges:
            b[s].append(t)
        step = 0
        q = [[0, 0], [0, 1]]
        while q:
            tmp = []
            for s, c in q:
                for t in rb[c][s]:
                    if res[t][c] > step + 1:
                        tmp.append([t, 1 - c])
                        res[t][c] = step + 1
            q = tmp[:]
            step += 1
        res = [min(item) for item in res]
        res = [-1 if v == float('inf') else v for v in res]
        return res


examples = [
    {
        "input": {
            "n": 3,
            "red_edges": [[0, 1], [1, 2]],
            "blue_edges": []
        },
        "output": [0, 1, -1]
    }, {
        "input": {
            "n": 3,
            "red_edges": [[0, 1]],
            "blue_edges": [[2, 1]]
        },
        "output": [0, 1, -1]
    }, {
        "input": {
            "n": 3,
            "red_edges": [[1, 0]],
            "blue_edges": [[2, 1]]
        },
        "output": [0, -1, -1]
    },  {
        "input": {
            "n": 3,
            "red_edges": [[0, 1]],
            "blue_edges": [[1, 2]]
        },
        "output": [0, 1, 2]
    },  {
        "input": {
            "n": 3,
            "red_edges": [[0, 1], [0, 2]],
            "blue_edges": [[1, 0]]
        },
        "output": [0, 1, 1]
    }, {
        "input": {
            "n": 5,
            "red_edges": [[0, 1], [1, 2], [2, 3], [3, 4]],
            "blue_edges": [[1, 2], [2, 3], [3, 1]]
        },
        "output": [0, 1, 2, 3, 7]
    }, {
        "input": {
            "n": 5,
            "red_edges": [[3, 2], [4, 1], [1, 4], [2, 4]],
            "blue_edges": [[2, 3], [0, 4], [4, 3], [4, 4], [4, 0], [1, 0]]

        },
        "output": [0, 2, -1, -1, 1]
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
