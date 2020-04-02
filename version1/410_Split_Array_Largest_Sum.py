# --*-- encoding: utf-8 --*--
"""
Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:
    1 ≤ n ≤ 1000
    1 ≤ m ≤ min(50, n)

Examples:

Input:
    nums = [7,2,5,10,8]
    m = 2
Output:
    18

Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8],
    where the largest sum among the two subarrays is only 18.
"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def split(target):
            v = 0
            c = 1
            for n in nums:
                if v + n > target:
                    v = n
                    c += 1
                else:
                    v += n
            return c

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) / 2
            v = split(mid)
            if v > m:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res


examples = [
    {
        "input": {
            "nums": [7, 2, 5, 10, 8],
            "m": 2,
        },
        "output": 18
    }, {
        "input": {
            "nums": [7, 2, 5, 10, 8],
            "m": 3,
        },
        "output": 14
    }, {
        "input": {
            "nums": [2, 3, 1, 2, 4, 3],
            "m": 5,
        },
        "output": 4
    }, {
        "input": {
            "nums": [1, 2147483646],
            "m": 1,
        },
        "output": 2147483647
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
