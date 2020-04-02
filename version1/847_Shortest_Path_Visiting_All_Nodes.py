"""
=========================
Project -> File: leetcode -> 847_Shortest_Path_Visiting_All_Nodes.py
Author: zhangchao
=========================
An undirected,
connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N,
and j != i is in the list graph[i] exactly once,
if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node.
You may start and stop at any node,
you may revisit nodes multiple times,
and you may reuse edges.


Example 1:

Input:
    [[1,2,3],[0],[0],[0]]
Output:
    4
Explanation:
    One possible path is [1,0,2,0,3]

Example 2:

Input:
    [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output:
    4
Explanation:
    One possible path is [0,1,4,2,3]


Note:

    1 <= graph.length <= 12
    0 <= graph[i].length < graph.length
"""


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        target = 2 ** n - 1
        q = [[1 << i, i] for i in range(n)]
        used = {(a, b): 1 for a, b in q}
        step = 0
        while True:
            tmp = []
            for v, head in q:
                if v == target:
                    return step
                for x in graph[head]:
                    nv = v | (1 << x)
                    if (nv, x) in used:
                        pass
                    else:
                        used[(nv, x)] = 1
                        tmp.append([nv, x])
            q = tmp
            step += 1


examples = [
    {
        "input": {
            "graph": [[1, 2, 3], [0], [0], [0]],
        },
        "output": 4
    }, {
        "input": {
            "graph": [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]],
        },
        "output": 4
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
