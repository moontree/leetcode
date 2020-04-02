"""
Given a string s,
return the last substring of s in lexicographical order.



Example 1:

Input:
    "abab"
Output:
    "bab"
Explanation:
    The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
    The lexicographically maximum substring is "bab".

Example 2:

Input:
    "leetcode"
Output:
    "tcode"


Note:

    1 <= s.length <= 4 * 10^5
    s contains only lowercase English letters.
"""


class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

        s += '.'
        n = len(s)

        l, r, k = 0, 1, 0
        while l < n and r < n and k < n:
            if s[l + k] == s[r + k]:
                k += 1
            else:
                if s[l + k] > s[r + k]:
                    r = r + k + 1
                else:
                    l = l + k + 1
                if l == r:
                    r += 1
                k = 0
        return s[l: -1]


examples = [
    {
        "input": {
            "s": "abab",
        },
        "output": "bab"
    }, {
        "input": {
            "s": "leetcode",
        },
        "output": "tcode"
    }, {
        "input": {
            "s": "aaaaa",
        },
        "output": "aaaaa"
    }, {
        "input": {
            "s": "zrziy",
        },
        "output": "zrziy"
    }, {
        "input": {
            "s": "cacacb",
        },
        "output": "cb"
    }, {
        "input": {
            "s": "babcbd",
        },
        "output": "d"
    }, {
        "input": {
            "s": "cacbccc",
        },
        "output": "ccc"
    }, {
        "input": {
            "s": "aa",
        },
        "output": "aa"
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
