"""
Given a sorted positive integer array nums and an integer n,
add/patch elements to the array such that any number in range [1, n]
inclusive can be formed by the sum of some elements in the array.
 Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""


def min_patches(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    # patch = []
    reached = 0
    c = len(nums)
    i = 0
    res = 0
    while reached < n:
        if i < c and reached + 1 >= nums[i]:
            reached += nums[i]
            i += 1
        else:
            # patch.append(reached + 1)
            reached += reached + 1
            res += 1
    return res


examples = [
    {
        "nums": [1, 3],
        "n": 6,
        "res": 1,
    }, {
        "nums": [1, 5, 10],
        "n": 20,
        "res": 2,
    }, {
        "nums": [1, 2, 2],
        "n": 5,
        "res": 0,
    }
]


for example in examples:
    print min_patches(example["nums"], example["n"])
