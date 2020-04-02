"""
Given an integer array arr and an integer difference,
return the length of the longest subsequence in arr
which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.



Example 1:

Input:
    arr = [1,2,3,4], difference = 1
Output:
    4
Explanation:
    The longest arithmetic subsequence is [1,2,3,4].

Example 2:

Input:
    arr = [1,3,5,7], difference = 1
Output:
    1
Explanation:
    The longest arithmetic subsequence is any single element.

Example 3:

Input:
    arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output:
    4
Explanation:
    The longest arithmetic subsequence is [7,5,3,1].


Constraints:

    1 <= arr.length <= 10^5
    -10^4 <= arr[i], difference <= 10^4
"""


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = [0 for _ in range(20001)]
        res = 0
        for i, v in enumerate(arr):
            v += 10000
            dp[v] = dp[v - difference] + 1 if 0 <= v - difference <= 20000 else 1
            res = max(res, dp[v])
        return res


examples = [
    {
        "input": {
            "arr": [1, 2, 3, 4],
            "difference": 1
        },
        "output": 4
    }, {
        "input": {
            "arr": [1, 3, 5, 7],
            "difference": 1
        },
        "output": 1
    }, {
        "input": {
            "arr": [1, 5, 7, 8, 5, 3, 4, 2, 1],
            "difference": -2
        },
        "output": 4
    }, {
        "input": {
            "arr": [3, 0, -3, 4, -4, 7, 6],
            "difference": 3
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
