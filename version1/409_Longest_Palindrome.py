"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


def longest_palindrome(s):
    """
    :type s: str
    :rtype: int
    """
    records = {}
    for c in s:
        records[c] = records.get(c, 0) + 1
    has_odd = False
    res = 0
    for val in records.values():
        if val % 2 == 0:
            res += val
        else:
            res += val - 1
            has_odd = True
    if has_odd:
        res += 1
    return res


print longest_palindrome("abccccdd")
