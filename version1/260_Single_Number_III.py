"""
Given an array of numbers nums,
in which exactly two elements appear only once and all the other elements appear exactly twice.
 Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    total = 0
    for n in nums:
        total = total ^ n
    digit = total & -total
    a, b = 0, 0
    for n in nums:
        if n & digit:
            a = a ^ n
        else:
            b = b ^ n
    return [a, b]


examples = [
    {
        "nums": [1, 2, 1, 3, 2, 5],
        "res": [3, 5],
    }
]


for example in examples:
    print single_number(example["nums"])
