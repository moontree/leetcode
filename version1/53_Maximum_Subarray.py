"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

examples = [
    {
        "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "output": 6
    }, {
        "nums": [-1],
        "output": -1
    }, {
        "nums": [-1, 1, -2, 3],
        "output": 3
    }, {
        "nums": [1, 2],
        "output": 3
    }
]


def max_sub_array(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    i = 1
    left_sum = nums[0]
    while i < len(nums):
        if left_sum < 0:
            left_sum = nums[i]
            i += 1
        else:
            left_sum += nums[i]
            i += 1
        if left_sum > res:
            res = left_sum
    return res


for example in examples:
    print max_sub_array(example["nums"])
