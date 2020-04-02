"""
=========================
Project -> File: leetcode -> 1388_Pizza_With_3n_Slices.py
Author: zhangchao
=========================
There is a pizza with 3n slices of varying size,
you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick next slice in anti clockwise direction of your pick.
Your friend Bob will pick next slice in clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

Example 1:

Input:
    slices = [1,2,3,4,5,6]
Output:
    10
Explanation:
    Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively.
    Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively.
    Total = 4 + 6.

Example 2:

Input:
    slices = [8,9,8,6,1,1]
Output:
    16
Output:
    Pick pizza slice of size 8 in each turn.
    If you pick slice with size 9 your partners will pick slices of size 8.

Example 3:

Input:
    slices = [4,1,2,5,8,3,1,9,7]
Output:
    21

Example 4:

Input:
    slices = [3,1,2]
Output:
    3


Constraints:

    1 <= slices.length <= 500
    slices.length % 3 == 0
    1 <= slices[i] <= 1000
"""


class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        n = len(slices)
        t = n / 3

        def helper(nums):
            dp = [[0 for _ in range(t + 1)] for _ in range(len(nums))]
            for i in range(len(nums)):
                for j in range(1, t + 1):
                    v1 = 0 if i < 2 else dp[i - 2][j - 1]
                    v2 = 0 if i < 1 else dp[i - 1][j]
                    dp[i][j] = max(v1 + nums[i], v2)
            return dp[-1][-1]
        return max(helper(slices[1:]), helper(slices[: -1]))


examples = [
    {
        "input": {
            "slices": [1, 2, 3, 4, 5, 6],
        },
        "output": 10
    }, {
        "input": {
            "slices": [8, 9, 8, 6, 1, 1],
        },
        "output": 16
    }, {
        "input": {
            "slices": [4, 1, 2, 5, 8, 3, 1, 9, 7],
        },
        "output": 21
    }, {
        "input": {
            "slices": [3, 1, 2],
        },
        "output": 3
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
