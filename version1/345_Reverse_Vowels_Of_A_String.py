"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""


def reverse_vowels(s):
    """
    :type s: str
    :rtype: str
    """
    r = list(s)
    i, j = 0, len(r) - 1
    vowels = 'aeiouAEIOU'
    while i < j:
        while i < j and r[i] not in vowels:
            i += 1
        while j > i and r[j] not in vowels:
            j -= 1
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)


examples = [
    {
        "s": "hello",
        "res": "holle"
    }, {
        "s": "leetcode",
        "res": "leotcede"
    }
]


for example in examples:
    print reverse_vowels(example["s"])
