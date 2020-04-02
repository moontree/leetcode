"""
Given a set of distinct positive integers,
find the largest subset such that every pair (Si, Sj)
of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""


def largest_divisible_subset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    nums.sort()
    res = [[1, [i]] for i in nums]
    for i, v in enumerate(nums):
        pre_index = -1
        pre_len = 0
        for j in xrange(i):
            if v % nums[j] == 0 and pre_len < res[j][0]:
                pre_len = res[j][0]
                pre_index = j
        if pre_index > -1:
            res[i][0] = pre_len + 1
            res[i][1] = res[pre_index][1][:] + [v]
    longest = 0
    path = []
    for l, tpath in res:
        if longest < l:
            longest = l
            path = tpath
    # print res
    return path


examples = [
    {
        "nums": [1, 2, 3],
        "res": [1, 2]
    }, {
        "nums": [1, 2, 4, 8],
        "res": [1, 2, 4, 8]
    }, {
        "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "res": [1, 2, 4, 8]
    }, {
        "nums": [1],
        "res": [1, 2, 4, 8]
    }
]


for example in examples:
    print largest_divisible_subset(example["nums"])

