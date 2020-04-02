"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    a = 1
    b = 1
    for i in range(2, n + 1):
        b, a= a + b, b
    return b


print climb_stairs(5)
