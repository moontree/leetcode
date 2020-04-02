"""
Find the contiguous subarray within an array
 (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos = nums[:]
    neg = nums[:]
    for i in range(1, len(nums)):
        a, b, c = pos[i - 1] * nums[i], neg[i - 1] * nums[i], nums[i]
        pos[i] = max(a, b, c)
        neg[i] = min(a, b, c)
    return max(pos)


examples = [
    {
        "nums": [2, 3, -2, 4],
        "res": 6
    }, {
        "nums": [2, 3, -2, 4, -1],
        "res": 48
    }, {
        "nums": [2, -1, 1, 4, -1],
        "res": 8
    }, {
        "nums": [-2, 1, 1, 4, 1],
        "res": 8
    }, {
        "nums": [2, -5, -2, -4, 3],
        "res": 24
    }, {
        "nums": [-4, -3, -2],
        "res": 12
    }
]


for example in examples:
    print max_product(example["nums"])
