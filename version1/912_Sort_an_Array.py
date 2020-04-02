"""
Given an array of integers nums, sort the array in ascending order.



Example 1:

Input:
    [5,2,3,1]
Output:
    [1,2,3,5]
Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Note:

1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def helper(nums, l, r):
            if l >= r:
                return
            ll, rr = l, r - 1
            # print('in while ----', nums[l: r + 1])
            while ll <= rr:
                while ll <= rr and nums[ll] <= nums[r]:
                    ll += 1
                while ll <= rr and nums[rr] > nums[r]:
                    rr -= 1
                if ll < rr:
                    nums[ll], nums[rr] = nums[rr], nums[ll]
                # print(ll, rr, nums[l: r + 1])
            # print('after while', ll, rr, r, nums[l: r + 1])
            nums[ll], nums[r] = nums[r], nums[ll]
            # print(l, r, ll, rr, nums)

            helper(nums, l, ll - 1)
            helper(nums, ll + 1, r)

        helper(nums, 0, len(nums) - 1)
        return nums


examples = [
    {
        "input": {
            "nums": [5, 2, 3, 1],
        },
        "output": [1, 2, 3, 5]
    }, {
        "input": {
            "nums": [5, 1, 1, 2, 0, 0],
        },
        "output": [0, 0, 1, 1, 2, 5]
    }, {
        "input": {
            "nums": [1, 2, 3, 4, 5],
        },
        "output": [1, 2, 3, 4, 5]
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
