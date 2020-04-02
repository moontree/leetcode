"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""


def find_min(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] < nums[1]:
            return nums[0]
        return nums[1]
    l, r = 0, len(nums) - 1
    mid = (l + r) / 2
    if nums[mid] > nums[l]:
        if nums[l] < nums[r]:
            return nums[l]
        else:
            l = mid + 1
    else:
        r = mid
    return find_min(nums[l: r + 1])


examples = [
    {
        "nums": [1, 2, 3, 4, 5, 6],
        "res": 1
    }, {
        "nums": [6, 1, 2, 3, 4, 5],
        "res": 1
    }, {
        "nums": [5, 6, 1, 2, 3, 4],
        "res": 1
    }, {
        "nums": [6, 7, 5],
        "res": 1
    }
]


for example in examples:
    print find_min(example["nums"])
