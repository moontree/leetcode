"""
=========================
Project -> File: leetcode -> 1328_Break_a_Palindrome.py
Author: zhangchao
=========================
Given a palindromic string palindrome,
replace exactly one character by any lowercase English letter
so that the string becomes the lexicographically smallest possible string
that isn't a palindrome.

After doing so, return the final string.
If there is no way to do so, return the empty string.



Example 1:

Input:
    palindrome = "abccba"
Output:
    "aaccba"

Example 2:

Input:
    palindrome = "a"
Output:
    ""

Constraints:
    1 <= palindrome.length <= 1000
    palindrome consists of only lowercase English letters.
"""


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ''
        l, r = 0, len(palindrome) - 1
        while l < r:
            if palindrome[l] != 'a':
                return palindrome[:l] + 'a' + palindrome[l + 1:]
            else:
                l += 1
                r -= 1
        return palindrome[:-1] + 'b'


examples = [
    {
        "input": {
            "palindrome": "abccba",
        },
        "output": "aaccba"
    }, {
        "input": {
            "palindrome": "a",
        },
        "output": ""
    }, {
        "input": {
            "palindrome": "aa"
        },
        "output": "ab"
    }, {
        "input": {
            "palindrome": "aba"
        },
        "output": "abb"
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
