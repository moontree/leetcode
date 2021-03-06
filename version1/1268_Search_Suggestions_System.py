# --*-- encoding: utf-8 --*--
"""
Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names
from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix
return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input:
    products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output:
    [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]
Explanation:
    products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input:
    products = ["havana"], searchWord = "havana"
Output:
    [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input:
    products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output:
    [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input:
    products = ["havana"], searchWord = "tatiana"
Output:
    [[],[],[],[],[],[],[]]


Constraints:

    1 <= products.length <= 1000
    There are no repeated elements in products.
    1 <= Σ products[i].length <= 2 * 10^4
    All characters of products[i] are lower-case English letters.
    1 <= searchWord.length <= 1000
    All characters of searchWord are lower-case English letters.
"""


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        res = []
        q = products[:]
        for i, c in enumerate(searchWord):
            cur = []
            for p in q:
                if i < len(p) and p[i] == c:
                    cur.append(p)
            cur.sort()
            res.append(cur[:3])
            q = cur[:]

        return res


examples = [
    {
        "input": {
            "products": ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "searchWord": "mouse"
        },
        "output":  [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"]
        ]
    }, {
        "input": {
            "products": ["havana"],
            "searchWord": "havana"
        },
        "output": [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
    }, {
        "input": {
            "products": ["bags", "baggage", "banner", "box", "cloths"],
            "searchWord": "bags"
        },
        "output": [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"]
        ]
    }, {
        "input": {
            "products": ["havana"],
            "searchWord": "tatiana"
        },
        "output":  [[], [], [], [], [], [], []]
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
