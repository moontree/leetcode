"""
Given a string,
find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""


def first_uniq_char(s):
    """
    :type s: str
    :rtype: int
    """
    records = {}
    counts = {}
    for i, c in enumerate(s):
        records[c] = i
        counts[c] = counts.get(c, 0) + 1
    res = len(s)
    for key in records:
        if counts[key] == 1 and res > records[key]:
            res = records[key]
    if res == len(s):
        return -1
    else:
        return res


examples = [
    {
        "s": "leetcode",
        "res": 0
    }, {
        "s": "loveleetcode",
        "res": 2
    }, {
        "s": "cc",
        "res": -1
    }, {
        "s": "cc",
        "res": -1
    }
]


for example in examples:
    print "-----"
    print first_uniq_char(example["s"])
