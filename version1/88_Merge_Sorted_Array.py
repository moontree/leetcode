"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
 to hold additional elements from nums2.
 The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i > -1 and j > -1:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    while j > -1:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    print nums1


examples = [
    {
        "nums1": [7, 8, 9, 10],
        "m": 4,
        "nums2": [1, 2, 3, 6],
        "n": 4
    }
]


for example in examples:
    merge(example["nums1"] + [0] * example["n"], example["m"], example["nums2"], example["n"])
