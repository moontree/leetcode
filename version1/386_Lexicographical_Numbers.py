"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
import math
import numpy as np

def lexical_order(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # if n < 10:
    #     return range(1, n + 1)
    # num = n
    # val = 1
    # res = []
    # while len(res) < n:
    #     if val <= n:
    #         res.append(val)
    #     if val * 10 <= n:
    #         val *= 10
    #     else:
    #         while val % 10 == 9:
    #             val = val / 10
    #         val += 1
    # return res

    ##  for i in range(base, n + 1) + range(n / 10 + 1, base):
    res = []
    c = len(str(n)) - 1
    base = 10 ** c
    for i in xrange(base, n + 1):
        tmp = []
        v = i
        while v % 10 == 0:
            v /= 10
            tmp.append(v)
        res += tmp[::-1]
        res.append(i)
    n = n / 10 + 1
    for i in xrange(n, base):
        tmp = []
        v = i
        while v % 10 == 0:
            v /= 10
            tmp.append(v)
        res += tmp[::-1]
        res.append(i)

    return res

print lexical_order(99)
