"""
You are installing a billboard and want it to have the largest height.
The billboard will have two steel supports, one on each side.
Each steel support must be an equal height.

You have a collection of rods which can be welded together.
For example, if you have rods of lengths 1, 2, and 3,
you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation.
 If you cannot support the billboard, return 0.



Example 1:

Input:
    [1,2,3,6]
Output:
    6
Explanation:
    We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.

Example 2:

Input:
    [1,2,3,4,5,6]
Output:
    10
Explanation:
    We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.

Example 3:

Input:
    [1,2]
Output:
    0
Explanation:
    The billboard cannot be supported, so we return 0.

Note:
    0 <= rods.length <= 20
    1 <= rods[i] <= 1000
    The sum of rods is at most 5000.
"""


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}
        for x in rods:
            for d, y in list(dp.items()):
                dp[d + x] = max(dp.get(x + d, 0), y)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
            print(dp)
        return dp[0]


examples = [
    {
        "input": {
            "rods": [1, 2, 3, 6],
        },
        "output": 6
    }, {
        "input": {
            "rods": [1, 2, 3, 4, 5, 6],
        },
        "output": 10
    }, {
        "input": {
            "rods": [1, 2],
        },
        "output": 0
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
