"""
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000
"""
import collections


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans


examples = [
    {
        "input": {
            "N": 6,
            "edges": [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]],
        },
        "output": [8, 12, 6, 10, 10, 10]
    }, {
        "input": {
            "N": 3,
            "edges": [[0, 2], [1, 2]],
        },
        "output": [3, 3, 2]
    }, {
        "input": {
            "N": 1,
            "edges": [],
        },
        "output": [0]
    }, {
        "input": {
            "N": 3,
            "edges": [[2, 0], [1, 0]],
        },
        "output": [2, 3, 3]
    }, {
        "input": {
            "N": 3,
            "edges": [[2, 1], [0, 2]],
        },
        "output": [3, 3, 2]
    }, {
        "input": {
            "N": 4,
            "edges": [[1, 2], [3, 0], [0, 2]],
        },
        "output": [4, 6, 4, 6]
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
