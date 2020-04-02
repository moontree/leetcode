"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps.
You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0,
or the step with index 1.

Example 1:
Input:
    cost = [10, 15, 20]
Output:
    15
Explanation:
    Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input:
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output:
    6
Explanation:
    Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        c = len(cost)
        a, b = cost[0], cost[1]
        for i in range(2, c):
            v = min(a, b) + cost[i]
            a, b = b, v
        return min(a, b)


examples = [
    {
        "input": {
            "cost": [10, 15, 20],
        },
        "output": 15
    }, {
        "input": {
            "cost": [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        },
        "output": 6
    }, {
        "input": {
            "cost": [1, 2],
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