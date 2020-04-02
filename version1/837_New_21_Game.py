"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.
During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.
What is the probability that she has N or less points?

Example 1:

Input:
    N = 10, K = 1, W = 10
Output:
    1.00000
Explanation:
    Alice gets a single card, then stops.

Example 2:

Input:
    N = 6, K = 1, W = 10
Output:
    0.60000
Explanation:
    Alice gets a single card, then stops.
    In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:

Input:
    N = 21, K = 17, W = 10
Output:
    0.73278
Note:

    0 <= K <= N <= 10000
    1 <= W <= 10000
    Answers will be accepted as correct if they are within 10^-5 of the correct answer.
    The judging time limit has been reduced for this question.
"""


class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        q, s = [], 0.0
        for jj in range(N, -1, -1):
            u = 1.0 if jj >= K else (1.0 / W * s)
            s += u + (-q.pop(0) if len(q) == W else 0)
            q.append(u)
        return q[-1]


examples = [
    {
        "input": {
            "N": 10,
            "K": 1,
            "W": 10
        },
        "output": 1.000
    }, {
        "input": {
            "N": 6,
            "K": 1,
            "W": 10
        },
        "output": 0.60000
    }, {
        "input": {
            "N": 21,
            "K": 17,
            "W": 10
        },
        "output": 0.73278
    }, {
        "input": {
            "N": 6,
            "K": 2,
            "W": 10
        },
        "output": 0.55
    }, {
        "input": {
            "N": 0,
            "K": 0,
            "W": 2
        },
        "output": 01.
    }, {
        "input": {
            "N": 5710,
            "K": 5070,
            "W": 8516
        },
        "output": 0.13649
    },
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']



