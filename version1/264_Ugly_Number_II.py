"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
 For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""


def nth_ugly_number(n):
    """
    :type n: int
    :rtype: int
    """
    n2, n3, n5 = [2], [3], [5]
    res = 1
    while n > 1:
        if n2[0] < n3[0] and n2[0] < n5[0]:
            res = n2.pop(0)
            n2.append(res * 2)
            n3.append(res * 3)
            n5.append(res * 5)
        elif n3[0] < n2[0] and n3[0] < n5[0]:
            res = n3.pop(0)
            n3.append(res * 3)
            n5.append(res * 5)
        elif n5[0] < n2[0] and n5[0] < n3[0]:
            res = n5.pop(0)
            n5.append(res * 5)
        n -= 1
    return res


print nth_ugly_number(1)
print nth_ugly_number(2)
print nth_ugly_number(3)
print nth_ugly_number(4)
print nth_ugly_number(5)
print nth_ugly_number(6)
print nth_ugly_number(7)
print nth_ugly_number(8)
print nth_ugly_number(9)
print nth_ugly_number(10)
print nth_ugly_number(11)
