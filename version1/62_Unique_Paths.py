"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


def unique(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    nums = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            nums[j] += nums[j - 1]
    return nums[-1]


print unique(5, 5)
