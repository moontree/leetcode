"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"
"""


def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    l, r = 0, 0
    for i in range(len(s)):
        tmp = find_by_mid(s, i, i)
        if tmp[1] - tmp[0] > r - l:
            [l, r] = tmp
    for i in range(len(s) - 1):
        tmp = find_by_mid(s, i, i + 1)
        if tmp[1] - tmp[0] > r - l:
            [l, r] = tmp
    return s[l + 1: r]


def find_by_mid(s, l, r):
    while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
    return l, r


examples = [
    {
        "s": "cbbd",
        "res": "bb",
    }, {
        "s": "abaca",
        "res": "aba",
    }, {
        "s": "ababacefeca",
        "res": "acefeca",
    },
]


for example in examples:
    print longest_palindrome(example["s"])
