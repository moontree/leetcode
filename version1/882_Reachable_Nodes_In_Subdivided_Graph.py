"""
=========================
Project -> File: leetcode -> 882_Reachable_Nodes_In_Subdivided_Graph.py
Author: zhangchao
=========================
Starting with an undirected graph (the "original graph") with nodes from 0 to N-1,
subdivisions are made to some of the edges.

The graph is given as follows:
edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

and n is the total number of new nodes on that edge.

Then, the edge (i, j) is deleted from the original graph,
n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

Now, you start at node 0 from the original graph, and in each move, you travel along one edge.

Return how many nodes you can reach in at most M moves.


Example 1:

Input:
    edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
Output:
    13
Explanation:
    The nodes that are reachable in the final graph after M = 6 moves are indicated below.

Example 2:

Input:
    edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
Output:
    23

Note:

    0 <= edges.length <= 10000
    0 <= edges[i][0] < edges[i][1] < N
    There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
    The original graph has no parallel edges.
    0 <= edges[i][2] <= 10000
    0 <= M <= 10^9
    1 <= N <= 3000
    A reachable node is a node that can be travelled to using at most M moves starting from node 0.
"""
import heapq
import collections


class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1
            for nxt, weight in graph[node].iteritems():

                v = min(weight, M - d)
                used[node, nxt] = v

                # d2 is the total distance to reach 'nei' (nei***or) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nxt, M + 1):
                    heapq.heappush(pq, (d2, nxt))
                    dist[nxt] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans


examples = [
    {
        "input": {
            "edges": [[0, 1, 10], [0, 2, 1], [1, 2, 2]],
            "M": 6,
            "N": 3
        },
        "output": 13
    }, {
        "input": {
            "edges": [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]],
            "M": 10,
            "N": 4
        },
        "output": 23
    }, {
        "input": {
            "edges": [[2, 4, 2], [3, 4, 5], [2, 3, 1], [0, 2, 1], [0, 3, 5]],
            "M": 14,
            "N": 5
        },
        "output": 18
    }, {
        "input": {
            "edges": [[1, 2, 5], [0, 3, 3], [1, 3, 2], [2, 3, 4], [0, 4, 1]],
            "M": 7,
            "N": 5
        },
        "output": 13
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
