"""
Given an array A of non-negative integers,
the array is squareful if for every pair of adjacent elements,
their sum is a perfect square.

Return the number of permutations of A that are squareful.
Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].



Example 1:

Input:
    [1,17,8]
Output:
    2
Explanation:
    [1,8,17] and [17,8,1] are the valid permutations.

Example 2:
Input:
    [2,2,2]
Output:
    1

Note:
    1 <= A.length <= 12
    0 <= A[i] <= 1e9
"""
import math


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counts = {}
        for v in A:
            counts[v] = counts.get(v, 0) + 1
        values = counts.keys()
        cache = {v: [] for v in values}
        for a in values:
            for b in values:
                if a == b and counts[a] == 1:
                    continue
                s = a + b
                r = int(math.sqrt(s))
                if r * r == s:
                    cache[a].append(b)
        # res = []
        self.res = 0

        def helper(cur):
            if len(cur) == len(A):
                # res.append(cur)
                self.res += 1
            for v in cache[cur[-1]]:
                if counts[v] > 0:
                    counts[v] -= 1
                    helper(cur + [v])
                    counts[v] += 1

        for v in values:
            counts[v] -= 1
            helper([v])
            counts[v] += 1

        return self.res


examples = [
    {
        "input": {
            "A": [1, 17, 8],
        },
        "output": 2
    }, {
        "input": {
            "A": [2, 2, 2],
        },
        "output": 1
    }, {
        "input": {
            "A": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        },
        "output": 1
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
