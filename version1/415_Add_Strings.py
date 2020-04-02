"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


def add_strings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    b1, b2 = [int(s) for s in num1][::-1], [int(s) for s in num2][::-1]
    c = 0
    m, n = len(b1), len(b2)
    i = 0
    res = []
    while i < m and i < n:
        val = b1[i] + b2[i] + c
        c = val / 10
        res.append(val % 10)
        i += 1
    while i < m:
        val = b1[i] + c
        c = val / 10
        res.append(val % 10)
        i += 1
    while i < n:
        val = b2[i] + c
        c = val / 10
        res.append(val % 10)
        i += 1
    if c > 0:
        res.append(c)
    print res
    return "".join([str(v) for v in res[::-1]])


print add_strings("99991", "9")
