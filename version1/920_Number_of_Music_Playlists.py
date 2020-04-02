"""
Your music player contains N different songs and she wants to listen to L
(not necessarily different) songs during your trip.

You create a playlist so that:

Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input:
    N = 3, L = 3, K = 1
Output:
    6
Explanation:
    There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].

Example 2:

Input:
    N = 2, L = 3, K = 0
Output:
    6
Explanation:
    There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]

Example 3:

Input:
    N = 2, L = 3, K = 1
Output:
    2
Explanation:
    There are 2 possible playlists. [1, 2, 1], [2, 1, 2]

Note:

0 <= K < N <= L <= 100
"""


class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        base = 10 ** 9 + 7

        def helper(n):
            res = 1
            for i in range(2, n + 1):
                res = (res * i) % base
            return res
        cache = {}

        def count(N, L):
            if N == L:
                return helper(N)
            elif N == K:
                return 0
            elif N < K:
                return 0
            else:
                if (N, L) not in cache:
                    if (N, L - 1) not in cache:
                        cache[(N, L - 1)] = count(N, L - 1)
                    if (N - 1, L - 1) not in cache:
                        cache[(N - 1, L - 1)] = count(N - 1, L - 1)
                    cache[(N, L)] = (cache[(N, L - 1)] * (N - K) + cache[(N - 1, L - 1)] * N) % base

            return cache[(N, L)]

        return count(N, L)


examples = [
    {
        "input": {
            "N": 3,
            "L": 3,
            "K": 1
        },
        "output": 6
    }, {
        "input": {
            "N": 2,
            "L": 3,
            "K": 0
        },
        "output": 6
    }, {
        "input": {
            "N": 2,
            "L": 3,
            "K": 1
        },
        "output": 2
    }, {
        "input": {
            "N": 37,
            "L": 50,
            "K": 8
        },
        "output": 32125759
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
