"""
There are N piles of stones arranged in a row.
The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile,
and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.



Example 1:

Input:
    stones = [3,2,4,1], K = 2
Output:
    20
Explanation:
    We start with [3, 2, 4, 1].
    We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
    We merge [4, 1] for a cost of 5, and we are left with [5, 5].
    We merge [5, 5] for a cost of 10, and we are left with [10].
    The total cost was 20, and this is the minimum possible.

Example 2:

Input:
    stones = [3,2,4,1], K = 3
Output:
    -1
Explanation:
    After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

Example 3:

Input:
    stones = [3,5,1,2,6], K = 3
Output:
    25
Explanation:
    We start with [3, 5, 1, 2, 6].
    We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
    We merge [3, 8, 6] for a cost of 17, and we are left with [17].
    The total cost was 25, and this is the minimum possible.


Note:

    1 <= stones.length <= 30
    2 <= K <= 30
    1 <= stones[i] <= 100
"""


class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        if n == 1:
            return 0
        pre_sum = [0]
        for s in stones:
            pre_sum.append(pre_sum[-1] + s)

        cache = {}

        def helper(i, j, k):
            if i > j:
                return float('inf')
            l = j - i + 1
            if l < k:
                return float('inf')
            if l == k:
                cache[(i, j, k)] = 0
            if (i, j, k) not in cache:
                if k == 1:
                    cache[(i, j, k)] = pre_sum[j + 1] - pre_sum[i] + helper(i, j, K)
                else:
                    res = float('inf')
                    for m in range(i, j):
                        res = min(res, helper(i, m, k - 1) + helper(m + 1, j, 1))
                    cache[(i, j, k)] = res
            return cache[(i, j, k)]

        res = helper(0, len(stones) - 1, 1)
        return res


examples = [
    {
        "input": {
            "stones": [3, 2, 4, 1],
            "K": 2
        },
        "output": 20
    }, {
        "input": {
            "stones": [1],
            "K": 2
        },
        "output": 0
    }, {
        "input": {
            "stones": [3, 2, 4, 1],
            "K": 3
        },
        "output": -1
    }, {
        "input": {
            "stones": [3, 5, 1, 2, 6],
            "K": 3
        },
        "output": 25
    }, {
        "input": {
            "stones": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "K": 3
        },
        "output": 87
    }, {
        "input": {
            "stones": [4, 6, 4, 7, 5],
            "K": 2
        },
        "output": 62
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
