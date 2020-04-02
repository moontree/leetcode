"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


def add_binary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    vals = {"0": 0, "1": 1}
    c = 0
    la = len(a)
    lb = len(b)
    if la < lb:
        a = '0' * (lb - la) + a
    else:
        b = '0' * (la - lb) + b
    print a, b
    res = ""
    for i in reversed(range(len(a))):
        tmp = vals[a[i]] + vals[b[i]] + c
        c = tmp / 2
        res += str(tmp % 2)
    if c > 0:
        res += str(1)
    return res[::-1]


print add_binary("1011", "1010")
