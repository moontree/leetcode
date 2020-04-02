"""
There is a brick wall in front of you.
 The wall is rectangular and has several rows of bricks.
 The bricks have the same height but different width.
  You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows.
Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick,
then the brick is not considered as crossed.
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall
, in which case the line will obviously cross no bricks.



Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
"""


def least_bricks(wall):
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    if len(wall) == 0:
        return 0
    n = sum(wall[0])
    counts = {}
    for row in wall:
        cur = 0
        for w in row[:-1]:
            cur += w
            counts[cur] = counts.get(cur, 0) + 1
    c = 0
    for k in counts:
        if c < counts[k]:
            c = counts[k]

    return len(wall) - c


examples = [
    {
        "wall": [
            [1, 2, 2, 1],
            [3, 1, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]
        ],
        "output": 2
    }, {
        "wall": [
            [1],
            [1],
            [1],
        ],
        "output": 3
    }
]


if __name__ == "__main__":
    for example in examples:
        print(least_bricks(example['wall']))
