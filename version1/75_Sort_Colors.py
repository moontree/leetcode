"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
 with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to
represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""


def sort_colors(nums):
    l = 0
    i = 0
    r = len(nums) - 1
    while i <= r:
        if nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
        elif nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        else:
            i += 1
    print nums


examples = [
    {
        "nums": [1, 1, 0, 0, 2, 1, 2]
    }, {
        "nums": [0, 2, 2, 1, 1, 1, 0]
    }, {
        "nums": [0, 0, 0, 0, 2, 1, 2]
    }, {
        "nums": [2, 1, 0, 0, 2, 1, 2]
    }, {
        "nums": [0, 0, 0]
    }, {
        "nums": [1, 1, 0]
    }
]


for example in examples:
    sort_colors(example["nums"])
