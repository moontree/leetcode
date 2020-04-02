"""
After robbing those houses on that street,
 the thief has found himself a new place for his thievery
  so that he will not get too much attention.
   This time, all houses at this place are arranged in a circle.
   That means the first house is the neighbor of the last one.
    Meanwhile, the security system for these houses
    remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    pre_max = nums[:]
    pre_max[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        pre_max[i] = max(pre_max[i - 2] + nums[i], pre_max[i - 1])
    return pre_max[-1]


def rob_2(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(rob(nums[1:]), rob(nums[:-1]))


examples = [
    {
        "nums": [1, 2, 3, 4, 5],
        "res": 8,
    }, {
        "nums": [9, 1, 5, 1, 10],
        "res": 15,
    }, {
        "nums": [9, 1, 1, 10, 1],
        "res": 19,
    }, {
        "nums": [1],
        "res": 1,
    }
]


for example in examples:
    print rob_2(example["nums"])
