"""
Given an array nums of integers,
a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.



Example 1:

Input:
    nums = [1,2,3]
Output:
    2
Explanation:
    We can decrease 2 to 0 or 3 to 1.

Example 2:

Input:
    nums = [9,6,1,6,2]
Output:
    4

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
"""


class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_diff, max_diff = 0, 0
        n = len(nums)
        for i in range(1, n, 2):
            l = r = nums[i - 1]
            if i + 1 < n:
                r = nums[i + 1]
            min_diff += max(0, nums[i] - min(l, r) + 1)
        for i in range(0, n, 2):
            if i == 0:
                l = r = nums[i + 1]
            else:
                l = r = nums[i - 1]
            if i + 1 < n:
                r = nums[i + 1]
            max_diff += max(0, nums[i] - min(l, r) + 1)
        return min(min_diff, max_diff)


examples = [
    {
        "input": {
            "nums": [1, 2, 3],
        },
        "output": 2
    }, {
        "input": {
            "nums": [9, 6, 1, 6, 2],
        },
        "output": 4
    }, {
        "input": {
            "nums":  [2, 7, 10, 9, 8, 9],
        },
        "output": 4
    }
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
