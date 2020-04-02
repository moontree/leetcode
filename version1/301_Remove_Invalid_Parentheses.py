"""
Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input:
    "()())()"
Output:
    ["()()()", "(())()"]

Example 2:

Input:
    "(a)())()"
Output:
    ["(a)()()", "(a())()"]

Example 3:

Input:
    ")("
Output:
    [""]
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lc, rc = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                lc += 1
            elif c == ')':
                if lc == 0:
                    rc += 1
                else:
                    lc -= 1

        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)
                # Pop for backtracking.
                expr.pop()
                # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, lc, rc, [])
        return list(result.keys())


examples = [
    {
        "input": {
            "s": "()())()",
        },
        "output": ["()()()", "(())()"]
    }, {
        "input": {
            "s": "(a)())()",
        },
        "output": ["(a)()()", "(a())()"]
    }, {
        "input": {
            "s": ")(",
        },
        "output": [""]
    }, {
        "input": {
            "s": ")()))())))",
        },
        "output": ["(())", "()()"]
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
