"""
Given n balloons, indexed from 0 to n-1.
Each balloon is painted with a number on it represented by array nums.
 You are asked to burst all the balloons.
  If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
   Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <= 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


def max_coins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in xrange(n)] for _ in xrange(n)]

    def calculate(i, j):
        if dp[i][j] or j == i + 1:
            return dp[i][j]
        coins = 0
        for k in xrange(i + 1, j):
            k_coins = nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j)
            if k_coins > coins:
                coins = k_coins
        dp[i][j] = coins
        return coins
    val = calculate(0, n - 1)
    return val


examples = [
    {
        "nums": [3, 1, 5, 8],
        "res": 167
    }, {
        "nums": [3],
        "res": 3
    }
]


for example in examples:
    print max_coins(example["nums"])
