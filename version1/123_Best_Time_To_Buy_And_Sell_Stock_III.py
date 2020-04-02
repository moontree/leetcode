"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    count = len(prices)
    if len(prices) == 0:
        return 0
    profits = []
    min_price = prices[0]
    max_profits = 0
    for p in prices:
        if min_price > p:
            min_price = p
        if p - min_price > max_profits:
            max_profits = p - min_price
        profits.append(max_profits)
    print profits

    max_price = prices[-1]
    max_profits = 0
    profits2 = []
    for j in range(count - 1, -1, -1):
        if max_price < prices[j]:
            max_price = prices[j]
        tmp_profit = max_price - prices[j]
        profits2.append(tmp_profit)
        if tmp_profit + profits[j] > max_profits:
            max_profits = tmp_profit + profits[j]
    print profits2[::-1]
    return max_profits
    # buy_price_1 = buy_price_2 = float('inf')
    # profit_1 = profit_2 = 0
    # for p in prices:
    #     profit_2 = max(profit_2, p - buy_price_2)
    #     buy_price_2 = min(buy_price_2, p - profit_1)
    #     profit_1 = max(profit_1, p - buy_price_1)
    #     buy_price_1 = min(buy_price_1, p)
    #     print buy_price_1, profit_1, p, buy_price_2, profit_2
    # return profit_2


examples = [
    {
        "prices": [7, 1, 5, 4, 6, 4],
        "res": 6,
    }, {
        "prices": [7, 1, 2, 4, 6, 4],
        "res": 5,
    }, {
        "prices": [7, 6, 4, 3, 1],
        "res": 0,
    }, {
        "prices": [4, 4, 5, 0, 0, 3, 1, 4],
        "res": 6,
    }, {
        "prices": [1, 2],
        "res": 1,
    }
]


for example in examples:
    print max_profit(example["prices"])
