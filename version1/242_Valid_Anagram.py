"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""


def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    sd = {}
    td = {}
    for c in s:
        sd[c] = sd.get(c, 0) + 1
    for c in t:
        td[c] = td.get(c, 0) + 1
    for key in sd:
        if sd[key] != td.get(key, 0):
            return False
    return len(sd) == len(td)


examples = [
    {
        "s": "anagram",
        "t": "nagaram",
        "res": True,
    }, {
        "s": "rat",
        "t": "car",
        "res": False,
    }
]
