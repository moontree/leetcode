"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""


examples = [
    {
        "input": {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 6
        },
        "output": 2
    }, {
        "input": {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3
        },
        "output": -1
    }, {
        "input": {
            "nums": [1, 3],
            "target": 3
        },
        "output": 1
    },
]


def binary_search(nums, target, _left, _right):
    left = _left
    right = _right
    while left <= right:
        mid = (left + right) / 2
        print "left ", left, "right ", right, "mid ", mid
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    count = len(nums)
    left = 0
    right = count - 1
    while left <= right:
        mid = (left + right) / 2
        print "left ", left, "right ", right, "mid ", mid
        if nums[mid] == target:
            return mid
        elif (target > nums[right] >= nums[mid]) or \
                (target < nums[mid] < nums[right]) or \
                (nums[left] <= target < nums[mid]):
            right = mid - 1
        else:
            left = mid + 1

    return -1


for example in examples:
    print "----- testing -----"
    print example
    res = search(example["input"]["nums"], example["input"]["target"])
    print res == example["output"], "res = ", res, "expected = ", example["output"]
