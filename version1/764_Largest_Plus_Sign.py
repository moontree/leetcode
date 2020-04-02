"""
In a 2D grid from (0, 0) to (N-1, N-1),
every cell contains a 1,
except those cells in the given list mines which are 0.
What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign.
If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center
grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s.
This is demonstrated in the diagrams below.
Note that there could be 0s or 1s beyond the arms of the plus sign,
only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

Example 1:

Input:
    N = 5, mines = [[4, 2]]
Output:
    2
Explanation:
    11111
    11111
    11111
    11111
    11011
In the above grid, the largest plus sign can only be order 2.

Example 2:

Input:
    N = 2, mines = []
Output:
    1
Explanation:
    There is no plus sign of order 2, but there is of order 1.


Example 3:
Input:
    N = 1, mines = [[0, 0]]
Output:
    0
Explanation:
    There is no plus sign, so return 0.
Note:

    N will be an integer in the range [1, 500].
    mines will have length at most 5000.
    mines[i] will be length 2 and consist of integers in the range [0, N-1].
    (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
"""
import bisect


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        row_breaks = {i: [-1, N] for i in range(N)}
        col_breaks = {i: [-1, N] for i in range(N)}
        grids = [[1 for _ in range(N)] for _ in range(N)]

        for r, c in mines:
            bisect.insort_left(row_breaks[r], c)
            bisect.insort_left(col_breaks[c], r)
            grids[r][c] = 0
        # for r in grids:
        #     print r
        # print row_breaks
        # print col_breaks

        res = 0
        for i in range(N):
            row = row_breaks[i]
            for k in range(len(row) - 1):
                for j in range(row[k] + res + 1, row[k + 1] - res):
                    if grids[i][j]:
                        l = j - row[k]
                        r = row[k + 1] - j
                        v = bisect.bisect_left(col_breaks[j], i)
                        u = i - col_breaks[j][v - 1]
                        d = col_breaks[j][v] - i
                        res = max(res, min(l, r, u, d))

        print res
        return res


examples = [
    {
        "input": {
            "N": 5,
            "mines": [[4, 2]]
        },
        "output": 2
    }, {
        "input": {
            "N": 2,
            "mines": []
        },
        "output": 1
    }, {
        "input": {
            "N": 1,
            "mines": [[0, 0]]
        },
        "output": 0
    }, {
        "input": {
            "N": 2,
            "mines": [[0, 0], [0, 1], [1, 0]]
        },
        "output": 1
    }, {
        "input": {
            "N": 10,
            "mines":[
                [0, 0], [0, 1], [0, 2], [0, 7],
                [1,2],[1,3],[1,9],
                [2,3],[2,5],[2,7],[2,8],
                [3,2],[3,5],[3,7],
                [4,2],[4,3],[4,5],[4,7],
                [5,1],[5,4],[5,8],[5,9],
                [7,2],[7,5],[7,7],[7,8],
                [8,5],[8,8],[9,0],
                [9,1],[9,2],[9,8]
            ]
        },
        "output": 4
    },
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']