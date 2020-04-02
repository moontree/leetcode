"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


examples = [
    {
        "s": "Hello World",
        "l": 5,
    }, {
        "s": "Test ",
        "l": 4,
    }, {
        "s": " a  ",
        "l": 1
    }
]


def length_of_last_word(s):
    """
    :type s: str
    :rtype: int
    """
    l = 0
    for p in s[::-1]:
        if p == ' ':
            if l > 0:
                return l
        else:
            l += 1
    return l


for example in examples:
    print length_of_last_word(example["s"])
