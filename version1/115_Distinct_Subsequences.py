"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
"""
""      t[0]     t[1]    t[2] ...
s[0]    
s[1]
s[2]
...

s[i] != t[j]:
nums[i][j] = nums[i - 1][j]
s[i] == t[j]:
nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
"""


def num_distinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    m, n = len(s), len(t)
    nums = [0 for _ in range(n + 1)]
    for i in range(1, m + 1):
        nums[0] = 1
        for j in range(1, n + 1)[::-1]:
            if s[i - 1] == t[j - 1]:
                nums[j] = nums[j - 1] + nums[j]
    return nums[-1]


examples = [
    {
        "s": "rabbbit",
        "t": "rabbit",
        "res": 3
    }, {
        "s": "ccc",
        "t": "c",
        "res": 3
    }
]


for example in examples:
    print num_distinct(example["s"], example["t"])
