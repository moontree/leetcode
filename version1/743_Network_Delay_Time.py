"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K.
How long will it take for all nodes to receive the signal? If it is impossible, return -1.



Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2


Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        paths = {}
        for s, t, time in times:
            if s in paths:
                paths[s].append([t, time])
            else:
                paths[s] = [[t, time]]
        q = [K]
        cache = {K: 0}
        while q:
            cur = q.pop(0)
            if cur not in paths:
                continue
            for v, w in paths[cur]:
                tmp = cache[cur] + w
                if cache.get(v, float('inf')) > tmp:
                    cache[v] = tmp
                    q.append(v)
        res = max(cache.values())
        print paths
        print cache
        if len(cache) == N:
            return res
        return -1


examples = [
    {
        "input": {
            "times": [
                [2, 1, 1],
                [2, 3, 1],
                [3, 4, 1]
            ],
            "N": 4,
            "K": 2
        },
        "output": 2
    }, {
        "input": {
            "times": [
                [2, 1, 1],
                [2, 3, 1],
                [3, 1, 1]
            ],
            "N": 4,
            "K": 2
        },
        "output": -1
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