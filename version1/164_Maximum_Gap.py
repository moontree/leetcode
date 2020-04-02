# -*- coding: utf-8 -*-
"""
Given an unsorted array,
find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers
 and fit in the 32-bit signed integer range.

max(nums[i + 1] - nums[i]) in nums.sort()
"""


def maximum_gap(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 2:
        return 0
    max_val, min_val = nums[0], nums[0]
    for p in nums:
        if max_val < p:
            max_val = p
        if min_val > p:
            min_val = p
    # n buckets
    avg_gap = (max_val - min_val) / (n - 1) + 1
    buckets = {}
    for p in nums:
        index = (p - min_val) / avg_gap
        if buckets.get(index):
            vmin, vmax = buckets.get(index)
            if vmin > p:
                buckets[index][0] = p
            if vmax < p:
                buckets[index][1] = p
        else:
            buckets[index] = [p, p]
    array_format = []
    res = 0
    for key in buckets:
        array_format.append(buckets[key])
    n2 = len(buckets)
    for i in range(n2):
        bucket_diff = array_format[i][1] - array_format[i][0]
        out_bucket_diff = 0
        if i < n2 - 1:
            out_bucket_diff = array_format[i + 1][0] - array_format[i][1]
        res = max(res, bucket_diff, out_bucket_diff)
    return res


examples = [
    {
        "nums": [3, 1, 2],
        "res": 1
    }, {
        "nums": [3, 5, 9],
        "res": 4
    }, {
        "nums": [7, 1, 10],
        "res": 6
    }, {
        "nums": [1, 1, 1, 1, 1, 5, 5, 5, 5, 5],
        "res": 4
    }
]


for example in examples:
    print maximum_gap(example["nums"])
