"""
Given an array of integers, 1 <= a[i] <= n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[8,3,2,7,8,2,3,1]

Output:
[2,3]
"""


def find_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    res = []
    # use flag
    # for v in nums:
    #     idx = abs(v) - 1
    #     nums[idx] = -nums[idx]
    #     if nums[idx] > 0:
    #         res.append(idx + 1)
    # use mod
    for v in nums:
        nums[(v - 1) % n] += n
    for i in xrange(len(nums)):
        if (nums[i] - 1) / n >= 2:
            res.append(i + 1)
    return res


print find_duplicates([8,3,2,7,8,2,3,1])
