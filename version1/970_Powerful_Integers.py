"""
Given two positive integers x and y,
an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.
 In your answer, each value should occur at most once.



Example 1:

Input:
    x = 2, y = 3, bound = 10
Output:
    [2,3,4,5,7,9,10]
Explanation:
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2

Example 2:

Input:
    x = 3, y = 5, bound = 15
Output:
    [2,4,6,8,10,14]

Note:
    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
"""


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        xx, yy = [], [1]
        xv, yv = 1, 1
        while xv < bound:
            xx.append(xv)
            xv *= x
            if xv == xx[-1]:
                break
        while yv < bound:
            yy.append(yv)
            yv *= y
            if yv == yy[-1]:
                break
        cache = {}
        for x in xx:
            for y in yy:
                tmp = x + y
                if tmp <= bound:
                    cache[tmp] = True
        return cache.keys()


examples = [
    {
        "input": {
            "x": 2,
            "y": 3,
            "bound": 10
        },
        "output": [2, 3, 4, 5, 7, 9, 10]
    }, {
        "input": {
            "x": 3,
            "y": 5,
            "bound": 15
        },
        "output": [2, 4, 6, 8, 10, 14]
    }, {
        "input": {
            "x": 1,
            "y": 1,
            "bound": 10
        },
        "output": [2]
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
