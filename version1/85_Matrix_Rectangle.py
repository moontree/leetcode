"""
Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""


def maximal_rectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    area = 0
    if len(matrix) == 0:
        return 0
    n = len(matrix[0])
    records = [[[0, 0] for _ in range(n)] for _ in range(len(matrix))]
    """
    record[i][j] = [left_1_count, up_1_count]
    """
    for i in range(0, len(matrix)):
        if matrix[i][0] == '0':
            records[i][0] = [0, 0]
        else:
            records[i][0] = [1, 1 + ((i > 0) and records[i - 1][0][1])]
            if records[i][0][1] > area:
                area = records[i][0][1]
        for j in range(1, n):
            if '1' == matrix[i][j]:
                records[i][j] = [records[i][j - 1][0] + 1, records[i - 1][j][1] + 1]
            else:
                records[i][j] = [0, 0]
    for i in range(0, len(matrix)):
        for j in range(n):
            nums = records[i][j]
            if nums[0]:
                w = nums[0]
                h = 0
                while h < nums[1]:
                    tmp_w = records[i - h][j][0]
                    if tmp_w < w:
                        w = tmp_w
                    h += 1
                    tmp_area = h * w
                    if tmp_area > area:
                        area = tmp_area
    return area


def maximal_rectangle_lrh(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    area = 0
    if len(matrix) == 0:
        return 0
    n = len(matrix[0])
    records = [[[0, n - 1, 0] for _ in range(n)] for _ in range(len(matrix))]
    """
    record[i][j] = [left_1_j, right_1_j, height]
    """
    for i in range(0, len(matrix)):
        cur_left = 0
        cur_right = n
        for j in range(0, n):
            if matrix[i][j] == '1':
                records[i][j][0] = max(records[i - 1][j][0], cur_left)
                records[i][j][2] = records[i - 1][j][2] + 1
            else:
                cur_left = j + 1
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == '1':
                records[i][j][1] = min(records[i - 1][j][1], cur_right)
                tmp_area = (records[i][j][1] - records[i][j][0] + 1) * records[i][j][2]
                if tmp_area > area:
                    area = tmp_area
            else:
                cur_right = j - 1
    for r in records:
        print r
    return area


"""
Make to 84
"""
def maximal_rectangle_according_to_height(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in xrange(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        print height
        for i in xrange(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
    return ans


examples = [
    {
        "matrix": [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        "count": 6
    }, {
        "matrix": [
            ["1", "0", "1", "0", "1"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "0"],
        ],
        "count": 8
    }, {
        "matrix": [
            ["1", "0"],
            ["1", "0"],
        ],
        "count": 2
    }
]


for example in examples:
    print maximal_rectangle(example["matrix"])
