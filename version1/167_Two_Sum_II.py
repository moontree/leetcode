"""
Given an array of integers that is already sorted in ascending order,
 find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
 Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution
and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(numbers) - 1
    while l < r:
        res = numbers[l] + numbers[r]
        if res == target:
            return [l + 1, r + 1]
        if res < target:
            l += 1
        else:
            r -= 1
    return [0, 0]


examples = [
    {
        "numbers": [2, 7, 11, 15],
        "target": 9,
        "res": [1, 2]
    }
]


for example in examples:
    print two_sum(example["numbers"], example["target"])
