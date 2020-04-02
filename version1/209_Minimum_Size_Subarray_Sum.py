"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum >= s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
"""


def min_sub_array_len(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    start = 0
    res = n + 1
    sum = 0
    for i in range(n):
        sum += nums[i]
        while sum >= s:
            res = min(res, i - start + 1)
            sum -= nums[start]
            start += 1
    if res == n + 1:
        return 0
    else:
        return res


examples = [
    {
        "s": 117,
        "nums": [2, 3, 1, 2, 4, 3],
        "res": 2
    }, {
        "s": 15,
        "nums": [1, 2, 3, 4, 5],
        "res": 5
    }, {
        "s": 4,
        "nums": [1, 4, 4],
        "res": 1
    }
]


for example in examples:
    print min_sub_array_len(example["s"], example["nums"])
