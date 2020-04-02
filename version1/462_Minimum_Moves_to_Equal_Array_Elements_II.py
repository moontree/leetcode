"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal,
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""
import math


def min_moves2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    mid = nums[len(nums) / 2]
    return sum(map(lambda x: abs(x - mid), nums))


print min_moves2([1, 2, 2, 10])