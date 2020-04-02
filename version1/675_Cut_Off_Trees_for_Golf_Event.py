"""
You are asked to cut off trees in a forest for a golf event.
The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through,
and this positive number represents the tree's height.

You are asked to cut off all the trees in this forest in the order of tree's height
- always cut off the tree with lowest height first.
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and
you should output the minimum steps you need to walk to cut off all the trees.
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input:
    [
     [1,2,3],
     [0,0,4],
     [7,6,5]
    ]
Output:
    6


Example 2:

Input:
    [
     [1,2,3],
     [0,0,0],
     [7,6,5]
    ]
Output:
    -1


Example 3:

Input:
    [
     [2,3,4],
     [0,0,5],
     [8,7,6]
    ]
Output:
    6
Explanation:
    You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.


    Hint: size of the given matrix will not exceed 50x50.
"""


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        r, c = len(forest), len(forest[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def helper(x1, y1, x2, y2):
            used = [[0 for _ in range(c)] for _ in range(r)]
            used[x1][y1] = 1
            q = [(x1, y1)]
            step = 0
            while q:
                tmp = []
                for x, y in q:
                    if x == x2 and y == y2:
                        return step
                    for d in directions:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < r and 0 <= ny < c and forest[nx][ny] and not used[nx][ny]:
                            tmp.append([nx, ny])
                            used[nx][ny] = 1
                q = tmp
                if len(q) == 0:
                    return -1
                step += 1

        pairs = [(i, j, forest[i][j]) for i in range(r) for j in range(c) if forest[i][j]]
        pairs.sort(key=lambda x: x[-1])
        d = 0
        cx, cy = 0, 0
        for x, y, _ in pairs:
            step = helper(cx, cy, x, y)
            if step < 0:
                return -1
            d += step
            cx, cy = x, y
        return d


examples = [
    {
        "input": {
            "forest": [
                [1, 2, 3],
                [0, 0, 4],
                [7, 6, 5]
            ],
        },
        "output": 6
    }, {
        "input": {
            "forest": [
                [1, 2, 3],
                [0, 0, 0],
                [7, 6, 5]
            ],
        },
        "output": -1
    }, {
        "input": {
            "forest": [
                [1, 2, 3],
                [0, 0, 4],
                [7, 6, 5]
            ],
        },
        "output": 6
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
