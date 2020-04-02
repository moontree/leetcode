"""
Given a balanced parentheses string S,
compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input:
    "()"
Output:
    1

Example 2:

Input:
    "(())"
Output:
    2

Example 3:

Input:
    "()()"
Output:
    2

Example 4:

Input:
    "(()(()))"
Output:
    6


Note:

    S is a balanced parentheses string, containing only ( and ).
    2 <= S.length <= 50

"""


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        scores = []
        # q = []
        for c in S:
            if c == '(':
                scores.append(0)
                # q.append(c)
            else:
                # q.pop()
                score = 0
                while scores and scores[-1] != 0:
                    score += scores.pop()
                scores[-1] = score * 2 or 1
        return sum(scores)


examples = [
    {
        "input": {
            "S": "()",
        },
        "output": 1
    }, {
        "input": {
            "S": "(())",
        },
        "output": 2
    }, {
        "input": {
            "S": "()()",
        },
        "output": 2
    }, {
        "input": {
            "S": "(()(()))",
        },
        "output": 6
    }, {
        "input": {
            "S": "(()(()))()(())",
        },
        "output": 9
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']
