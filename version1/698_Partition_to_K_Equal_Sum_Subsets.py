"""
=========================
Project -> File: leetcode -> 698_Partition_to_K_Equal_Sum_Subsets.py
Author: zhangchao
=========================
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input:
    nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output:
    True
Explanation:
    It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:
    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.
"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)


examples = [
    {
        "input": {
            "nums": [4, 3, 2, 3, 5, 2, 1],
            "k": 4
        },
        "output": True
    }, {
        "input": {
            "nums": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "k": 5
        },
        "output": True
    }, {
        "input": {
            "nums": [3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269],
            "k": 5
        },
        "output": True
    }, {
        "input": {
            "nums": [2, 2, 2, 2, 3, 4, 5],
            "k": 4
        },
        "output": False
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
