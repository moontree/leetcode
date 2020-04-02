"""
=========================
Project -> File: leetcode -> 689_Maximum_Sum_of_3_Non_Overlapping_Subarrays.py
Author: zhangchao
=========================
In a given array nums of positive integers,
find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k,
and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example:

Input:
    [1,2,1,2,6,7,5,1], 2
Output:
    [0, 3, 5]
Explanation:
    Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
    We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
    nums.length will be between 1 and 20000.
    nums[i] will be between 1 and 65535.
    k will be between 1 and floor(nums.length / 3).
"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s, v, n = [], 0, len(nums)
        for c in nums:
            v += c
            s.append(v)
        s.append(0)

        r = [[0, 0] for _ in range(n)]
        v, idx = 0, -1
        for i in range(n - k + 1)[::-1]:
            ts = s[i + k - 1] - s[i - 1]
            if ts >= v:
                v, idx = ts, i
            r[i] = [v, idx]

        lv, li = s[k - 1], 0
        res, v = 0, 0
        for i in range(k, n - k):
            tmp_lv = s[i - 1] - s[i - k - 1]
            if tmp_lv > lv:
                lv, li = tmp_lv, i - k

            tmp = lv + s[i + k - 1] - s[i - 1] + r[i + k][0]
            if tmp > v:
                res, v = [li, i, r[i + k][1]], tmp
        return res


examples = [
    {
        "input": {
            "nums": [1, 2, 1, 2, 6, 7, 5, 1],
            "k": 2
        },
        "output": [0, 3, 5]
    }, {
        "input": {
            "nums": [7, 13, 20, 19, 19, 2, 10, 1, 1, 19],
            "k": 3
        },
        "output": [1, 4, 7]
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
