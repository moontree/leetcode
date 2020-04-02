"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
(Recall that a node is a leaf if and only if it has 0 children.)

The value of each non-leaf node is equal to
the product of the largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered,
return the smallest possible sum of the values of each non-leaf node.
It is guaranteed this sum fits into a 32-bit integer.


Example 1:

Input:
    arr = [6,2,4]
Output:
    32
Explanation:
    There are two possible trees.
    The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4


Constraints:

    2 <= arr.length <= 40
    1 <= arr[i] <= 15
    It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
"""


class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # n = len(arr)
        # max_vals = [arr[:] for _ in range(n)]
        # for i in range(n):
        #     v = arr[i]
        #     for j in range(i + 1, n):
        #         v = max(v, arr[j])
        #         max_vals[i][j] = v
        # for row in max_vals:
        #     print row
        #
        # dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = 0
        # for num in range(1, n + 1):
        #     for l in range(0, n - num + 1):
        #         r = l + num - 1
        #         for m in range(l, r):
        #             dp[l][r] = min(dp[l][r], dp[l][m] + dp[m + 1][r] + max_vals[l][m] * max_vals[m + 1][r])
        # return dp[0][-1]
        q = []
        res = 0
        for v in arr:
            while len(q) > 1 and q[-2] <= v:
                res += q.pop() * q[-1]
            while q and q[-1] <= v:
                res += q.pop() * v
            q.append(v)
        while len(q) > 1:
            res += q.pop() * q[-1]
        return res


examples = [
    {
        "input": {
            "arr": [6, 2, 4],
        },
        "output": 32
    }, {
        "input": {
            "arr": [1, 2, 3, 4],
        },
        "output": 20
    }, {
        "input": {
            "arr": [15, 13, 5, 3, 15]
        },
        "output": 500
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
