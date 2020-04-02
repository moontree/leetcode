"""
=========================
Project -> File: leetcode -> 761_Special_Binary_String.py
Author: zhangchao
=========================
Special binary strings are binary strings with the following two properties:

    The number of 0's is equal to the number of 1's.
    Every prefix of the binary string has at least as many 1's as 0's.
Given a special string S,
a move consists of choosing two consecutive, non-empty, special substrings of S,
and swapping them.
(Two strings are consecutive if
the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:
Input:
    S = "11011000"
Output:
    "11100100"
Explanation:
    The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
    This is the lexicographically largest string possible after some number of swaps.
Note:

    S has length at most 50.
    S is guaranteed to be a special binary string as defined above.
"""


class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """

        vt = []
        cnt, l = 0, 0
        for i, c in enumerate(S):
            if c == '1':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                vt.append('1' + self.makeLargestSpecial(S[l + 1: i]) + '0')
                l = i + 1
        vt.sort(reverse=True)
        return ''.join(vt)


examples = [
    {
        "input": {
            "S": "11011000",
        },
        "output": "11100100"
    }, {
        "input": {
            "S": "1010101100",
        },
        "output": "111001010"
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
