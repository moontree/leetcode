"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input:
    [1,2,3,4,4,3,2,1]
Output:
    true
Explanation:
    Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:

Input:
    [1,1,1,2,2,2,3,3]
Output:
    false
Explanation:
    No possible partition.

Example 3:

Input:
    [1]
Output:
    false
Explanation:
    No possible partition.

Example 4:

Input:
    [1,1]
Output:
    true
Explanation:
    Possible partition [1,1]

Example 5:

Input:
    [1,1,2,2,2,2]
Output:
    true
Explanation:
    Possible partition [1,1],[2,2],[2,2]

Note:
    1 <= deck.length <= 10000
    0 <= deck[i] < 10000
"""
import math


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        cache = {}
        for v in deck:
            cache[v] = cache.get(v, 0) + 1

        values = cache.values()
        val = values[0]
        for v in values:
            val = gcd(val, v)
            if val == 1:
                return False
        return True


examples = [
    {
        "input": {
            "deck": [1, 2, 3, 4, 4, 3, 2, 1],

        },
        "output": True
    }, {
        "input": {
            "deck": [1, 1, 1, 2, 2, 2, 3, 3],

        },
        "output": False
    }, {
        "input": {
            "deck": [1],

        },
        "output": False
    }, {
        "input": {
            "deck": [1, 1],

        },
        "output": True
    }, {
        "input": {
            "deck": [1, 1, 2, 2, 2, 2],

        },
        "output": True
    }, {
        "input": {
            "deck": [1, 1, 1, 1, 2, 2, 2, 2, 2, 2],

        },
        "output": True
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
