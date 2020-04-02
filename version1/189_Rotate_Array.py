"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    l, r = 0, n - k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = n - k, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = 0, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


def rotate_nk(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    for i in range(k):
        keep = nums[-1]
        for j in range(n)[::-1]:
            nums[j] = nums[j - 1]
        nums[0] = keep


def rotate_append(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]


examples = [
    {
        "nums": [1, 2, 3, 4, 5, 6, 7],
        "k": 3
    }, {
        "nums": [1],
        "k": 3
    }, {
        "nums": [1, 2, 3, 4, 5, 6, 7],
        "k": 10
    }, {
        "nums": [1, 2],
        "k": 1
    }
]


for example in examples:
    print rotate(example["nums"], example["k"])
