"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input:
    [0,1]
Output:
    2
Explanation:
    [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input:
    [0,1,0]
Output:
    2
Explanation:
    [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note:
    The length of the given binary array will not exceed 50,000.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, diff = 0, 0
        cache = {}
        for i, v in enumerate(nums):
            diff += 1 if v == 1 else -1
            if diff == 0:
                res = max(res, i + 1)
            elif diff not in cache:
                cache[diff] = i
            else:
                res = max(res, i - cache[diff])
        return res


        # res = 0
        # for v in nums:
        #     counts[v] += 1
        #     res =
        # print(res)
        # l, r = 0, len(nums) - 1
        # while l < r and counts[0] != counts[1]:
        #     if nums[l] == nums[r]:
        #         counts[nums[l]] -= 1
        #         l += 1
        #     else:
        #         if counts[0] > counts[1]:
        #             if nums[l] == 0:
        #                 l += 1
        #             else:
        #                 r -= 1
        #             counts[0] -= 1
        #         else:
        #             if nums[l] == 0:
        #                 r -= 1
        #             else:
        #                 l += 1
        #             counts[1] -= 1
        # return max(res, 2 * min(counts))


examples = [
    {
        "input": {
            "nums": [0, 1]
        },
        "output": 2
    }, {
        "input": {
            "nums": [0, 1, 0]
        },
        "output": 2
    }, {
        "input": {
            "nums": [0, 1, 0, 0]
        },
        "output": 2
    }, {
        "input": {
            "nums": [1, 1, 0, 0, 1, 0, 1, 1]
        },
        "output": 6
    },  {
        "input": {
            "nums": [0, 1, 0, 1, 1, 1]
        },
        "output": 4
    }, {
        "input": {
            "nums": [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
        },
        "output": 68
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
