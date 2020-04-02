"""
Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1),
remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
    23
Explanation:
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
    ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
    ----> [1, 3, 3, 3, 1] (1*1=1 points)
    ----> [1, 1] (3*3=9 points)
    ----> [] (2*2=4 points)
Note:
     The number of boxes n would not exceed 100.
"""


class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def helper(l, r, k):
            if l > r:
                return 0
            if dp[l][r][k] != 0:
                return dp[l][r][k]
            while r > 1 and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            dp[l][r][k] = helper(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], helper(l, i, k + 1) + helper(i + 1, r - 1, 0))
            # print l, r, k, dp[l][r][k]
            return dp[l][r][k]

        return helper(0, n - 1, 0)


examples = [
    {
        "input": {
            "boxes": [1, 3, 2, 2, 2, 3, 4, 3, 1],
        },
        "output": 23
    }, {
        "input": {
            "boxes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        },
        "output": 10
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
