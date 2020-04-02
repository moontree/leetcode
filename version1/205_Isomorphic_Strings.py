"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


def is_isomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    n = len(s)
    s_to_t_map = {}
    t_to_s_map = {}
    for i in range(n):
        c = s_to_t_map.get(s[i])
        if c is None:
            s_to_t_map[s[i]] = t[i]
        else:
            if c != t[i]:
                return False
        cc = t_to_s_map.get(t[i])
        if cc is None:
            t_to_s_map[t[i]] = s[i]
        else:
            if cc != s[i]:
                return False
    return True


examples = [
    {
        "s": "egg",
        "t": "add",
        "res": True
    }, {
        "s": "foo",
        "t": "bar",
        "res": False
    }, {
        "s": "paper",
        "t": "title",
        "res": True
    }, {
        "s": "ab",
        "t": "aa",
        "res": False
    }
]


for example in examples:
    print is_isomorphic(example["s"], example["t"])
