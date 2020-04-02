"""
=========================
Project -> File: leetcode -> 1347_Minimum_Number_of_Steps_to_Make_Two_Strings_Anagram.py
Author: zhangchao
=========================
Given two equal-size strings s and t.
In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


Example 1:

Input:
    s = "bab", t = "aba"
Output:
    1
Explanation:
    Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:

Input:
    s = "leetcode", t = "practice"
Output:
    5
Explanation:
    Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:

Input:
    s = "anagram", t = "mangaar"
Output:
    0
Explanation:
    "anagram" and "mangaar" are anagrams.

Example 4:

Input:
    s = "xxyyzz", t = "xxyyzz"
Output:
    0

Example 5:

Input:
    s = "friend", t = "family"
Output:
    4


Constraints:

    1 <= s.length <= 50000
    s.length == t.length
    s and t contain lower-case English letters only.
"""


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cs, ct = {}, {}
        for i in range(len(s)):
            cs[s[i]] = cs.get(s[i], 0) + 1
            ct[t[i]] = ct.get(t[i], 0) + 1
        res = 0
        for k in cs:
            res += abs(cs[k] - ct.get(k, 0))
        for k in ct:
            if k not in cs:
                res += ct[k]
        return res / 2


examples = [
    {
        "input": {
            "s": "bab",
            "t": "aba"
        },
        "output": 1
    }, {
        "input": {
            "s": "leetcode",
            "t": "practice"
        },
        "output": 5
    }, {
        "input": {
            "s": "anagram",
            "t": "mangaar"
        },
        "output": 0
    }, {
        "input": {
            "s": "xxyyzz",
            "t": "xxyyzz"
        },
        "output": 0
    }, {
        "input": {
            "s": "friend",
            "t": "family"
        },
        "output": 4
    },
]

import time

if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
