"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        m = len(nums)
        self.sums = [0 for _ in xrange(m + 1)]
        tmp_sum = [0 for _ in xrange(m + 1)]
        for i in xrange(m):
            tmp_sum[i + 1] = tmp_sum[i] + nums[i]
        for i in xrange(m):
            index = i + 1
            diff = index & -index
            self.sums[index] = tmp_sum[index] - tmp_sum[index - diff]
        print self.sums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        stop = len(self.nums) + 1
        while i < stop:
            self.sums[i] += diff
            i += i & -i

    def sum_range(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum(j) - self._sum(i - 1)

    def _sum(self, i):
        i += 1
        res = 0
        while i:
            res += self.sums[i]
            i -= i & -i
        return res


obj = NumArray([1, 2, 3, 4, 5, 6])
print obj.sum_range(0, 3)
obj.update(0, 0)
print obj.sum_range(0, 3)
