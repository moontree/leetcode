"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
 return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""


def reverse_bits(n):
    res = 0
    for i in range(32):
        mod = n % 2
        res = res * 2 + mod
        n = n / 2
    return res


print reverse_bits(43261596)
