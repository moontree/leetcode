"""
A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S with only uppercases, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.



Example 1:

Input:
    "ABC"
Output:
    10
Explanation:
    All possible substrings are: "A","B","C","AB","BC" and "ABC".
    Evey substring is composed with only unique letters.
    Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

Input:
    "ABA"
Output:
    8
Explanation:
    The same as example 1, except uni("ABA") = 1.


Note: 0 <= S.length <= 10000.
"""


class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        cache = {}
        for i, c in enumerate(S):
            if c not in cache:
                cache[c] = [-1]
            cache[c].append(i)
        res = 0
        for c in cache:
            cache[c].append(len(S))
            for i in range(1, len(cache[c]) - 1):
                l, cur, r = cache[c][i - 1: i + 2]
                res += (cur - l) * (r - cur)
        return res % (10 ** 9 + 7)


examples = [
    {
        "input": {
            "S": "ABC"
        },
        "output": 10
    }, {
        "input": {
            "S": "ABA"
        },
        "output": 8
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
