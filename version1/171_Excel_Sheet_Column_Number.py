"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""


def title_to_number(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    for c in s:
        res = res * 26 + ord(c) - ord('A') + 1
    return res


examples = [
    {
        "s": 'A',
        "res": 1,
    }, {
        "s": 'AA',
        "res": 27,
    }, {
        "s": 'Z',
        "res": 26,
    }, {
        "s": 'AZ',
        "res": 52,
    }, {
        "s": 'ZY',
        "res": 701,
    }
]


for example in examples:
    print title_to_number(example["s"])
