"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty,
and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S,
consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.



Example 1:

Input:
    "(()())(())"
Output:
    "()()()"
Explanation:
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input:
    "(()())(())(()(()))"
Output:
    "()()()()(())"
Explanation:
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input:
    "()()"
Output:
    ""
Explanation:
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".

Note:

    S.length <= 10000
    S[i] is "(" or ")"
    S is a valid parentheses string
"""


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res, tmp = "", ""
        count = 0
        for c in S:
            tmp += c
            if c == '(':
                count += 1
            else:
                count -= 1
                if count == 0:
                    res += tmp[1:-1]
                    tmp = ''
        return res


examples = [
    {
        "input": {
            "S": "(()())(())",
        },
        "output": "()()()"
    }, {
        "input": {
            "S": "(()())(())(()(()))",
        },
        "output": "()()()()(())"
    }, {
        "input": {
            "S": "()()",
        },
        "output": ""
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
