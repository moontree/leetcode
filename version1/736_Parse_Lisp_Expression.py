"""
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable.

Expressions always evaluate to a single integer.

(An integer could be positive or negative.)

A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr),
where let is always the string "let",
then there are 1 or more pairs of alternating variables and expressions,
meaning that the first variable v1 is assigned the value of the expression e1,
the second variable v2 is assigned the value of the expression e2,
and so on sequentially; and then the value of this let-expression is the value of the expression expr.

An add-expression takes the form (add e1 e2) where add is always the string "add",
there are always two expressions e1, e2,
and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.

A mult-expression takes the form (mult e1 e2) where mult is always the string "mult",
there are always two expressions e1, e2,
and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.

For the purposes of this question,
we will use a smaller subset of variable names.
A variable starts with a lowercase letter,
then zero or more lowercase letters or digits.
Additionally for your convenience,
the names "add", "let", or "mult" are protected and will never be used as variable names.

Finally, there is the concept of scope.
When an expression of a variable name is evaluated,
within the context of that evaluation,
the innermost scope (in terms of parentheses) is checked first for the value of that variable,
and then outer scopes are checked sequentially.
It is guaranteed that every expression is legal.
Please see the examples for more details on scope.

Evaluation Examples:
Input:
    (add 1 2)
Output:
    3

Input:
    (mult 3 (add 2 3))
Output:
    15

Input:
    (let x 2 (mult x 5))
Output:
    10

Input:
    (let x 2 (mult x (let x 3 y 4 (add x y))))
Output:
    14
Explanation:
    In the expression (add x y), when checking for the value of the variable x,
    we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
    Since x = 3 is found first, the value of x is 3.

Input:
    (let x 3 x 2 x)
Output:
    2
Explanation:
    Assignment in let statements is processed sequentially.

Input:
    (let x 1 y 2 x (add x y) (add x y))
Output:
    5
Explanation:
    The first (add x y) evaluates as 3, and is assigned to x.
    The second (add x y) evaluates as 3+2 = 5.

Input:
    (let x 2 (add (let x 3 (let x 4 x)) x))
Output:
    6
Explanation:
    Even though (let x 4 x) has a deeper scope, it is outside the context
    of the final x in the add-expression.  That final x will equal 2.

Input:
    (let a1 3 b2 (add a1 1) b2)
Output:
    4
Explanation:
    Variable names can contain digits after the first character.
"""


class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        contexts = []

        def run(ss):
            if isinstance(ss, list):
                return parse(ss)
            else:
                if ss.isdigit() or (ss[0] == '-' and ss[1:].isdigit()):
                    return int(ss)
                else:
                    for context in contexts[::-1]:
                        if ss in context:
                            return context[ss]

        def parse(ss):
            operation = ss[0]
            if operation == 'let':
                contexts.append({})
                for i in range(1, len(ss) - 1, 2):
                    contexts[-1][ss[i]] = run(ss[i + 1])
                v = run(ss[-1])
                contexts.pop()
                return v
            elif operation == 'add':
                v2, v1 = run(ss[2]), run(ss[1])
                return v1 + v2
            elif operation == 'mult':
                v2, v1 = run(ss[2]), run(ss[1])
                return v1 * v2

        q = []
        tmp = ''
        for c in expression:
            if c == '(':
                if tmp:
                    q.append(tmp)
                tmp = ''
                q.append(c)
            elif c == ' ':
                if tmp:
                    q.append(tmp)
                tmp = ''
            elif c == ')':
                if tmp:
                    q.append(tmp)
                tmp = ''
                s = []
                while q[-1] != '(':
                    s.append(q.pop())
                q.pop()
                q.append(s[::-1])
            else:
                tmp += c
        # print expression
        # print q[0]
        res = parse(q[0])
        # print res
        return res

examples = [
    {
        "input": {
            "expression": "(add 1 2)"
        },
        "output": 3
    }, {
        "input": {
            "expression": "(mult 3 (add 2 3))"
        },
        "output": 15
    }, {
        "input": {
            "expression": "(let x 2 (mult x 5))"
        },
        "output": 10
    }, {
        "input": {
            "expression": "(let x 2 (mult x (let x 3 y 4 (add x y))))"
        },
        "output": 14
    }, {
        "input": {
            "expression": "(let x 3 x 2 x)"
        },
        "output": 2
    }, {
        "input": {
            "expression": "(let x 1 y 2 x (add x y) (add x y))"
        },
        "output": 5
    }, {
        "input": {
            "expression": "(let x 2 (add (let x 3 (let x 4 x)) x))"
        },
        "output": 6
    }, {
        "input": {
            "expression": "(let a1 3 b2 (add a1 1) b2)"
        },
        "output": 4
    }, {
        "input": {
            "expression": "(let x (add 12 -7) (mult x x))"
        },
        "output": 25
    },
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']