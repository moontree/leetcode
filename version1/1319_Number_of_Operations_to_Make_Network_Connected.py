"""
There are n computers numbered from 0 to n-1
connected by ethernet cables connections forming a network
where connections[i] = [a, b] represents a connection between computers a and b.
Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections.
You can extract certain cables between two directly connected computers,
and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected.
If it's not possible, return -1.



Example 1:

Input:
    n = 4, connections = [[0,1],[0,2],[1,2]]
Output:
    1
Explanation:
    Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:

Input:
    n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output:
    2

Example 3:

Input:
    n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output:
    -1
Explanation:
    There are not enough cables.

Example 4:
Input:
    n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output:
    0


Constraints:

    1 <= n <= 10^5
    1 <= connections.length <= min(n*(n-1)/2, 10^5)
    connections[i].length == 2
    0 <= connections[i][0], connections[i][1] < n
    connections[i][0] != connections[i][1]
    There are no repeated connections.
    No two computers are connected by more than one cable.
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
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        dsu = DSU(n)
        for a, b in connections:
            dsu.union(a, b)
        nn = len(connections)
        cache = {}
        for i in range(n):
            cache[dsu.find(i)] = 1
        parts = len(cache)
        return parts - 1 if nn >= n - 1 else -1


examples = [
    {
        "input": {
            "n": 4,
            "connections": [[0, 1], [0, 2], [1, 2]]
        },
        "output": 1
    }, {
        "input": {
            "n": 6,
            "connections": [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
        },
        "output": 2
    }, {
        "input": {
            "n": 6,
            "connections": [[0, 1], [0, 2], [0, 3], [1, 2]]
        },
        "output": -1
    }, {
        "input": {
            "n": 5,
            "connections": [[0, 1], [0, 2], [3, 4], [2, 3]]
        },
        "output": 0
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
