"""
=========================
Project -> File: leetcode -> 789_Escape_The_Ghosts.py
Author: zhangchao
=========================
You are playing a simplified Pacman game.
You start at the point (0, 0), and your destination is (target[0], target[1]).
There are several ghosts on the map,
the i-th ghost starts at (ghosts[i][0], ghosts[i][1]).

Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions:
north, east, west, or south, going from the previous point to a new point 1 unit of distance away.

You escape if and only if you can reach the target before any ghost reaches you
(for any given moves the ghosts may take.)
If you reach any square (including the target) at the same time as a ghost,
it doesn't count as an escape.

Return True if and only if it is possible to escape.

Example 1:
Input:
    ghosts = [[1, 0], [0, 3]]
    target = [0, 1]
Output:
    true
Explanation:
    You can directly reach the destination (0, 1) at time 1,
    while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.

Example 2:
Input:
    ghosts = [[1, 0]]
    target = [2, 0]
Output:
    false
Explanation:
    You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

Example 3:
Input:
    ghosts = [[2, 0]]
    target = [1, 0]
Output:
    false
Explanation:
    The ghost can reach the target at the same time as you.
Note:

    All points have coordinates with absolute value <= 10000.
    The number of ghosts will not exceed 100.
"""


class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        dis = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if (abs(target[0] - x) + abs(target[1] - y)) <= dis:
                return False
        return True


examples = [
    {
        "input": {
            "ghosts": [[1, 0], [0, 3]],
            "target": [0, 1]
        },
        "output": True
    }, {
        "input": {
            "ghosts": [[1, 0]],
            "target": [2, 0]
        },
        "output": False
    }, {
        "input": {
            "ghosts": [[2, 0]],
            "target": [1, 0]
        },
        "output": False
    }, {
        "input": {
            "ghosts": [[1, 9], [2, -5], [3, 8], [9, 8], [-1, 3]],
            "target": [8, -10]
        },
        "output": False
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
