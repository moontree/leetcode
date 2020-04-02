"""
=========================
Project -> File: leetcode -> 1324_Print_Words_Vertically.py
Author: zhangchao
=========================
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.



Example 1:

Input:
    s = "HOW ARE YOU"
Output:
    ["HAY","ORO","WEU"]
Explanation:
    Each word is printed vertically.
    "HAY"
    "ORO"
    "WEU"

Example 2:

Input:
    s = "TO BE OR NOT TO BE"
Output:
    ["TBONTB","OEROOE","   T"]
Explanation:
    Trailing spaces is not allowed.
    "TBONTB"
    "OEROOE"
    "   T"

Example 3:

Input:
    s = "CONTEST IS COMING"
Output:
    ["CIC","OSO","N M","T I","E N","S G","T"]

Constraints:
    1 <= s.length <= 200
    s contains only upper case English letters.
    It's guaranteed that there is only one space between 2 words.
"""


class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split(' ')
        res, n = [], len(words)
        nn = max([len(word) for word in words])
        for i in range(nn):
            chars = [word[i] if i < len(word) else ' ' for word in words]
            ss = ''.join(chars)
            res.append(ss)
        return [ss.rstrip() for ss in res]


examples = [
    {
        "input": {
            "s": "HOW ARE YOU",
        },
        "output": ["HAY", "ORO", "WEU"]
    }, {
        "input": {
            "s": "TO BE OR NOT TO BE",
        },
        "output": ["TBONTB", "OEROOE", "   T"]
    }, {
        "input": {
            "s": "CONTEST IS COMING",
        },
        "output": ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]
    }
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
