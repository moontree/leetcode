"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
"""


def next_permutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 2
    while i > -1 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        nums.sort()
    else:
        new_order = nums[i:]
        new_order.sort()
        for j in range(len(new_order)):
            if new_order[j] > nums[i]:
                nums[i] = new_order[j]
                new_order.pop(j)
                break
        nums[i + 1:] = new_order
    return nums


p = [1, 1]
for k in range(3):
    p = next_permutation(p)
