"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
 and the absolute difference between i and j is at most k.
"""


def contains_nearby_duplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    record = {}
    for i in range(len(nums)):
        if record.get(nums[i]) is not None:
            if i - record.get(nums[i]) <= k:
                return True
        record[nums[i]] = i
    return False
