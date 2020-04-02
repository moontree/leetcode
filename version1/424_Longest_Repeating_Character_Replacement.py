"""
Given a string that consists of only uppercase English letters,
 you can replace any letter in the string with another letter at most k times.
  Find the length of a longest substring containing all repeating letters
   you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
import collections


def character_replacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    res = lo = 0
    counts = collections.Counter()
    for hi in range(len(s)):
        counts[s[hi]] += 1
        print counts.most_common(1)
        max_char_n = counts.most_common(1)[0][1]
        # print max_char_n
        while (hi - lo - max_char_n + 1 > k):
            counts[s[lo]] -= 1
            lo += 1
        res = max(res, hi - lo + 1)
    return res
    # res = 0
    # chars = set(s)
    # for c in chars:
    #     start, end, rest = 0, 0, k
    #     while end < len(s):
    #         if s[end] != c:
    #             rest -= 1
    #         end += 1
    #         while rest < 0:
    #             if s[start] != c:
    #                 rest += 1
    #             start += 1
    #         l = end - start
    #         res = max(l, res)
    # return res


examples = [
    {
        "input": {
            "s": "ABAB",
            "k": 2
        },
        "output": 4
    }, {
        "input": {
            "s": "AABABBA",
            "k": 2
        },
        "output": 5
    }, {
        "input": {
            "s": "ABABBA",
            "k": 1
        },
        "output": 4
    }, {
        "input": {
            "s": "AAABABBBBBAABB",
            "k": 2
        },
        "output": 4
    }, {
        "input": {
            "s": "AABA",
            "k": 0
        },
        "output": 4
    }
]


for example in examples:
    print "---"
    print character_replacement(**example["input"])
