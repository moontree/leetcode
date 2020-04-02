"""
Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


def find_disappeared_numbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    n = len(nums)
    for v in nums:
        nums[(v - 1) % n] += n
    for i in xrange(len(nums)):
        if nums[i] <= n:
            res.append(i + 1)
    return res


print find_disappeared_numbers([4,3,2,7,8,2,3,1])