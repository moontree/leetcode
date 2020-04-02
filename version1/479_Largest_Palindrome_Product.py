"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""


def largest_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    x = [9, 99, 993, 9999, 99979, 999999, 9998017, 99999999]
    y = [1, 91, 913, 9901, 99681, 999001, 9997647, 99990001]

    return ((x[n - 1] % 1337) * (y[n - 1] % 1337)) % 1337


for i in xrange(1, 9):
    val = largest_palindrome(i)
    print val, val % 1337
