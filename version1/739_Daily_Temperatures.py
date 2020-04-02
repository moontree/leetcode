"""
Given a list of daily temperatures T,
return a list such that,
for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example,
given the list of temperatures
T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        q = []
        res = [0 for _ in range(len(T))]
        for i, t in enumerate(T):
            while q and t > T[q[-1]]:
                res[q[-1]] = i - q[-1]
                q.pop()
            q.append(i)
        print res
        return res


examples = [
    {
        "input": {
            "T": [73, 74, 75, 71, 69, 72, 76, 73]
        },
        "output": [1, 1, 4, 2, 1, 1, 0, 0]
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