"""
Find the length of the longest substring T of a given string
(consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""


def longest_substring(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    start = [s]
    while True:
        new_break = False
        parts = []
        for ss in start:
            counts = {}
            for c in ss:
                counts[c] = counts.get(c, 0) + 1
            l = 0
            records = {}
            cur = 0
            while cur < len(ss):
                c = ss[cur]
                records[c] = records.get(c, 0) + 1
                if counts[c] < k:
                    if l < cur - k + 1:
                        parts.append(s[l: cur])
                        new_break = True
                    for key in records:
                        counts[key] -= records[key]
                    records = {}
                    l = cur + 1
                cur += 1
            if l < cur - k + 1:
                parts.append(ss[l: cur])
        start = parts
        if not new_break:
            break
    if not start:
        return 0
    return max(len(p) for p in start)


examples = [
    {
        "s": "aaabb",
        "k": 3,
        "res": 3
    }, {
        "s": "ababbc",
        "k": 2,
        "res": 5
    }, {
        "s": "bbaaacbd",
        "k": 3,
        "res": 5
    }, {
        "s": "",
        "k": 3,
        "res": 5
    }
]


for example in examples:
    print longest_substring(example["s"], example["k"])