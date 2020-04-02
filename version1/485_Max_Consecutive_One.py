"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

"""


def find_max_consecutive_ones(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res, cur = 0, 0
    for n in nums:
        if n == 1:
            cur += 1
        else:
            res = max(res, cur)
            cur = 0
    return max(res, cur)


print find_max_consecutive_ones([1, 1, 0, 1, 1, 1])