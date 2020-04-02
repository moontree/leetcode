"""
=========================
Project -> File: leetcode -> 1192_Critical_Connections_in_a_Network.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/9 5:20 PM
=========================
"""

"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections 
forming a network where connections[i] = [a, b] represents a connection between servers a and b. 
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:

Input: 
    n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: 
    [[1,3]]
Explanation: 
    [[3,1]] is also accepted.
 

Constraints:

    1 <= n <= 10^5
    n-1 <= connections.length <= 10^5
    connections[i][0] != connections[i][1]
    There are no repeated connections.
"""


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        cache = {i: [] for i in range(n)}
        for s, e in connections:
            cache[s].append(e)
            cache[e].append(s)

        dsn, low, visited = [0 for _ in range(n)], [n for _ in range(n)], [0 for _ in range(n)]
        # stack = []
        ans = []

        def helper(i, cnt, p):
            dsn[i] = low[i] = cnt
            visited[i] = 1
            # stack.append(i)
            for nxt in cache[i]:
                if nxt == p:
                    continue
                if not visited[nxt]:
                    helper(nxt, cnt + 1, i)
                    low[i] = min(low[i], low[nxt])
                else:
                    low[i] = min(low[i], low[nxt])
                if low[nxt] > dsn[i]:
                    ans.append([i, nxt])

        for i in range(n):
            if not visited[i]:
                helper(i, 0, -1)

        return ans


examples = [
    {
        "input": {
            "n": 4,
            "connections": [[0, 1], [1, 2], [2, 0], [1, 3]]
        },
        "output": [[1, 3]]
    }, {
        "input": {
            "n": 6,
            "connections": [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
        },
        "output": [[1, 3]]
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
