"""
Given an integer array with all positive numbers and no duplicates,
 find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""


def combination_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums, combs = sorted(nums), [1] + [0] * (target)
    for i in range(target + 1):
        for num in nums:
            if num > i: break
            combs[i] += combs[i - num]
    return combs[target]


examples = [
    {
        "input": {
            "nums": [1, 2, 3],
            "target": 4
        },
        "output": 7
    }
]


for example in examples:
    print combination_sum(**example["input"])
