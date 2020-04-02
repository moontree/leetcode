"""
=========================
Project -> File: leetcode -> 1343_Number_of_Sub_arrays_of_Size_K_and_Average_Greater_than_or_Equal_to_Threshold.py
Author: zhangchao
=========================
Given an array of integers arr and two integers k and threshold.

Return the number of sub-arrays of size k and average greater than or equal to threshold.


Example 1:

Input:
    arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output:
    3
Explanation:
    Sub-arrays [2,5,5],[5,5,5] and [5,5,8]
    have averages 4, 5 and 6 respectively.
    All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:

Input:
    arr = [1,1,1,1,1], k = 1, threshold = 0
Output:
    5

Example 3:

Input:
    arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output:
    6
Explanation:
    The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

Example 4:

Input:
    arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
Output:
    1

Example 5:

Input:
    arr = [4,4,4,4], k = 4, threshold = 1
Output:
    1


Constraints:

    1 <= arr.length <= 10^5
    1 <= arr[i] <= 10^4
    1 <= k <= arr.length
    0 <= threshold <= 10^4
"""


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res, b, n = 0, k * threshold, len(arr)
        s = sum(arr[:k])
        if s >= b:
            res += 1
        for r in range(k, n):
            s += arr[r] - arr[r - k]
            res += (s >= b)
        return res


examples = [
    {
        "input": {
            "arr": [2, 2, 2, 2, 5, 5, 5, 8],
            "k": 3,
            "threshold": 4
        },
        "output": 3
    }, {
        "input": {
            "arr": [1, 1, 1, 1, 1],
            "k": 1,
            "threshold": 0
        },
        "output": 5
    }, {
        "input": {
            "arr": [11, 13, 17, 23, 29, 31, 7, 5, 2, 3],
            "k": 3,
            "threshold": 5
        },
        "output": 6
    }, {
        "input": {
            "arr": [7, 7, 7, 7, 7, 7, 7],
            "k": 7,
            "threshold": 7
        },
        "output": 1
    }, {
        "input": {
            "arr": [4, 4, 4, 4],
            "k": 4,
            "threshold": 1
        },
        "output": 1
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
