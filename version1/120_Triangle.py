"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
 where n is the total number of rows in the triangle.
"""


examples = [
    {
        "triangle": [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        "res": 11
    }
]


def minimum_total(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    h = len(triangle)
    if h == 0:
        return 0
    sums = [triangle[0][0]]
    for i in range(1, h):
        sums.append(float('inf'))
        next_sum = []
        for j in range(i + 1):
            next_sum.append(min(sums[j - 1], sums[j]) + triangle[i][j])
        sums = next_sum
    return min(sums)


for example in examples:
    print minimum_total(example["triangle"])
