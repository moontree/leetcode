"""
=========================
Project -> File: leetcode -> 1187_Make_Array_Strictly_Increasing.py
Author: zhangchao
=========================
Given two integer arrays arr1 and arr2,
return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation,
you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.



Example 1:

Input:
    arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output:
    1
Explanation:
    Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:

Input:
    arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output:
    2
Explanation:
    Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:

Input:
    arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output:
    -1
Explanation:
    You can't make arr1 strictly increasing.


Constraints:
    1 <= arr1.length, arr2.length <= 2000
    0 <= arr1[i], arr2[i] <= 10^9
"""
import bisect


class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # dp[i][j]: arr1[: j] changed i times, last value
        """
        dp[i][j] :
        a) previous changed i times: arr1[j] > dp[i][j - 1] :  cur item
        b) previous changed i - 1 times: bisect.biset_right(usable)
        """
        # usable = sorted(list(set(arr2)))
        # n1, n2 = len(arr1), len(usable)
        # dp = [[float('inf') for _ in range(n1 + 1)] for _ in range(n2 + 1)]
        # dp[0][0] = -1
        # for i in range(n2 + 1):
        #     for j in range(1, n1 + 1):
        #         idx = bisect.bisect_right(usable, dp[i - 1][j - 1])
        #         if idx < len(usable):
        #             dp[i][j] = usable[idx]
        #         if arr1[j - 1] > dp[i][j - 1]:
        #             dp[i][j] = min(dp[i][j], arr1[j - 1])
        #         if dp[i][j] != float('inf') and j == n1:
        #             continue
        #             # return i
        #     print i, dp[i]
        # return -1
        #

        usable = sorted(list(set(arr2)))
        n1, n2 = len(arr1), len(usable)
        prev = [float('inf') for _ in range(n1 + 1)]
        for i in range(n2 + 1):
            cur = [float('inf') for _ in range(n1 + 1)]
            if i == 0:
                cur[0] = -1
            for j in range(1, n1 + 1):
                idx = bisect.bisect_right(usable, prev[j - 1])
                if idx < len(usable):
                    cur[j] = usable[idx]
                if arr1[j - 1] > cur[j - 1]:
                    cur[j] = min(cur[j], arr1[j - 1])
                if cur[j] != float('inf') and j == n1:
                    return i

            prev = cur
        return -1


examples = [
    {
        "input": {
            "arr1": [1, 5, 3, 6, 7],
            "arr2": [1, 3, 2, 4]
        },
        "output": 1
    }, {
        "input": {
            "arr1": [1, 5, 3, 6, 7],
            "arr2": [4, 3, 1]
        },
        "output": 2
    }, {
        "input": {
            "arr1": [1, 5, 3, 6, 7],
            "arr2": [1, 6, 3, 3]
        },
        "output": -1
    }, {
        "input": {
            "arr1": [19, 18, 7, 4, 11, 8, 3, 10, 5, 8, 13],
            "arr2": [13, 16, 9, 14, 3, 12, 15, 4, 21, 18, 1, 8, 17, 0, 3, 18]
        },
        "output": 9
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
