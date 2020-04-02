#
"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        c = len(nums)
        nums.append(1)
        v = 1
        l, r = 0, 0
        while r < c:
            v = v * nums[r]
            r += 1
            while l < r and v >= k:
                v /= nums[l]
                l += 1
            count += r - l
        print(count)
        return count


examples = [
    {
        "input": {
            "nums": [10, 5, 2, 6],
            "k": 100
        },
        "output": 8
    }, {
        "input": {
            "nums": [1, 2, 3],
            "k": 0
        },
        "output": 0
    }, {
        "input": {
            "nums": [1, 1, 1, 1, 1, 1, 1],
            "k": 5
        },
        "output": 28
    }, {
        "input": {
            "nums": [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3],
            "k": 19
        },
        "output": 18
    }, {
        "input": {
            "nums": [1, 100],
            "k": 19
        },
        "output": 1
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']