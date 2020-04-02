"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


def wiggle_sort(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    half = len(nums[::2])
    nums[0::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


examples = [
    {
        "nums": [1, 5, 1, 1, 6, 4, 1]
    }, {
        "nums": [1, 3, 2, 2, 3, 1]
    }, {
        "nums": [4, 5, 5, 6]
    }
]


def check(nums):
    valid = True
    for i in xrange(1, len(nums) - 1):
        if i % 2 == 1:
            valid = valid and nums[i - 1] < nums[i] and nums[i] > nums[i + 1]
        else:
            valid = valid and nums[i] < nums[i - 1] and nums[i] < nums[i + 1]
        if not valid:
            return False
    return True


for example in examples:
    sn = wiggle_sort(example["nums"])
    print sn, check(sn)
