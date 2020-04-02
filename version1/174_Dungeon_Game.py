"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid.
 Our valiant knight (K) was initially positioned in the top-left room and
  must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers)
 upon entering these rooms; other rooms are either empty (0's)
  or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible,
 the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below,
the initial health of the knight must be at least 7
if he follows the optimal path RIGHT -> RIGHT ->DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and
the bottom-right room where the princess is imprisoned.
"""


def calculate_minimum_hp(dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    m, n = len(dungeon), len(dungeon[0])
    hps = [[1 for _ in range(n)] for _ in range(m)]
    hps[-1][-1] = max(1, 1 - dungeon[-1][-1])
    for i in range(m - 1)[::-1]:
        hps[i][-1] = max(1, hps[i + 1][-1] - dungeon[i][-1])
    for j in range(n - 1)[::-1]:
        hps[-1][j] = max(hps[-1][j + 1] - dungeon[-1][j], 1)
    for i in range(m - 1)[::-1]:
        for j in range(n - 1)[::-1]:
            hps[i][j] = max(min(hps[i + 1][j], hps[i][j + 1]) - dungeon[i][j], 1)
    for p in hps:
        print p
    return hps[0][0]


examples = [
    {
        "dungeon": [
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5],
        ],
        "res": 7
    }, {
        "dungeon": [
            [1, -3, 3],
            [0, -2, 0],
            [-3, -3, -3],
        ],
        "res": 3
    }
]


for example in examples:
    print calculate_minimum_hp(example["dungeon"])
