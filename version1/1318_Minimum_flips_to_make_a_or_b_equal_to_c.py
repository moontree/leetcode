"""
Given 3 positives numbers a, b and c.
Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.


Example 1:


Input:
    a = 2, b = 6, c = 5
Output:
    3
Explanation:
    After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

Example 2:

Input:
    a = 4, b = 2, c = 7
Output:
    1

Example 3:

Input:
    a = 1, b = 2, c = 3
Output:
    0


Constraints:

    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9
"""


class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        while a or b or c:
            ta, tb, tc = a % 2, b % 2, c % 2
            if (ta | tb) != tc:
                if tc == 0:
                    res += ta + tb
                else:
                    res += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return res


examples = [
    {
        "input": {
            "a": 2,
            "b": 6,
            "c": 5
        },
        "output": 3
    }, {
        "input": {
            "a": 4,
            "b": 2,
            "c": 7
        },
        "output": 1
    }, {
        "input": {
            "a": 1,
            "b": 2,
            "c": 3
        },
        "output": 0
    }, {
        "input": {
            "a": 8,
            "b": 3,
            "c": 5
        },
        "output": 3
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
