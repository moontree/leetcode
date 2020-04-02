"""
Given an array nums of positive integers.
Your task is to select some subset of nums,
multiply each element by an integer and add all these numbers.
The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

Example 1:

Input:
    nums = [12,5,7,23]
Output:
    true
Explanation:
    Pick numbers 5 and 7.
    5*3 + 7*(-2) = 1

Example 2:

Input:
    nums = [29,6,10]
Output:
    true
Explanation:
    Pick numbers 29, 6 and 10.
    29*1 + 6*(-3) + 10*(-1) = 1

Example 3:

Input:
    nums = [3,6]
Output:
    false

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""


class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        g = nums[0]
        for n in nums:
            g = gcd(g, n)
            if g == 1:
                return True
        return False


examples = [
    {
        "input": {
            "nums": [12, 5, 7, 23],
        },
        "output": True
    },  {
        "input": {
            "nums": [29, 6, 10],
        },
        "output": True
    },  {
        "input": {
            "nums": [3, 6],
        },
        "output": False
    },
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
