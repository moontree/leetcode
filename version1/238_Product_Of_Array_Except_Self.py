"""
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""


def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lt, rt, n, left, right = 1, 1, len(nums), nums[:], nums[:]
    for i in range(n):
        left[i] = lt
        lt *= nums[i]
        right[n - i - 1] = rt
        rt *= nums[n - i - 1]
    for i in range(n):
        nums[i] = left[i] * right[i]
    return nums


examples = [
    {
        "nums": [1, 2, 3, 4],
    }, {
        "nums": [1, 2],
    }, {
        "nums": [1],
    }
]


for example in examples:
    print product_except_self(example["nums"])
