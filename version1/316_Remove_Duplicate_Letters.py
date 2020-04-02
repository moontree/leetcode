"""
Given a string which contains only lowercase letters,
 remove duplicate letters so that every letter appear once and only once.
 You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"


"""


def remove_duplicate_letters(s):
    """
    :type s: str
    :rtype: str
    """
    res = []
    records = {}
    visited = {}
    for p in s:
        records[p] = records.get(p, 0) + 1
        visited[p] = False
    for p in s:
        records[p] -= 1
        if visited[p]:
            continue
        else:
            while len(res) and p < res[-1] and records[res[-1]] != 0:
                c = res.pop()
                visited[c] = False
            res.append(p)
            visited[p] = True
    return "".join(res)


examples = [
    {
        "s": "bcabc",
        "res": "abc",
    }, {
        "s": "cbacdcbc",
        "res": "acdb",
    }, {
        "s": "abacbdare",
        "res": "acdb",
    }
]


for example in examples:
    print remove_duplicate_letters(example["s"])
