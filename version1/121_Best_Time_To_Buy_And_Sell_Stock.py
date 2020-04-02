"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
 design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)


Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    res = 0
    val = float('inf')
    for p in prices:
        if p < val:
            val = p
        else:
            tmp = p - val
            if tmp > res:
                res = tmp
    return res


examples = [
    {
        "prices": [7, 1, 5, 4, 6, 4],
        "res": 5,
    }, {
        "prices": [7, 6, 4, 3, 1],
        "res": 0,
    }
]


for example in examples:
    print max_profit(example["prices"])
