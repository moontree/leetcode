"""
For a undirected graph with tree characteristics, we can choose any node as the root.
 The result graph is then a rooted tree.
 Among all possible rooted trees,
  those with minimum height are called minimum height trees (MHTs).
   Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
 You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
 Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

"""


def find_min_height_trees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if len(edges) != n - 1:
        return []
    if n == 1:
        return [0]
    links = {}
    for x, y in edges:
        links[x] = links.get(x, []) + [y]
        links[y] = links.get(y, []) + [x]
    leaves = [k for k in xrange(n) if len(links[k]) == 1]
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            j = links[leaf].pop()
            links[j].remove(leaf)
            if len(links[j]) == 1:
                new_leaves.append(j)
        leaves = new_leaves
    return leaves


examples = [
    {
        "n": 4,
        "edges": [[1, 0], [1, 2], [1, 3]],
        "res": [1]
    }, {
        "n": 6,
        "edges": [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]],
        "res": [3, 4]
    }, {
        "n": 2,
        "edges": [[0, 1]],
        "res": [0, 1]
    }, {
        "n": 1,
        "edges": [],
        "res": [0]
    }
]


for example in examples:
    print find_min_height_trees(example["n"], example["edges"])
