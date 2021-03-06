"""
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c),
where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix,
sorted by their distance from (r0, c0) from smallest distance to largest distance.
Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance,
|r1 - r2| + |c1 - c2|.
(You may return the answer in any order that satisfies this condition.)



Example 1:

Input:
    R = 1, C = 2, r0 = 0, c0 = 0
Output:
    [[0,0],[0,1]]
Explanation:
    The distances from (r0, c0) to other cells are: [0,1]

Example 2:

Input:
    R = 2, C = 2, r0 = 0, c0 = 1
Output:
    [[0,1],[0,0],[1,1],[1,0]]
Explanation:
    The distances from (r0, c0) to other cells are: [0,1,1,2]
    The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

Example 3:
Input:
    R = 2, C = 3, r0 = 1, c0 = 2
Output:
    [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation:
    The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
    There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].


Note:

    1 <= R <= 100
    1 <= C <= 100
    0 <= r0 < R
    0 <= c0 < C
"""


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        used = [[0 for _ in range(C)] for _ in range(R)]
        n = R * C
        i = 0
        used[r0][c0] = 1
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = [[r0, c0]]
        while len(res) < n:
            cur = res[i]
            for d in directions:
                ni, nj = cur[0] + d[0], cur[1] + d[1]
                if 0 <= ni < R and 0 <= nj < C and used[ni][nj] == 0:
                    used[ni][nj] = 1
                    res.append([ni, nj])
            i += 1
        return res


examples = [
    {
        "input": {
            "R": 1,
            "C": 2,
            "r0": 0,
            "c0": 0

        },
        "output": [[0, 0], [0, 1]]
    }, {
        "input": {
            "R": 2,
            "C": 2,
            "r0": 0,
            "c0": 1

        },
        "output": [[0, 1], [0, 0], [1, 1], [1, 0]]
    }, {
        "input": {
            "R": 2,
            "C": 3,
            "r0": 1,
            "c0": 2

        },
        "output": [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
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
