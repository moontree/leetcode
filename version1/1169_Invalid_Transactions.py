"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values
representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions,
return a list of transactions that are possibly invalid.
You may return the answer in any order.



Example 1:

Input:
    transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output:
    ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation:
    The first transaction is invalid because the second transaction occurs within a difference of 60 minutes,
    have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:

Input:
    transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output:
    ["alice,50,1200,mtv"]

Example 3:

Input:
    transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output:
    ["bob,50,1200,mtv"]

Constraints:
    transactions.length <= 1000
    Each transactions[i] takes the form "{name},{time},{amount},{city}"
    Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
    Each {time} consist of digits, and represent an integer between 0 and 1000.
    Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""


class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        res = {}
        cache = {}
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            if int(amount) > 1000:
                res[transaction] = True
            if name not in cache:
                cache[name] = []
            cache[name].append([int(time), city, transaction])
        for pairs in cache.values():
            n = len(pairs)
            for i in range(n):
                for j in range(i + 1, n):
                    if abs(pairs[i][0] - pairs[j][0]) <= 60 and pairs[i][1] != pairs[j][1]:
                        res[pairs[i][-1]] = True
                        res[pairs[j][-1]] = True
        return res.keys()


examples = [
    {
        "input": {
            "transactions": ["alice,20,800,mtv", "alice,50,100,beijing"],
        },
        "output": ["alice,20,800,mtv", "alice,50,100,beijing"]
    }, {
        "input": {
            "transactions": ["alice,20,800,mtv", "alice,50,1200,mtv"],
        },
        "output": ["alice,50,1200,mtv"]
    }, {
        "input": {
            "transactions": ["alice,20,800,mtv", "bob,50,1200,mtv"],
        },
        "output": ["bob,50,1200,mtv"]
    }, {
        "input": {
            "transactions": [
                "bob,689,1910,barcelona",
                "alex,696,122,bangkok",
                "bob,832,1726,barcelona",
                "bob,820,596,bangkok",
                "chalicefy,217,669,barcelona",
                "bob,175,221,amsterdam"
            ],
        },
        "output": ["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok"]
    },
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
