"""
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid.
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input:
    "()"
Output:
    True

Example 2:
Input:
    "(*)"
Output:
    True

Example 3:
Input:
    "(*))"
Output:
    True

Note:
    The string size will be in the range [1, 100].
"""


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r, v, q = 0, 0, 0, []
        for c in s:
            if c == '(':
                q.append(c)
            elif c == ')':
                tmp = []
                while q and q[-1] == '*':
                    tmp.append(q.pop())
                if not q:
                    if not tmp:
                        return False
                    tmp.pop()
                else:
                    q.pop()
                q += tmp
            else:
                q.append(c)

        qq = []
        for c in q:
            if c == '(':
                qq.append(c)
            else:
                if qq:
                    qq.pop()
        if len(qq):
            return False
        return True


examples = [
    {
        "input": {
            "s": "()",
        },
        "output": True
    }, {
        "input": {
            "s": "(*)",
        },
        "output": True
    }, {
        "input": {
            "s": "(*))",
        },
        "output": True
    }, {
        "input": {
            "s": "(*)(",
        },
        "output": False
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
