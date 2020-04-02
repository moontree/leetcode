"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""


def is_scramble(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    m, n = len(s1), len(s2)
    if m != n or sorted(s1) != sorted(s2):
        return False
    if n < 4 or s1 == s2:
        return True
    for mid in range(1, m):
        if is_scramble(s1[:mid], s2[:mid]) and is_scramble(s1[mid:], s2[mid:]):
            return True
        if is_scramble(s1[:mid], s2[-mid:]) and is_scramble(s1[mid:], s2[:-mid]):
            return True
    return False


examples = [
    {
        "s1": "great",
        "s2": "rgeta",
        "res": True
    }, {
        "s1": "great",
        "s2": "rgeat",
        "res": True
    }, {
        "s1": "great",
        "s2": "gater",
        "res": True
    }, {
        "s1": "abb",
        "s2": "bab",
        "res": True
    }, {
        "s1": "a",
        "s2": "b",
        "res": False
    }
]


for example in examples:
    print is_scramble(example["s1"], example["s2"])