"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


def reverse_string(s):
    """
    :type s: str
    :rtype: str
    """
    r = list(s)
    i, j  = 0, len(r) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1

    return "".join(r)
