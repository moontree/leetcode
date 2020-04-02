"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.
Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)



Example 1:

Input:
    [2,7,4,1,8,1]
Output:
    1
Explanation:
    We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
    we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
    we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.

Note:
    1 <= stones.length <= 30
    1 <= stones[i] <= 100
"""


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # s = sum(stones)
        # target = s / 2
        # dp = [0 for _ in range(target + 1)]
        # for i in range(len(stones)):
        #     for w in range(stones[i], target + 1)[::-1]:
        #         dp[w] = max(dp[w], dp[w - stones[i]] + stones[i])
        # return s - dp[-1] * 2
        target = sum(stones) / 2.0
        candidates = {0}
        for x in stones:
            addition = set()
            for y in candidates:
                if x + y <= target:
                    addition.add(x + y)
            candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))


examples = [
    {
        "input": {
            "stones": [2, 7, 4, 1, 8, 1],
        },
        "output": 1
    }, {
        "input": {
            "stones": [31, 26, 33, 21, 40],
        },
        "output": 5
    }, {
        "input": {
            "stones": [1, 2, 3],
        },
        "output": 0
    }, {
        "input": {
            "stones": [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98],
        },
        "output": 1
    }, {
        "input": {
            "stones": [1, 2, 3, 6],
        },
        "output": 0
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
