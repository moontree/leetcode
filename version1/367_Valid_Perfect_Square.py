"""
Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""


def is_perfect_square_bisect(num):
    """
    :type num: int
    :rtype: bool
    """
    s, e = 0, num + 1
    while s < e:
        mid = (e - s) / 2 + s
        val = mid * mid
        if val == num:
            return True
        elif val < num:
            s = mid + 1
        else:
            e = mid
    return False


def is_perfect_square(num):
    # 1 + 3 + 5 + ... + (2k - 1) = k * k
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


print is_perfect_square(4)
print is_perfect_square(13)
print is_perfect_square(100)
print is_perfect_square(0)
print is_perfect_square(1)