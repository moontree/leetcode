"""
=========================
Project -> File: leetcode -> 1377_Frog_Position_After_T_Seconds.py
Author: zhangchao
=========================
Given an undirected tree consisting of n vertices numbered from 1 to n.
A frog starts jumping from the vertex 1.
In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected.
The frog can not jump back to a visited vertex.
In case the frog can jump to several vertices it jumps randomly to one of them with the same probability,
otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges,
where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.


Example 1:

Input:
    n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output:
    0.16666666666666666
Explanation:
    The figure above shows the given graph.
    The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1
    and then jumping with 1/2 probability to vertex 4 after second 2.
    Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666.

Example 2:

Input:
    n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output:
    0.3333333333333333
Explanation:
    The figure above shows the given graph.
    The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1.

Example 3:

Input:
    n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output:
    0.16666666666666666


Constraints:

    1 <= n <= 100
    edges.length == n-1
    edges[i].length == 2
    1 <= edges[i][0], edges[i][1] <= n
    1 <= t <= 50
    1 <= target <= n
    Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        cache = {i: [] for i in range(n + 1)}
        for s, tt in edges:
            cache[s].append(tt)
            cache[tt].append(s)
        reached = [0 for _ in range(n + 1)]
        q = [[1, 1.]]
        reached[1] = 1
        while t:
            tmp = []
            for cur, prob in q:
                nxts = [v for v in cache[cur] if not reached[v]]
                p = 1. / len(nxts) if len(nxts) else 1
                for nxt in nxts:
                    reached[nxt] = 1
                    tmp.append([nxt, prob * p])
                if not nxts:
                    if cur == target:
                        return prob
                    tmp.append([cur, prob])
            q = tmp
            t -= 1
        for tt, p in q:
            if tt == target:
                return p
        return 0


examples = [
    {
        "input": {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 2,
            "target": 4
        },
        "output": 0.16666666666666666
    }, {
        "input": {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 1,
            "target": 7
        },
        "output": 0.3333333333333333
    }, {
        "input": {
            "n": 7,
            "edges": [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            "t": 20,
            "target": 6
        },
        "output": 0.16666666666666666
    }, {
        "input": {
            "n": 3,
            "edges": [[2, 1], [3, 2]],
            "t": 1,
            "target": 2
        },
        "output": 1
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
