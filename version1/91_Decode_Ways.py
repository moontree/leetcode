"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""


def is_valid_1(s):
    if len(s) == 1 and s != '0':
        return True
    return False


def is_valid_2(s):
    if len(s) != 2:
        return False
    if s[0] == '1' or (s[0] == '2' and s[1] < '7'):
        return True
    return False


def num_decodings(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0 or s[0] == "0":
        return 0
    if len(s) == 1:
        return 1
    f1 = 1
    f2 = 1
    res = 0
    for i in range(1, len(s)):
        if is_valid_1(s[i]):
            res += f1
        if is_valid_2(s[i - 1:i + 1]):
            res += f2
        f2, f1 = f1, res
        f1 = res
        res = 0
    return f1


examples = [
    {
        "s": "12",
        "nums": 2
    }, {
        "s": "10",
        "nums": 1
    }, {
        "s": "00",
        "nums": 0
    }, {
        "s": "31",
        "nums": 1
    }, {
        "s": "26",
        "nums": 2
    }, {
        "s": "142",
        "nums": 2
    }, {
        "s": "230",
        "nums": 0
    }, {
        "s": "101",
        "nums": 1
    }
]


for example in examples:
    print num_decodings(example["s"])
