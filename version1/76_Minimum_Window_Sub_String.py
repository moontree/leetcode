"""
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
"""


def min_window(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    missing = len(t)
    # need, missing = collections.Counter(t), len(t)
    l = 0
    start, end = 0, 0
    for r in range(len(s)):
        c = s[r]
        missing -= need.get(c, 0) > 0
        need[c] = need.get(c, 0) - 1
        if not missing:
            while l <= r and need[s[l]] < 0:
                need[s[l]] = need.get(s[l], 0) + 1
                l += 1
            if not end or r + 1 - l <= end - start:
                start, end = l, r + 1
    return s[start: end]


examples = [
    {
        "s": "aabbafaewf",
        "t": "ae",
        "res": "ae"
    }, {
        "s": "bababaa",
        "t": "aa",
        "res": "aa"
    }, {
        "s": "acb",
        "t": "a",
        "res": "a"
    }, {
        "s": "cabefgecdaecf",
        "t": "cae",
        "res": "aec"
    },
]


for example in examples:
    print min_window(example["s"], example["t"])
