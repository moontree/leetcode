"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.
"""


def my_sqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 2:
        return x
    else:
        l = 0
        r = x
        while l <= r:
            m = (l + r) / 2
            tmp = m * m
            if tmp == x:
                return m
            elif tmp < x:
                l = m + 1
            else:
                r = m - 1
    return l - 1


print my_sqrt(2)
print my_sqrt(4)
print my_sqrt(6)
print my_sqrt(9)
