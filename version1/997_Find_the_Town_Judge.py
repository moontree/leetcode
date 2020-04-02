"""
In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust,
 an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified,
return the label of the town judge.
Otherwise, return -1.



Example 1:

Input:
    N = 2, trust = [[1,2]]
Output:
    2

Example 2:

Input:
    N = 3, trust = [[1,3],[2,3]]
Output:
    3

Example 3:

Input:
    N = 3, trust = [[1,3],[2,3],[3,1]]
Output:
    -1

Example 4:
Input:
    N = 3, trust = [[1,2],[2,3]]
Output:
    -1

Example 5:

Input:
    N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output:
    3


Note:

    1 <= N <= 1000
    trust.length <= 10000
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N
"""


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        ins, outs = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]
        for s, t in trust:
            ins[t] += 1
            outs[s] += 1
        for i in range(1, N + 1):
            if ins[i] == N - 1 and outs[i] == 0:
                return i
        return -1


examples = [
    {
        "input": {
            "N": 2,
            "trust": [[1, 2]]
        },
        "output": 2
    }, {
        "input": {
            "N": 3,
            "trust": [[1, 3], [2, 3]]
        },
        "output": 3
    }, {
        "input": {
            "N": 3,
            "trust": [[1, 3], [2, 3], [3, 1]]
        },
        "output": -1
    }, {
        "input": {
            "N": 3,
            "trust": [[1, 2], [2, 3]]
        },
        "output": -1
    }, {
        "input": {
            "N": 4,
            "trust": [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
        },
        "output": 3
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
