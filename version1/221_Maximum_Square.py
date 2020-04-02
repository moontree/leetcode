"""
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""


def maximal_square(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
        return 0
    m, n = len(matrix), len(matrix[0])
    nums = [1 if p == "1" else 0 for p in matrix[0]]
    nums.append(0)
    res = cal_area(nums, n)
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == "1":
                nums[j] += 1
            else:
                nums[j] = 0
        res = max(res, cal_area(nums, n))
    return res


def cal_area(nums, n):
    stack = [-1]
    res = 0
    for j in range(n + 1):
        while nums[j] < nums[stack[-1]]:
            h = nums[stack.pop()]
            w = j - stack[-1] - 1
            s = min(w, h)
            before_area = s * s
            res = max(res, before_area)
        stack.append(j)
    return res


examples = [
    {
        "matrix": [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ],
        "res": 4
    }
]


for example in examples:
    print maximal_square(example["matrix"])
