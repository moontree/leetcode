"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column,
and toggling each value in that row or column:
changing all 0s to 1s, and all 1s to 0s.

After making any number of moves,
every row of this matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score.



Example 1:

Input:
    [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output:
    39
Explanation:
    Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Note:

    1 <= A.length <= 20
    1 <= A[0].length <= 20
    A[i][j] is 0 or 1.

"""


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        r, c = len(A), len(A[0])
        for row in A:
            if row[0] == 0:
                for i in range(c):
                    row[i] = 1 - row[i]

        for j in range(1, c):
            n0, n1 = 0, 0
            for i in range(r):
                if A[i][j] == 0:
                    n0 += 1
                else:
                    n1 += 1
            if n0 > n1:
                for i in range(r):
                    A[i][j] = 1 - A[i][j]

        res = 0
        for row in A:
            tmp = 0
            for col in row:
                tmp = tmp * 2 + col
            res += tmp
        return res


examples = [
    {
        "input": {
            "A":  [
                [0, 0, 1, 1],
                [1, 0, 1, 0],
                [1, 1, 0, 0]]
        },
        "output": 39
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']