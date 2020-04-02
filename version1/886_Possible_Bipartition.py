"""
Given a set of N people (numbered 1, 2, ..., N),
we would like to split everyone into two groups of any size.

Each person may dislike some other people,
and they should not go into the same group.

Formally, if dislikes[i] = [a, b],
it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input:
    N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output:
    true
Explanation:
    group1 [1,4], group2 [2,3]

Example 2:

Input:
    N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output:
    false

Example 3:

Input:
    N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output:
    false


    Note:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].

"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        cache = {
            i: [] for i in range(1, N + 1)
        }
        groups = {}
        used = {}
        for x, y in dislikes:
            cache[x].append(y)
            cache[y].append(x)
        for i in range(1, N + 1):
            if i in used:
                pass
            elif len(cache[i]) == 0:
                used[i] = True
            else:
                q = [[i, 0]]
                groups[i] = 0
                used[i] = True
                while q:
                    tmp = []
                    for s, f in q:
                        for t in cache[s]:
                            if t not in used:
                                tmp.append([t, 1 - f])
                            if t in groups and groups[t] != 1 - f:
                                return False
                            else:
                                groups[t] = 1 - f
                                used[t] = True
                    q = tmp
        return True


examples = [
    {
        "input": {
            "N": 4,
            "dislikes": [[1, 2], [1, 3], [2, 4]]
        },
        "output": True
    }, {
        "input": {
            "N": 3,
            "dislikes": [[1, 2], [1, 3], [2, 3]]
        },
        "output": False
    }, {
        "input": {
            "N": 5,
            "dislikes": [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        },
        "output": False
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
        v = func(**example['input'])
        print v, v == example['output']