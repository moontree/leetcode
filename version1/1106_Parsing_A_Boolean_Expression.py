"""
Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

    "t", evaluating to True;
    "f", evaluating to False;
    "!(expr)", evaluating to the logical NOT of the inner expression expr;
    "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
    "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...


Example 1:

Input:
    expression = "!(f)"
Output:
    true

Example 2:

Input:
    expression = "|(f,t)"
Output:
    true

Example 3:

Input:
    expression = "&(t,f)"
Output:
    false

Example 4:

Input:
    expression = "|(&(t,f,t),!(t))"
Output:
    false

Constraints:

    1 <= expression.length <= 20000
    expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
    expression is a valid expression representing a boolean, as given in the description.
"""


class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        q = []
        for c in expression:
            if c == 't':
                q.append(True)
            elif c == 'f':
                q.append(False)
            else:
                if c != ')':
                    q.append(c)
                else:
                    v, orv, andv = None, False, True
                    while q and q[-1] != '(':
                        if q[-1] == ',':
                            pass
                        else:
                            v = q[-1]
                            orv |= v
                            andv &= v
                        q.pop()
                    q.pop()
                    op = q.pop()
                    if op == '!':
                        q.append(not v)
                    elif op == '&':
                        q.append(andv)
                    elif op == '|':
                        q.append(orv)
            # print c, q
        # print q
        return q[0]


examples = [
    {
        "input": {
            "expression": "!(f)",
        },
        "output": True
    }, {
        "input": {
            "expression": "|(f,t)",
        },
        "output": True
    }, {
        "input": {
            "expression": "&(t,f)",
        },
        "output": False
    }, {
        "input": {
            "expression": "|(&(t,f,t),!(t))",
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
