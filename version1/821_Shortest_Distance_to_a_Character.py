"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [n + 1 for _ in range(n)]
        for i, v in enumerate(S):
            if v == C:
                res[i] = 0
            else:
                res[i] = min(res[i - 1] + 1, res[i])
        for i in range(n)[::-1]:
            if res[i] == C or i == n - 1:
                continue
            res[i] = min(res[i], res[i + 1] + 1)
        return res


examples = [
    {
        "input": {
            "S": "loveleetcode",
            "C": 'e',
        },
        "output": [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
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
        print func(**example['input']) == example['output']