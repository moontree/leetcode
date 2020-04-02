"""
Given a string S of '(' and ')' parentheses,
we add the minimum number of parentheses ( '(' or ')',
and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string,
return the minimum number of parentheses we must add to make the resulting string valid.



Example 1:

Input:
    "())"
Output:
    1

Example 2:
Input:
    "((("
Output:
    3

Example 3:

Input:
    "()"
Output:
    0

Example 4:
Input:
    "()))(("
Output:
    4

Note:

    S.length <= 1000
    S only consists of '(' and ')' characters.
"""


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res, left = 0, 0
        for c in S:
            if left == 0:
                if c == ')':
                    res += 1
                else:
                    left += 1
            else:
                if c == '(':
                    left += 1
                else:
                    left -= 1
        res += left
        return res


examples = [
    {
        "input": {
            "S": "())",
        },
        "output": 1
    }, {
        "input": {
            "S": "(((",
        },
        "output": 3
    }, {
        "input": {
            "S": "()",
        },
        "output": 0
    },  {
        "input": {
            "S": "()))((",
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
