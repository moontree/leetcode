"""
Your are given an array of integers prices,
for which the i-th element is the price of a given stock on day i;
 and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time
(ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input:
    prices = [1, 3, 2, 8, 4, 9], fee = 2
Output:
    8
Explanation:
    The maximum profit can be achieved by:
    Buying at prices[0] = 1
    Selling at prices[3] = 8
    Buying at prices[4] = 4
    Selling at prices[5] = 9
    The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""



class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        hold, sold = -prices[0], 0
        for i in range(1, n):
            hold, sold = max(hold, sold - prices[i]), max(sold, hold + prices[i] - fee)
        return max(hold, sold)
        # n = len(prices)
        # dp = [[0, 0] for _ in range(n)]
        # dp[0] = [-prices[0], 0]
        # # dp[i][0]: keep one
        # # dp[i][1]: keep zero
        # for i in range(1, n):
        #     # print dp[i - 1], prices[i]
        #     dp[i][0] = max(dp[i -1][0], dp[i - 1][1] - prices[i])
        #     dp[i][1] = max(dp[i -1][1], dp[i - 1][0] + prices[i] - fee)
        # return max(dp[-1])


examples = [
    {
        "input": {
            "prices": [1, 3, 2, 8, 4, 9],
            "fee": 2
        },
        "output": 8
    },
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']
