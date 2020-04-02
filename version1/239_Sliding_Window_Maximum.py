"""
Given an array nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
 You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
"""


def max_sliding_window(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = []
    indexes = []
    for i, v in enumerate(nums):
        while indexes and nums[indexes[-1]] < v:
            indexes.pop()
        indexes.append(i)
        if indexes[0] == i - k:
            indexes.pop(0)
        if i > k - 2:
            res.append(nums[indexes[0]])
    return res


examples = [
    {
        "nums": [1, 3, -1, -3, 5, 3, 6, 7],
        "k": 3,
        "res": [3, 3, 5, 5, 6, 7]
    }
]


for example in examples:
    print max_sliding_window(example["nums"], example["k"])
