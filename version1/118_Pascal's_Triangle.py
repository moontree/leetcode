"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    res = [[1], [1, 1]]
    for i in range(2, numRows):
        previous = res[-1]
        cur = [1]
        for j in range(len(previous) - 1):
            cur.append(previous[j] + previous[j + 1])
        cur.append(1)
        res.append(cur[:])
    return res


print generate(5)
