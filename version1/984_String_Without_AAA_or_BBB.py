"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.


Example 1:

Input:
    A = 1, B = 2
Output:
    "abb"
Explanation:
    "abb", "bab" and "bba" are all correct answers.

Example 2:

Input:
    A = 4, B = 1
Output:
    "aabaa"

Note:
    0 <= A <= 100
    0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == B:
            return 'ab' * A
        elif A > B:
            if B > 0:
                return 'aab' + self.strWithout3a3b(A - 2, B - 1)
            else:
                return 'a' * A
        else:
            if A > 0:
                return 'bba' + self.strWithout3a3b(A - 1, B - 2)
            else:
                return 'b' * B


examples = [
    {
        "input": {
            "A": 1,
            "B": 2
        },
        "output": "bab"
    }, {
        "input": {
            "A": 4,
            "B": 1
        },
        "output": "aabaa"
    }, {
        "input": {
            "A": 5,
            "B": 2
        },
        "output": "abaabaa"
    }, {
        "input": {
            "A": 1,
            "B": 1
        },
        "output": "ab"
    }, {
        "input": {
            "A": 1,
            "B": 3
        },
        "output": "bbab"
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
