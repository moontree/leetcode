"""
You have an initial power P,
an initial score of 0 points,
and a bag of tokens.

Each token can be used at most once,
has a value token[i], and has potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.


Example 1:

Input:
    tokens = [100], P = 50
Output:
    0

Example 2:

Input:
    tokens = [100,200], P = 150
Output:
    1

Example 3:

Input:
    tokens = [100,200,300,400], P = 200
Output:
    2

Note:
    tokens.length <= 1000
    0 <= tokens[i] < 10000
    0 <= P < 10000
"""


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        if len(tokens) == 0 or P < tokens[0]:
            return 0
        res = 0
        points = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            while l <= r and P >= tokens[l]:
                P -= tokens[l]
                l += 1
                points += 1
            if res < points:
                res = points
            points -= 1
            P += tokens[r]
            r -= 1
        return res


examples = [
    {
        "input": {
            "tokens": [100],
            "P": 50
        },
        "output": 0
    }, {
        "input": {
            "tokens": [100, 200],
            "P": 150
        },
        "output": 1
    }, {
        "input": {
            "tokens": [100, 200, 300, 400],
            "P": 200
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
