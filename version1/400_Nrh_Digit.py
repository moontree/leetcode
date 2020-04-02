"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
import math


def find_nth_digit(n):
    """
    :type n: int
    :rtype: int
    """
    bits = 1
    pre = 0
    cur = 9
    while n > cur * bits:
        n -= cur * bits
        pre += cur
        bits += 1
        cur = cur * 10
    # print n
    base = 10 ** (bits - 1) - 1
    offset = n / bits
    # print base, offset, n % bits
    if n % bits == 0:
        return (base + offset) % 10
    else:
        num = base + offset + 1
        left = n % bits
        i = 0
        while i < bits - left:
            num = num / 10
            i += 1
        return num % 10

for i in xrange(10000, 10001):
    print find_nth_digit(i)
