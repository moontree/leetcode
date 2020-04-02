"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

solution:
in fact number of 5 as factor
"""


def trailing_zeroes(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n:
        count += n / 5
        n = n / 5
    return count
