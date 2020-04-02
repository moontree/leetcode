"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 <=x < 10^n.

Example:
Given n = 2, return 91.
(The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""


def count_numbers_with_unique_digits(n):
    """
    :type n: int
    :rtype: int
    """

    permute = [362880, 362880, 181440, 60480, 15120, 3024, 504, 72, 9, 1]
    res = 1
    for i in xrange(1, min(n + 1, 11)):
        res += 9 * permute[-i]
    return res


print count_numbers_with_unique_digits(1)
print count_numbers_with_unique_digits(2)
print count_numbers_with_unique_digits(3)
print count_numbers_with_unique_digits(4)
print count_numbers_with_unique_digits(5)
print count_numbers_with_unique_digits(6)
print count_numbers_with_unique_digits(7)
print count_numbers_with_unique_digits(8)
print count_numbers_with_unique_digits(9)
print count_numbers_with_unique_digits(10)
print count_numbers_with_unique_digits(11)
print count_numbers_with_unique_digits(12)
