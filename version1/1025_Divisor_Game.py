"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.
On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game,
 assuming both players play optimally.



Example 1:

Input:
    2
Output:
    true
Explanation:
    Alice chooses 1, and Bob has no more moves.

Example 2:

Input:
    3
Output:
    false
Explanation:
    Alice chooses 1, Bob chooses 1, and Alice has no more moves.

Note:

    1 <= N <= 1000
"""


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        cache = {
            1: False,
            2: True,
            3: False
        }

        def helper(n):
            if n not in cache:
                for i in range(1, n / 2 + 1):
                    if n % i == 0:
                        v = n - i
                        if v not in cache:
                            cache[v] = helper(v)
                        if not cache[v]:
                            cache[n] = True
                            return True
                cache[n] = False
            return cache[n]

        return helper(N)


examples = [
    {
        "input": {
            "N": 2,
        },
        "output": True
    },  {
        "input": {
            "N": 3,
        },
        "output": False
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
