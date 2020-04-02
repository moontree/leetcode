"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


def find_min(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    beg = 0
    end = len(nums) - 1
    while beg <= end:
        while beg < end and nums[beg] == nums[beg + 1]:
            beg += 1
        while end > beg and nums[end] == nums[end - 1]:
            end -= 1
        if beg == end:
            return nums[beg]

        mid = (beg + end) / 2
        if nums[mid] > nums[end]:
            beg = mid + 1
        else:
            end = mid
    return nums[beg]


examples = [
    {
        "nums": [1, 1, 1, 1, 2],
        "res": 1
    }, {
        "nums": [2, 2, 2, 1, 1, 1],
        "res": 1
    }, {
        "nums": [3, 3, 3, 3, 1],
        "res": 1
    }, {
        "nums": [6, 7, 5],
        "res": 1
    }, {
        "nums": [1],
        "res": 1
    }
]


for example in examples:
    print find_min(example["nums"])
