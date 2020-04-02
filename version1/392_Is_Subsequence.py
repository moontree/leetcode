"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t.
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
 of the characters without disturbing the relative positions of the remaining characters.
  (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
and you want to check one by one to see if T has its subsequence.
In this scenario, how would you change your code?
"""


def is_subsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i, n = 0, len(s)
    if n == 0:
        return True
    for c in t:
        if s[i] == c:
            i += 1
        if i == n:
            return True
    return False


examples = [
    {
        "input": {
            "s": "abc",
            "t": "ahbgdc"
        },
        "output": True
    }, {
        "input": {
            "s": "axc",
            "t": "ahbgdc"
        },
        "output": True
    }
]


for example in examples:
    print is_subsequence(**example["input"])

## Follow up
"""
Preprocess: record positions of each char, and search of char in s which is greater than index
index = the smallest index of c 
"""