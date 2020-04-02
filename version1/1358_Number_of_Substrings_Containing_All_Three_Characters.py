"""
=========================
Project -> File: leetcode -> 1358_Number_of_Substrings_Containing_All_Three_Characters.py
Author: zhangchao
=========================
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input:
    s = "abcabc"
Output:
    10
Explanation:
    The substrings containing at least one occurrence of the characters a, b and c are
    "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:

Input:
    s = "aaacb"
Output:
    3
Explanation:
    The substrings containing at least one occurrence of the characters a, b and c
    are "aaacb", "aacb" and "acb".

Example 3:

Input:
    s = "abc"
Output:
    1

Constraints:

    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.
"""


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        res, l = 0, 0
        for r, c in enumerate(s):
            cache[c] = cache.get(c, 0) + 1
            if len(cache) < 3:
                continue
            else:
                while cache[s[l]] > 1:
                    cache[s[l]] -= 1
                    l += 1
                res += l + 1

        return res


examples = [
    {
        "input": {
            "s": "abcabc",
        },
        "output": 10
    }, {
        "input": {
            "s": "aaacb",
        },
        "output": 3
    }, {
        "input": {
            "s": "abc",
        },
        "output": 1
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
