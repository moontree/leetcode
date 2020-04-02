"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee a win.
"""
import math
# 0, 1, 2, 3, ..., n
# 0, 1, 2, .., k - 1, [k], k + 1, ..., n


def get_money_amount(n):
    """
    :type n: int
    :rtype: int
    """
    # costs: [i, j + 1]
    costs = [[-1 for _ in xrange(n + 1)] for _ in xrange(n + 1)]
    for i in xrange(n + 1):
        for j in xrange(n + 1):
            if j < i + 1:
                costs[i][j] = 0
            elif j == i + 1:
                costs[i][j] = i
            elif j == i + 2:
                costs[i][j] = i + 1
    def dp(s, e):
        if costs[s][e] > -1:
            return costs[s][e]
        ret = float("inf")
        for i in xrange(s + 1, e):
            tmp = max(dp(s, i - 1), dp(i + 1, e)) + i
            ret = min(ret, tmp)
        costs[s][e] = ret
        return ret
    val = dp(1, n)
    return val


print get_money_amount(20)
