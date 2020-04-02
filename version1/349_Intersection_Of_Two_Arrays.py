"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
"""


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    records1, records2 = {}, {}
    for n in nums1:
        records1[n] = 1
    for n in nums2:
        records2[n] = 1
    res = []
    for key in records1:
        if records2.get(key):
            res.append(key)
    return res