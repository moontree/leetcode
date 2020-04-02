"""
Given a positive integer n,
 find the least number of perfect square numbers
  (for example, 1, 4, 9, 16, ...) which sum to n.

For example,
given n = 12, return 3 because 12 = 4 + 4 + 4;
 given n = 13, return 2 because 13 = 4 + 9.
"""
import math


def num_squares(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0, 1]
    for i in range(2, n + 1):
        min_val = i
        for j in range(1, int(math.sqrt(i)) + 1):
            rest = i - j * j
            if rest >= 0:
                if dp[rest] + 1 < min_val:
                    min_val = dp[rest] + 1
                    if min_val == 1:
                        break
        dp.append(min_val)
    return dp[-1]


print num_squares(7691)
