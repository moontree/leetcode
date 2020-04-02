"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
 is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
 and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


def can_finish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    out_degrees = [0] * numCourses
    pre_nodes = [[] for _ in range(numCourses)]
    for pair in prerequisites:
        out_degrees[pair[1]] += 1
        pre_nodes[pair[0]].append(pair[1])
    queue = []
    for i in range(numCourses):
        if out_degrees[i] == 0:
            queue.append(i)
    k = 0
    while len(queue):
        cur = queue.pop(0)
        k += 1
        for p in pre_nodes[cur]:
            out_degrees[p] -= 1
            if out_degrees[p] == 0:
                queue.append(p)
    return k == numCourses


examples = [
    {
        "num": 2,
        "prerequisites": [
            [1, 0]
        ],
        "res": True
    }, {
        "num": 2,
        "prerequisites": [
            [1, 0],
            [0, 1]
        ],
        "res": False
    }, {
        "num": 3,
        "prerequisites": [
            [1, 0],
            [1, 2],
            [0, 1]
        ],
        "res": False
    }, {
        "num": 4,
        "prerequisites": [
            [0, 1], [3, 1], [1, 3], [3, 2]
        ],
        "res": True
    }, {
        "num": 4,
        "prerequisites": [
            [2, 0], [1, 0], [3, 1], [3, 2], [1, 3]
        ],
        "res": False
    }
]


for example in examples:
    print can_finish(example["num"], example["prerequisites"])
