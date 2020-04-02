"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz",
so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p.
Your job is to find out how many unique non-empty substrings of p are present in s.
In particular, your input is the string p
and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""


def find_substring_in_wrapround_string(p):
    """
    :type p: str
    :rtype: int
    """
    res = {c: 1 for c in p}
    l = 1
    for i in xrange(len(p) - 1):
        prev, cur = p[i], p[i + 1]
        l = l + 1 if (ord(cur) - ord(prev)) % 26 == 1 else 1
        res[cur] = max(res[cur], l)
    return sum(res.values())

    # s = list("abcdefghijklmnopqrstuvwxyz")
    # records = {}
    # cur = ""
    # for c in p:
    #     idx = ord(c) - ord("a")
    #     if not cur or cur[-1] == s[idx - 1]:
    #         cur += c
    #     else:
    #         if len(cur) > records.get(cur[0], 0):
    #             for i, cc in enumerate(cur[:26]):
    #                 if records.get(cc, 0) < len(cur) - i:
    #                     records[cc] = len(cur) - i
    #         cur = c
    # for i, cc in enumerate(cur[:26]):
    #     if records.get(cc, 0) < len(cur) - i:
    #         records[cc] = len(cur) - i
    # return sum(records.values())


examples = [
    {
        "p": "a",
        "res": 1
    }, {
        "p": "cac",
        "res": 2
    }, {
        "p": "zab",
        "res": 6
    }, {
        "p": "zabzbcd",
        "res": 11
    }
]


for example in examples:
    print find_substring_in_wrapround_string(example["p"])
