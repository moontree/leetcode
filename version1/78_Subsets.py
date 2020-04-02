"""
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


def combine(nums, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    n = len(nums)
    if n < k or k == 0:
        return [[]]
    if k == n:
        return [nums]
    if k == 1:
        return [[i] for i in nums]
    else:
        res1 = combine(nums[: -1], k)
        res2 = combine(nums[: -1], k - 1)
        res = [[nums[-1]] + p for p in res2]
        res += res1
        return res


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for k in range(0, len(nums) + 1):
        res += combine(nums, k)
    return res
    # i = 0
    # count = len(nums)
    # total_nums = 1 << len(nums)
    # res = []
    # vals = {'0': 0, '1': 1}
    # while i < total_nums:
    #     needed = bin(i)[2:].rjust(count, '0')
    #     tmp = []
    #     for j in range(count):
    #         if vals[needed[j]]:
    #             tmp.append(nums[j])
    #     res.append(tmp)
    #     i += 1
    # return res


print subsets([1, 2, 0])
