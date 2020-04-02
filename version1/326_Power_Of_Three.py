"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

"""


def is_power_of_three(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and 1162261467 % n == 0
