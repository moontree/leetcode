"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""


def is_interleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    m, n, p = len(s1), len(s2), len(s3)
    if m + n != p:
        return False
    s1 = '.' + s1
    s2 = '.' + s2
    s3 = '.' + s3
    s = [[False for _ in range(len(s1))] for _ in range(len(s2))]
    s[0][0] = True
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] and s1[j] == s3[j]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] and s2[i] == s3[i]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = (s[i - 1][j] and s2[i] == s3[i + j]) or (s[i][j - 1] and s1[j] == s3[i + j])
    return s[-1][-1]


examples = [
    {
        "s1": "aabcc",
        "s2": "dbbca",
        "s3": "aadbbcbcac",
        "res": True
    }, {
        "s1": "aabcc",
        "s2": "dbbca",
        "s3": "aadbbbaccc",
        "res": False
    }, {
        "s1": "a",
        "s2": "b",
        "s3": "a",
        "res": False
    }
]


for example in examples:
    print is_interleave(example["s1"], example["s2"], example["s3"])
