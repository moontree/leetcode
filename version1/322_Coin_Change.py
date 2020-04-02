"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""


def coin_change(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    vals = [float('inf') for _ in xrange(amount + 1)]
    for coin in coins:
        if coin < amount + 1:
            vals[coin] = 1
    vals[0] = 0
    for i in xrange(1, amount + 1):
        count = float("inf")
        for coin in coins:
            if i - coin > -1:
                if vals[i - coin] + 1 < count:
                    count = vals[i - coin] + 1
        vals[i] = count
    if vals[-1] != float("inf"):
        return vals[-1]
    else:
        return -1


examples = [
    {
        "coins": [1, 2, 5],
        "amount": 11,
        "res": 3
    }, {
        "coins": [2],
        "amount": 3,
        "res": -1
    }, {
        "coins": [1],
        "amount": 0,
        "res": -1
    }
]


for example in examples:
    print coin_change(example["coins"], example["amount"])
