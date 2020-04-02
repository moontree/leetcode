"""
Given an array nums,
 write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""


def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = 0
    left = 0
    for p in nums:
        if p == 0:
            count += 1
        else:
            nums[left] = p
            left += 1
    n = len(nums) - 1
    for i in range(count):
        nums[n - i] = 0


examples = [
    {
        "nums": [0, 1, 0, 3, 12],
    }
]


for example in examples:
    move_zeroes(example["nums"])
