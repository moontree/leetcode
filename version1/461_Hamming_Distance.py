# --*-- coding: utf-8 --*--
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 <= x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""


def hamming_distance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    diff = x ^ y
    res = 0
    while diff:
        res += 1
        diff &= diff - 1
    return res


print hamming_distance(1, 4)