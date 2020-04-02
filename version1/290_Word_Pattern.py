"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


def word_pattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    words = str.split(" ")
    return len(pattern) == len(words) and \
           len(set(zip(words, pattern))) == len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))


examples = [
    {
        "pattern": "abba",
        "str": "dog cat cat dog",
        "res": True
    }, {
        "pattern": "abba",
        "str": "dog cat cat fish",
        "res": False
    }, {
        "pattern": "aaaa",
        "str": "dog cat cat fish",
        "res": False
    }, {
        "pattern": "abba",
        "str": "dog dog dog dog",
        "res": False
    }
]


for example in examples:
    print word_pattern(example["pattern"], example["str"])
