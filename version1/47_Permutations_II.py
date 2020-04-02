"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


def permute2(nums):
    rest = 0
    for key in nums:
        rest += nums[key]
    if rest == 0:
        return [[]]
    res = []
    for key in nums:
        if nums[key] > 0:
            head = key
            nums[key] -= 1
            for p in permute2(nums):
                res.append([head] + p)
            nums[key] += 1
    return res


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    mapped = {}
    for i in nums:
        mapped[i] = mapped.get(i, 0) + 1
    print mapped
    return permute2(mapped)


print permute([1])
