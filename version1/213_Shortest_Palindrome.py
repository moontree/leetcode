"""
Given a string S,
 you are allowed to convert it to a palindrome by adding characters in front of it.
  Find and return the shortest palindrome
   you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""


def shortest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    dup = s + "#" + s[::-1]
    table = [0] * len(dup)
    index = 0
    for i in range(1, len(dup)):
        if dup[index] == dup[i]:
            table[i] = table[i - 1] + 1
            index += 1
        else:
            index = table[i - 1]
            while index > 0 and dup[index] != dup[i]:
                index = table[index - 1]
            if dup[index] == dup[i]:
                table[i] = table[i - 1] + 1
                index += 1
            table[i] = index
    rest = table[-1]
    return s[rest:][::-1] + s


examples = [
    {
        "s": "abcd",
        "res": "dcbabcd"
    }, {
        "s": "aacecaaa",
        "res": "aaacecaaa"
    }
]


for example in examples:
    print shortest_palindrome(example["s"])