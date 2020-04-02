"""
Given n and m which are the dimensions of a matrix initialized by zeros
and given an array indices where indices[i] = [ri, ci].
For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.



Example 1:


Input:
    n = 2, m = 3, indices = [[0,1],[1,1]]
Output:
    6
Explanation:
    Initial matrix = [[0,0,0],[0,0,0]].
    After applying first increment it becomes [[1,2,1],[0,1,0]].
    The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

Example 2:


Input:
    n = 2, m = 2, indices = [[1,1],[0,0]]
Output:
    0
Explanation:
    Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.

Constraints:
    1 <= n <= 50
    1 <= m <= 50
    1 <= indices.length <= 100
    0 <= indices[i][0] < n
    0 <= indices[i][1] < m
"""


class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        cx, cy = {}, {}
        for x, y in indices:
            cx[x] = cx.get(x, 0) + 1
            cy[y] = cy.get(y, 0) + 1
        res = 0
        for i in range(n):
            for j in range(m):
                if (cx.get(i, 0) + cy.get(j, 0)) % 2 == 1:
                    res += 1
        return res


examples = [
    {
        "input": {
            "n": 2,
            "m": 3,
            "indices": [[0, 1], [1, 1]]
        },
        "output": 6
    }, {
        "input": {
            "n": 2,
            "m": 2,
            "indices": [[1, 1], [0, 0]]
        },
        "output": 0
    }, {
        "input": {
            "n": 48,
            "m": 37,
            "indices": [[40, 5]]
        },
        "output": 83
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
