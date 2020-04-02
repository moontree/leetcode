"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]
    for c in nums:
        new_res = []
        for t in res:
            for j in range(len(t) + 1):
                new_res.append(t[:j] + [c] + t[j:])
        res = new_res
    return res


def permute_recursive(nums):
    return nums and [p[:i] + [nums[0]] + p[i:] for p in permute(nums[1:]) for i in range(len(nums))] or [[]]


def permute_recursive_2(nums):
    if len(nums) == 0:
        return [[]]
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        head = nums[i]
        rest = nums[:i] + nums[i + 1:]
        for p in permute_recursive_2(rest):
            res.append([head] + p)
    return res


print permute([1, 4, 5])
