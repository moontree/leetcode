"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


examples = [
    {
        "nums": [2, 3, 1, 1, 4],
        "res": True
    },{
        "nums": [0],
        "res": True
    }, {
        "nums": [3, 2, 1, 0, 4],
        "res": False
    },
]


def can_jump(nums):
    """
    :type nums: List[int]
    :rtype: 
    """
    count = len(nums)
    ranges = [i + nums[i] for i in range(count)]
    reached = 0
    for i in range(count):
        if reached < i:
            return False
        if reached < ranges[i]:
            reached = ranges[i]
    return True


for example in examples:
    print can_jump(example["nums"])
