"""
In this problem, a rooted tree is a directed graph such that,
there is exactly one node (the root) for which all other nodes are descendants of this node,
plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N),
with one additional directed edge added.
The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges.
Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v,
where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input:
    [[1,2], [1,3], [2,3]]
Output:
    [2,3]
Explanation:
    The given directed graph will be like this:
      1
     / \
    v   v
    2-->3

Example 2:
Input:
    [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output:
    [4,1]
Explanation:
    The given directed graph will be like this:
    5 <- 1 -> 2
         ^    |
         |    v
         4 <- 3
Note:
    The size of the input 2D-array will be between 3 and 1000.
    Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""
class DSU:

    def __init__(self, n):
        self.cache = {i: i for i in xrange(n)}

    def find(self, x):
        if self.cache[x] != x:
            self.cache[x] = self.find(self.cache[x])
        return self.cache[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.cache[b] = a


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def helper(remove_i):
            n = len(edges) + 1
            dsu = DSU(n)
            cnt = n - 1
            for i, (s, t) in enumerate(edges):
                if i == remove_i:
                    continue
                ps, pt = dsu.find(s), dsu.find(t)
                if ps != pt:
                    cnt -= 1
                    dsu.union(s, t)
            return cnt == 1

        # in degree is 2
        cache = {}
        for i, (s, t) in enumerate(edges):
            if t not in cache:
                cache[t] = i
            else:
                if helper(i):
                    return [s, t]
                else:
                    return edges[cache[t]]

        n = len(edges) + 1
        dsu = DSU(n)
        for s, t in edges:
            ps, pt = dsu.find(s), dsu.find(t)
            if ps != pt:
                dsu.union(s, t)
            else:
                return [s, t]


examples = [
    {
        "input": {
            "edges": [[1, 2], [1, 3], [2, 3]],
        },
        "output": [2, 3]
    }, {
        "input": {
            "edges": [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
        },
        "output": [4, 1]
    }, {
        "input": {
            "edges": [[2, 1], [3, 1], [4, 2], [1, 4]],
        },
        "output": [2, 1]
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
