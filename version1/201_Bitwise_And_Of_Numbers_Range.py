"""
Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.
For example, given the range [5, 7], you should return 4.
"""


def range_bitwise_and(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # res = m & n
    # if m == n:
    #     return res
    # rest = len(bin(n - m)) - 2
    # res = res >> rest << rest
    # return res
    i = 0
    while m != n:
        n >>= 1
        m >>= 1
        i += 1
    return m << i


examples = [
    {
        "m": 5,
        "n": 7,
        "res": 4
    }, {
        "m": 4,
        "n": 7,
        "res": 4
    }, {
        "m": 0,
        "n": 2147483647,
        "res": 0
    }, {
        "m": 6,
        "n": 7,
        "res": 6
    }, {
        "m": 57,
        "n": 63,
        "res": 56
    }
]


for example in examples:
    print range_bitwise_and(example["m"], example["n"])
