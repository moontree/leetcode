"""
=========================
Project -> File: leetcode -> 1340_Jump_Game_V.py
Author: zhangchao
=========================
Given an array of integers arr and an integer d.
In one step you can jump from index i to index:
    i + x where: i + x < arr.length and 0 < x <= d.
    i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j
if arr[i] > arr[j] and arr[i] > arr[k]
for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping.
Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

Example 1:

Input:
    arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output:
    4
Explanation:
    You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
    Note that if you start at index 6 you can only jump to index 7.
    You cannot jump to index 5 because 13 > 9.
    You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
    Similarly You cannot jump from index 3 to index 2 or index 1.

Example 2:

Input:
    arr = [3,3,3,3,3], d = 3
Output:
    1
Explanation:
    You can start at any index. You always cannot jump to any index.

Example 3:

Input:
    arr = [7,6,5,4,3,2,1], d = 1
Output:
    7
Explanation:
    Start at index 0. You can visit all the indicies.

Example 4:

Input:
    arr = [7,1,7,1,7,1], d = 2
Output:
    2

Example 5:

Input:
    arr = [66], d = 1
Output:
    1


Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 10^5
    1 <= d <= arr.length
"""


class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        dp = [0 for _ in range(len(arr))]
        self.res = 0

        def hepler(i):
            if dp[i]:
                return dp[i]
            for k in range(1, d + 1):
                if i - k < 0 or arr[i - k] >= arr[i]:
                    break
                dp[i] = max(dp[i], hepler(i - k) + 1)
            for k in range(1, d + 1):
                if i + k >= len(arr) or arr[i + k] >= arr[i]:
                    break
                dp[i] = max(dp[i], hepler(i + k) + 1)
            dp[i] = max(dp[i], 1)
            self.res = max(self.res, dp[i])
            return dp[i]

        for i in range(len(arr)):
            hepler(i)

        return self.res

        # n, res = len(arr), 1
        # pairs = [[v, i] for i, v in enumerate(arr)]
        # pairs.sort()
        # dp = [1 for _ in range(n)]
        # for v, i in pairs:
        #     for k in range(1, d + 1):
        #         if i - k < 0 or arr[i - k] >= v:
        #             break
        #         dp[i] = max(dp[i], dp[i - k] + 1)
        #     for k in range(1, d + 1):
        #         if i + k >= n or arr[i + k] >= v:
        #             break
        #         dp[i] = max(dp[i], dp[i + k] + 1)
        #     res = max(res, dp[i])
        # return res


examples = [
    {
        "input": {
            "arr": [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12],
            "d": 2
        },
        "output": 4
    }, {
        "input": {
            "arr": [3, 3, 3, 3, 3],
            "d": 3
        },
        "output": 1
    }, {
        "input": {
            "arr": [7, 6, 5, 4, 3, 2, 1],
            "d": 1
        },
        "output": 7
    }, {
        "input": {
            "arr": [7, 1, 7, 1, 7, 1],
            "d": 2
        },
        "output": 2
    }, {
        "input": {
            "arr": [66],
            "d": 1
        },
        "output": 1
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
