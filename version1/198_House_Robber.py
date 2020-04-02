"""
You are a professional robber planning to rob houses along a street.
 Each house has a certain amount of money stashed,
  the only constraint stopping you from robbing each of them is that
   adjacent houses have security system connected and
   it will automatically contact the police
   if two adjacent houses were broken into on the same night.

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


examples = [
    {
        "nums": [1, 2, 3, 4, 5],
        "res": 9,
    }, {
        "nums": [1, 9, 5, 1, 10],
        "res": 19,
    }, {
        "nums": [9, 1, 1, 10, 1],
        "res": 19,
    }
]


for example in examples:
    print rob(example["nums"])
