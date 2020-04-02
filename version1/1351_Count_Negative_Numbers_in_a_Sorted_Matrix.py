"""
=========================
Project -> File: leetcode -> 1351_Count_Negative_Numbers_in_a_Sorted_Matrix.py
Author: zhangchao
=========================
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.



Example 1:

Input:
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output:
    8
Explanation:
    There are 8 negatives number in the matrix.

Example 2:

Input:
    grid = [[3,2],[1,0]]
Output:
    0

Example 3:

Input:
    grid = [[1,-1],[-1,-1]]
Output:
    3

Example 4:

Input:
    grid = [[-1]]
Output:
    1


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""
import bisect


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        r, c = len(grid), len(grid[0])
        j = 0
        for i in range(r)[::-1]:
            while j < c and grid[i][j] >= 0:
                j += 1
            res += c - j
            continue
        return res


examples = [
    {
        "input": {
            "grid": [
                [4, 3, 2, -1],
                [3, 2, 1, -1],
                [1, 1, -1, -2],
                [-1, -1, -2, -3]
            ],
        },
        "output": 8
    }, {
        "input": {
            "grid": [
                [3, 2],
                [1, 0]
            ],
        },
        "output": 0
    }, {
        "input": {
            "grid": [
                [1, -1],
                [-1, -1]
            ],
        },
        "output": 3
    }, {
        "input": {
            "grid": [[-1]],
        },
        "output": 1
    }
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
