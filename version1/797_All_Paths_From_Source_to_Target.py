"""
Given a directed, acyclic graph of N nodes.
Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:
the nodes are 0, 1, ..., graph.length - 1.
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths = [[0]]
        res = []
        while True:
            tmp = []
            appended = False
            for path in paths:
                cur = path[-1]
                if cur == len(graph) - 1:
                    res.append(path)
                else:
                    for idx in graph[cur]:
                        new_path = path[:] + [idx]
                        tmp.append(new_path)
                        appended = True
            if not appended:
                break
            paths = tmp[:]
        print res
        return res


examples = [
    {
        "input": {
            "graph": [
                [1, 2],
                [2, 3],
                [3],
                []
            ]
        },
        "output": [
            [0, 1, 3],
            [0, 2, 3]
        ]
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']