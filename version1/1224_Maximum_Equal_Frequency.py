"""
Given an array nums of positive integers,
return the longest possible length of an array prefix of nums,
such that it is possible to remove exactly one element from this prefix
so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements,
it's still considered that every appeared number has the same number of ocurrences (0).



Example 1:

Input:
    nums = [2,2,1,1,5,3,3,5]
Output:
    7
Explanation:
    For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5,
    we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

Example 2:

Input:
    nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output:
    13

Example 3:

Input:
    nums = [1,1,1,2,2,2]
Output:
    5

Example 4:

Input:
    nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output:
    8

Constraints:

    2 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
"""


class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        freqs = {}
        for v in nums:
            cache[v] = cache.get(v, 0) + 1
        if len(cache) >= len(nums) - 1 or len(cache) == 1:
            return len(nums)
        for v in cache.values():
            freqs[v] = freqs.get(v, 0) + 1
        res = len(nums)
        for v in nums[::-1]:
            if len(freqs) == 2:
                freq = min(freqs.keys())
                if freqs.get(freq + 1, 0) == 1 or freqs.get(1, 0) == 1:
                    return res
            old_freq = cache[v]
            cache[v] -= 1
            freqs[old_freq] -= 1
            if freqs[old_freq] == 0:
                del freqs[old_freq]
            if cache[v]:
                freqs[cache[v]] = freqs.get(cache[v], 0) + 1
            res -= 1
        return 0


examples = [
    {
        "input": {
            "nums": [2, 2, 1, 1, 5, 3, 3, 5],
        },
        "output": 7
    }, {
        "input": {
            "nums": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5],
        },
        "output": 13
    }, {
        "input": {
            "nums": [1, 1, 1, 2, 2, 2],
        },
        "output": 5
    }, {
        "input": {
            "nums": [10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6],
        },
        "output": 8
    }, {
        "input": {
            "nums": [1, 2, 3, 4, 5, 6, 7, 7],
        },
        "output": 8
    }, {
        "input": {
            "nums": [1, 1, 1, 1],
        },
        "output": 4
    }, {
        "input": {
            "nums": [1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 1, 2, 3, 5, 6],
        },
        "output": 13
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
