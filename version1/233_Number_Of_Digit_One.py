"""
Given an integer n, count the total number of digit 1
 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""


def count_digit_one(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    digits = []
    rest = []
    while n:
        digits.append(n % 10)
        n = n / 10
        rest.append(n)
    c = 0
    pre_num = ""
    res = []
    for i in range(len(digits)):
        d, r = digits[i], rest[i]
        added = 0
        if d == 1:
            added = int(str(r) + str(pre_num)) + 1
        elif d > 1:
            added = (10 ** c) * (r + 1)
        else:
            added = (10 ** c) * r
        res.append(added)
        c += 1
        pre_num = str(d) + pre_num
    return sum(res)


# print count_digit_one(13)
# print count_digit_one(111)
# print count_digit_one(123)
# print count_digit_one(1314)
# print count_digit_one(39)
# print count_digit_one(9)
print count_digit_one(123)

