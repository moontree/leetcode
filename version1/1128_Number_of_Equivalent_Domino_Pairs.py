"""
Given a list of dominoes,
dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
if and only if either (a==c and b==d), or (a==d and b==c) -
that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
and dominoes[i] is equivalent to dominoes[j].



Example 1:

Input: dominoes =
    [[1,2],[2,1],[3,4],[5,6]]
Output:
    1

Constraints:
    1 <= dominoes.length <= 40000
    1 <= dominoes[i][j] <= 9
"""


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        nums = [[0 for _ in range(10)] for _ in range(10)]
        for a, b in dominoes:
            nums[a][b] += 1
        res = 0
        for i in range(1, 10):
            for j in range(1, 10):
                if i < j:
                    res += nums[i][j] * nums[j][i]
                    res += nums[i][j] * (nums[i][j] - 1) / 2
                    res += nums[j][i] * (nums[j][i] - 1) / 2
                elif i == j:
                    res += nums[i][j] * (nums[i][j] - 1) / 2
                else:
                    continue
        return res


examples = [
    {
        "input": {
            "dominoes": [[1, 2], [2, 1], [3, 4], [5, 6]],
        },
        "output": 1
    }, {
        "input": {
            "dominoes":  [[2, 2], [1, 2], [1, 2], [1, 1], [1, 2], [1, 1], [2, 2]],
        },
        "output": 5
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
