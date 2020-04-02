"""
Given an integer array,
you need to find one continuous subarray that if you only sort this subarray in ascending order,
 then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end = -1, -2
    c = len(nums)
    min_val = nums[-1]
    max_val = nums[0]
    for i in range(1, c):
        max_val = max(max_val, nums[i])
        min_val = min(nums[c - i - 1], min_val)
        if nums[i] < max_val:
            end = i
        if nums[c - i - 1] > min_val:
            start = c - i - 1
    print(start, end)
    return end - start + 1


examples = [
    {
        "nums": [2, 6, 4, 8, 10, 9, 15],
        "res": 5
    }, {
        "nums": [2, 6, 4, 8, 10],
        "res": 2
    }, {
        "nums": [2, 4, 8, 10],
        "res": 0
    }, {
        "nums": [1, 3, 2, 2, 2],
        "res": 4
    }
]


if __name__ == "__main__":
    for example in examples:
        print(findUnsortedSubarray(example["nums"]))