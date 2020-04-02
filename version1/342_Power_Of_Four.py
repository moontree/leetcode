"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

"""


def is_power_of_four(num):
    """
    :type num: int
    :rtype: bool
    """
    res = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576,
           4194304, 16777216, 67108864, 268435456, 1073741824]
    return num in res


print is_power_of_four(1)
