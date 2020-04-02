"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines:
a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];

The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints:
each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.



Example 1:


Input:
    A = [1,4,2], B = [1,2,4]
Output:
    2
Explanation:
    We can draw 2 uncrossed lines as in the diagram.
    We cannot draw 3 uncrossed lines,
    because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:

Input:
    A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output:
    3

Example 3:

Input:
    A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output:
    2

Note:
    1 <= A.length <= 500
    1 <= B.length <= 500
    1 <= A[i], B[i] <= 2000
"""


class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        na, nb = len(A), len(B)
        dp = [[0 for _ in range(nb)] for _ in range(na)]
        for j in range(nb):
            if A[0] == B[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        for i in range(na):
            if A[i] == B[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, na):
            for j in range(1, nb):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]


examples = [
    {
        "input": {
            "A": [1, 4, 2],
            "B": [1, 2, 4]
        },
        "output": 2
    }, {
        "input": {
            "A": [2, 5, 1, 2, 5],
            "B": [10, 5, 2, 1, 5, 2]
        },
        "output": 3
    }, {
        "input": {
            "A": [1, 3, 7, 1, 7, 5],
            "B": [1, 9, 2, 5, 1],
        },
        "output": 2
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
