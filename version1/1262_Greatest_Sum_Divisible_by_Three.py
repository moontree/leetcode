"""
Given an array nums of integers,
we need to find the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""


class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = [[] for _ in range(3)]
        s = 0
        for n in nums:
            vals[n % 3].append(n)
            s += n
        if s % 3 == 0:
            return s
        elif s % 3 == 1:
            vals[1].sort()
            vals[2].sort()
            a = float('inf') if len(vals[1]) == 0 else vals[1][0]
            b = float('inf') if len(vals[2]) < 2 else vals[2][0] + vals[2][1]
            return s - min(a, b)
        elif s % 3 == 2:
            vals[1].sort()
            vals[2].sort()
            a = float('inf') if len(vals[1]) < 2 else vals[1][0] + vals[1][1]
            b = float('inf') if len(vals[2]) < 1 else vals[2][0]
            return s - min(a, b)


examples = [
    {
        "input": {
            "nums": [3, 6, 5, 1, 8],
        },
        "output": 18
    }, {
        "input": {
            "nums": [4],
        },
        "output": 0
    }, {
        "input": {
            "nums": [1, 2, 3, 4, 4],
        },
        "output": 12
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
