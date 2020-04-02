"""
Given an integer n.
No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution.
If there are many valid solutions you can return any of them.



Example 1:

Input:
    n = 2
Output:
    [1,1]
Explanation:
    A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.

Example 2:

Input:
    n = 11
Output:
    [2,9]

Example 3:

Input:
    n = 10000
Output:
    [1,9999]

Example 4:

Input:
    n = 69
Output:
    [1,68]

Example 5:

Input:
    n = 1010
Output:
    [11,999]


Constraints:

    2 <= n <= 10^4
"""


class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(n):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]


examples = [
    {
        "input": {
            "n": 2,
        },
        "output": [1, 1]
    }, {
        "input": {
            "n": 11,
        },
        "output": [2, 9]
    }, {
        "input": {
            "n": 10000,
        },
        "output": [1, 9999]
    }, {
        "input": {
            "n": 69,
        },
        "output": [1, 68]
    }, {
        "input": {
            "n": 1010,
        },
        "output": [11, 999]
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
