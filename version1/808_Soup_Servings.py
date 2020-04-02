"""
There are two types of soup:
type A and type B.
Initially we have N ml of each type of soup.
There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B
Serve 75 ml of soup A and 25 ml of soup B
Serve 50 ml of soup A and 50 ml of soup B
Serve 25 ml of soup A and 75 ml of soup B

When we serve some soup,
we give it to someone and we no longer have it.
Each turn, we will choose from the four operations with equal probability 0.25.
If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can.
We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first,
plus half the probability that A and B become empty at the same time.



Example:
Input:
    N = 50
Output:
    0.625
Explanation:
    If we choose the first two operations, A will become empty first.
    For the third operation, A and B will become empty at the same time.
    For the fourth operation, B will become empty first.
    So the total probability of A becoming empty first plus
    half the probability that A and B become empty at the same time,
    is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Notes:
    0 <= N <= 10^9.
    Answers within 10^-6 of the true value will be accepted as correct.
"""


class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 4800:
            return 1

        cache = {}

        def helper(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.
            elif b <= 0:
                return 0.
            if (a, b) not in cache:
                v = helper(a - 100, b) + helper(a - 75, b - 25) + helper(a - 50, b - 50) + helper(a - 25, b - 75)
                cache[(a, b)] = 0.25 * v
            return cache[(a, b)]

        res = helper(N, N)
        return res


examples = [
    {
        "input": {
            "N": 50
        },
        "output": 0.625
    }, {
        "input": {
            "N": 0
        },
        "output": 0.5
    }, {
        "input": {
            "N": 100
        },
        "output": 0.71875
    }, {
        "input": {
            "N": 101
        },
        "output": 0.74219
    }, {
        "input": {
            "N": 150
        },
        "output": 0.75781
    }, {
        "input": {
            "N": 200
        },
        "output": 0.79688
    }, {
        "input": {
            "N": 1000
        },
        "output": 1
    }
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