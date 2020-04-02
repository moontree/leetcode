"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
 Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

"""


def find_target_sum_ways(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    val = sum(nums)
    dp = {i: {} for i in xrange(len(nums))}
    if val < abs(S):
        return 0
    for i, v in enumerate(nums):
        if i == 0:
            dp[i][v] = dp[i].get(v, 0) + 1
            dp[i][-v] = dp[i].get(-v, 0) + 1
        else:
            for key in dp[i - 1]:
                dp[i][key + v] = dp[i].get(key + v, 0) + dp[i - 1][key]
                dp[i][key - v] = dp[i].get(key - v, 0) + dp[i - 1][key]
    return dp[len(nums) - 1].get(S, 0)
    # count = 0
    #
    # def helper(prefix, idx, cur, target, res):
    #     if idx >= len(nums):
    #         if cur == target:
    #             res.append(prefix[:])
    #         return
    #     prefix.append("-")
    #     helper(prefix, idx + 1, cur - nums[idx], target, res)
    #     prefix[-1] = "+"
    #     helper(prefix, idx + 1, cur + nums[idx], target, res)
    #     prefix.pop()
    #
    # cc = []
    # helper([], 0, 0, S, cc)
    # # print cc
    # return len(cc)


examples = [
    {
        "nums": [1, 1, 1, 1, 1],
        "S": 3,
        "res": 5
    }, {
        "nums": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        "S": 0,
        "res": 1048576
    }, {
        "nums": [42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47],
        "S": 38,
        "res": 5602
    }
]


for example in examples:
    print find_target_sum_ways(example["nums"], example["S"])
