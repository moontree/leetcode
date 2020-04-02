"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
the relation between mid, left, and right


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""


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
        if nums[mid] == target:
            return True
        while nums[left] == nums[mid]:
            left += 1
        if nums[mid] > nums[right]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            right -= 1
    return False


examples = [
    {
        "input": {
            "nums": [4, 4, 4, 6, 7, 4, 4, 4],
            "target": 6
        },
        "output": True
    }, {
        "input": {
            "nums": [4, 4, 4, 4, 7, 0, 4, 4],
            "target": 1
        },
        "output": False
    }, {
        "input": {
            "nums": [1, 1, 3, 1],
            "target": 3
        },
        "output": True
    }, {
        "input": {
            "nums": [1, 3, 1, 1, 1],
            "target": 3
        },
        "output": True
    }, {
        "input": {
            "nums": [3, 1, 2, 2, 2],
            "target": 1
        },
        "output": True
    }, {
        "input": {
            "nums": [3, 5, 1],
            "target": 3
        },
        "output": True
    },
]


for example in examples:
    print "----- testing -----"
    print example
    res = search(example["input"]["nums"], example["input"]["target"])
    print res == example["output"], "res = ", res, "expected = ", example["output"]
