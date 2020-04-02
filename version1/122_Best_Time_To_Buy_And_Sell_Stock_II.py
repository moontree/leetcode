"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
 (ie, buy one and sell one share of the stock multiple times).
 However, you may not engage in multiple transactions at the same time
 (ie, you must sell the stock before you buy again).
"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    res = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            res += prices[i + 1] - prices[i]
    return res


examples = [
    {
        "prices": [7, 1, 5, 4, 6, 4],
        "res": 6,
    },{
        "prices": [7, 1, 2, 4, 6, 4],
        "res": 5,
    }, {
        "prices": [7, 6, 4, 3, 1],
        "res": 0,
    }
]


for example in examples:
    print max_profit(example["prices"])
