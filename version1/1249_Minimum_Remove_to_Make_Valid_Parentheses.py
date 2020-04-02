"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')',
 in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input:
    s = "lee(t(c)o)de)"
Output:
    "lee(t(c)o)de"
Explanation:
    "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input:
    s = "a)b(c)d"
Output:
    "ab(c)d"

Example 3:

Input:
    s = "))(("
Output:
    ""
Explanation:
    An empty string is also valid.

Example 4:

Input:
    s = "(a(b(c)d)"
Output:
    "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, q = "", []
        for c in s:
            if c == '(':
                q.append(c)
            elif c == ')':
                tmp = ''
                while q and q[-1] != '(':
                    tmp = q.pop() + tmp
                if q and q[-1] == '(':
                    q.pop()
                    tmp = '(' + tmp + ')'
                    q.append(tmp)
                else:
                    if tmp:
                        q.append(tmp)
            else:
                q.append(c)
        for c in q:
            if c == '(' or c == ')':
                pass
            else:
                res += c
        return res


examples = [
    {
        "input": {
            "s": "lee(t(c)o)de)",
        },
        "output": "lee(t(c)o)de"
    }, {
        "input": {
            "s": "a)b(c)d",
        },
        "output": "ab(c)d"
    }, {
        "input": {
            "s": "))((",
        },
        "output": ""
    }, {
        "input": {
            "s": "(a(b(c)d)",
        },
        "output": "a(b(c)d)"
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
