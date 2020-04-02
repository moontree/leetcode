"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return reduce(lambda x, y: x ^ y, nums)


examples = [
    {
        "nums": [5, 6, 7, 6, 5]
    }
]


for example in examples:
    print single_number(example["nums"])
