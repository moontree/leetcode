"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


def subsets_with_dup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    mid = []
    for key in counts:
        mid.append([key, counts[key]])
    return subsets(mid)


def subsets(counts):
    if len(counts) == 0:
        return [[]]
    else:
        processing = counts.pop()
        previous = subsets(counts)
        res = []
        for k in range(processing[1] + 1):
            for p in previous:
                res.append(p + [processing[0]] * k)
        return res


print subsets_with_dup([])
