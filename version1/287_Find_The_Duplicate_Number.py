"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
 prove that at least one duplicate number must exist.
  Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


def find_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow = finder = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while True:
        slow = nums[slow]
        finder = nums[finder]
        if slow == finder:
            return slow


examples = [
    {
        "nums": [1, 1, 3, 1],
        "res": 1
    }
]


for example in examples:
    print find_duplicate(example["nums"])
