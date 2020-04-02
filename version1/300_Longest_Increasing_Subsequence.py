"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101],
 therefore the length is 4.
 Note that there may be more than one LIS combination,
 it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


def length_of_LIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    res, records = 1, [[], [nums[0]]]
    for p in nums:
        if p > records[-1][-1]:
            records.append(records[-1][:] + [p])
            res += 1
        else:
            for j in xrange(res, -1, -1):
                if j == 0:
                    records[1] = [p]
                elif p > records[j][-1]:
                    records[j + 1] = records[j][:] + [p]
                    break
    return res


examples = [
    {
        "nums": [10, 9, 2, 5, 3, 7, 101, 18],
        "res": 4
    }, {
        "nums": [1, 9, 10, 5, 6, 2, 3, 4, 5],
        "res": 5
    }
]


for example in examples:
    print length_of_LIS(example["nums"])
