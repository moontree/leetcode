"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


def convert_to_title(n):
    """
    :type n: int
    :rtype: str
    """
    chars = [chr(i).upper() for i in range(97, 123)]
    indexs = []
    while n > 0:
        n -= 1
        indexs.append(n % 26)
        n = n / 26
    res = [chars[i] for i in indexs][::-1]
    return "".join(res)


examples = [
    {
        "num": 1,
        "res": "A"
    }, {
        "num": 26,
        "res": "Z"
    }, {
        "num": 27,
        "res": "AA"
    }, {
        "num": 52,
        "res": "AZ"
    }, {
        "num": 26 * 27,
        "res": "ZZ"
    }, {
        "num": 701,
        "res": "ZY"
    }
]


for example in examples:
    print convert_to_title(example["num"])
