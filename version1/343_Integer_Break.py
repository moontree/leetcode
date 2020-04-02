"""
Given a positive integer n,
break it into the sum of at least two positive integers
 and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1);
given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""

"""
if n = 2k:
k * k >= 2k  --> k >= 2, n >= 4
if n == 2k + 1:
k * k + k >= 2k + 1  --> k >= 2, n >=5

if n >= 4, should split

6 = 2 + 2 + 2 = 3 + 3, 8 < 9
choose 3 as more as possible
"""


def integer_break(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n
    return product


print integer_break(3)
print integer_break(10)
