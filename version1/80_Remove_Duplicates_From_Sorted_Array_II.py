"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""


def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = -1
    r = 0
    while r < len(nums):
        count = 0
        val = nums[r]
        while r < len(nums) and nums[r] == val:
            r += 1
            count += 1
        if count == 1:
            l += 1
            nums[l] = val
        else:
            nums[l + 1] = val
            nums[l + 2] = val
            l += 2
    return l + 1


examples = [
    {
        "nums": [1, 1, 1, 2, 2, 2, 3],
        "length": 5
    }, {
        "nums": [1, 2, 2, 2, 3],
        "length": 4
    }, {
        "nums": [1, 1, 1, 1, 1, 1],
        "length": 2
    }, {
        "nums": [1, 2, 2, 2, 2, 3, 3, 3, 3],
        "length": 5
    }, {
        "nums": [1, 1, 1, 2, 3],
        "length": 4
    }, {
        "nums": [],
        "length": 0
    }
]


for example in examples:
    print remove_duplicates(example["nums"])