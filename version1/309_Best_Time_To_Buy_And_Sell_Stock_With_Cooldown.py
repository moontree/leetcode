"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 0: None 1: has_stock
        if len(prices) < 2:
            return 0
        dp = [[0 for _ in range(len(prices))], [-v for v in prices]]

        for i, v in enumerate(prices):
            # has_stock
            dp[1][i] = dp[0][i - 2] - v
            if i > 0:
                dp[1][i] = max(dp[1][i], dp[1][i - 1])
                dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + v)
        return max(dp[0][-1], dp[1][-1])


examples = [
    {
        "input": {
            "prices": [1, 2, 3, 0, 2],
        },
        "output": 3
    }, {
        "input": {
            "prices": [2, 1],
        },
        "output": 0
    }, {
        "input": {
            "prices": [1, 2, 4],
        },
        "output": 3
    }, {
        "input": {
            "prices": [2, 4, 1],
        },
        "output": 2
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
