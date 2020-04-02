"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
 Could you implement it using only constant extra space complexity?
"""


def missing_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_val = len(nums)
    missing = max_val * (max_val + 1) / 2 - sum(nums)
    return missing


examples = [
    {
        "nums": [3, 0, 1],
        "res": 2
    }, {
        "nums": [9, 6, 4, 2, 3, 5, 7, 0, 1],
        "res": 8
    }, {
        "nums": [0],
        "res": 1
    }
]


for example in examples:
    print missing_number(example["nums"])
