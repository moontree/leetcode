"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
import collections


def find_anagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    if len(s) < len(p) or not s or not p:
        return []
    p_records = {}
    for c in p:
        p_records[c] = p_records.get(c, 0) + 1
    res = []
    l, r, missing = 0, 0, len(p)
    while r < len(s):
        if p_records.get(s[r]) > 0:
            missing -= 1
        p_records[s[r]] = p_records.get(s[r], 0) - 1
        if missing == 0:
            res.append(l)
        if r - l == len(p) - 1:
            p_records[s[l]] += 1
            if p_records[s[l]] > 0:
                missing += 1
            l += 1
        r += 1
    return res



    # need = collections.Counter(p)
    # res = []
    # l, r, missing = 0, 0, len(p)
    # while r < len(s):
    #     if need[s[r]] > 0:
    #         missing -= 1
    #     need[s[r]] -= 1
    #
    #     if missing == 0:
    #         res.append(l)
    #
    #     if r - l == len(p) - 1:
    #         need[s[l]] += 1
    #         if need[s[l]] > 0:
    #             missing += 1
    #         l += 1
    #
    #     r += 1
    #
    # return res


print find_anagrams("cbaebabacd", "abc")
