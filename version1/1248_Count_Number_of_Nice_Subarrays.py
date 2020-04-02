"""
Given an array of integers nums and an integer k.
A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.


Example 1:

Input:
    nums = [1,1,2,1,1], k = 3
Output:
    2
Explanation:
    The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input:
    nums = [2,4,6], k = 1
Output:
    0
Explanation:
    There is no odd numbers in the array.

Example 3:

Input:
    nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output:
    16


Constraints:

    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length
"""


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        blocks = []
        prev = -1
        for i, v in enumerate(nums):
            if v % 2 == 1:
                blocks.append(i - prev)
                prev = i
        blocks.append(len(nums) - prev)
        res = 0
        for i in range(len(blocks) - k):
            res += blocks[i] * blocks[i + k]
        return res


examples = [
    {
        "input": {
            "nums": [1, 1, 2, 1, 1],
            "k": 3
        },
        "output": 2
    }, {
        "input": {
            "nums": [2, 4, 6],
            "k": 1
        },
        "output": 0
    },  {
        "input": {
            "nums": [2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            "k": 2
        },
        "output": 16
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
