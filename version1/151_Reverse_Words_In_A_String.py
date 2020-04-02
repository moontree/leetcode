"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.
"""


def reverse_words(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split(' ')[::-1]
    res = ""
    for w in words:
        if len(w):
            res += w + " "
    return res[:-1]


examples = [
    {
        "s": "the sky is blue",
        "res": "blue is sky the"
    }, {
        "s": " ",
        "res": ""
    }
]


for example in examples:
    print reverse_words(example["s"])
