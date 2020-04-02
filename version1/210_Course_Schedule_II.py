"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders,
 you just need to return one of them.
 If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take.
 To take course 1 you should have finished course 0.
 So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take.
To take course 3 you should have finished both courses 1 and 2.
 Both courses 1 and 2 should be taken after you finished course 0.
  So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
"""


def find_order(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    in_degrees = [0] * numCourses
    pre_nodes = [[] for _ in range(numCourses)]
    for pair in prerequisites:
        in_degrees[pair[0]] += 1
        pre_nodes[pair[1]].append(pair[0])
    queue = []
    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)
    k = 0
    res = []
    while len(queue):
        cur = queue.pop(0)
        res.append(cur)
        k += 1
        for p in pre_nodes[cur]:
            in_degrees[p] -= 1
            if in_degrees[p] == 0:
                queue.append(p)
    if k == numCourses:
        return res
    else:
        return []


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
    print find_order(example["num"], example["prerequisites"])
