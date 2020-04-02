"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""
import bisect


def count_range_sum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    # prefix, thisSum, ans = [0], 0, 0
    # for n in nums:
    #     thisSum += n
    #     ans += bisect.bisect_right(prefix, thisSum - lower) - bisect.bisect_left(prefix, thisSum - upper)
    #     bisect.insort(prefix, thisSum)
    # return ans
    first = [0]
    for num in nums:
        first.append(first[-1] + num)
    print first
    def sort(lo, hi):
        mid = (lo + hi) / 2
        if mid == lo:
            return 0
        count = sort(lo, mid) + sort(mid, hi)
        i = j = mid
        for left in first[lo:mid]:
            while i < hi and first[i] - left < lower: i += 1
            while j < hi and first[j] - left <= upper: j += 1
            count += j - i
        # first[lo:hi] = sorted(first[lo:hi])
        return count

    res = sort(0, len(first))
    print first
    return res


examples = [
    {
        "nums": [-2, 5, -1],
        "lower": -2,
        "upper": 2,
        "res": 3
    }
]


for example in examples:
    print count_range_sum(example["nums"], example["lower"], example["upper"])
    