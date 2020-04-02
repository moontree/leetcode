"""
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places,
and will cover the original existing characters.

Given a string consists of lower English letters only,
your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input:
    "aaabbb"
Output:
    2
Explanation:
    Print "aaa" first and then print "bbb".
Example 2:
Input:
    "aba"
Output:
    2
Explanation:
    Print "aaa" first and then print "b" from the second place of the string,
    which will cover the existing character 'a'.

Hint:
    Length of the given string will not exceed 100.
"""


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}

        def helper(i, j):
            """
            d[i][j] = min(d[i][k] + d[k + 1][j])
            :param i:
            :param j:
            :return:
            """
            if i > j:
                return 0
            if (i, j) not in cache:
                ans = 1 + helper(i + 1, j)
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        ans = min(ans, helper(i, k - 1) + helper(k + 1, j))
                cache[(i, j)] = ans
            return cache[(i, j)]
        res = helper(0, len(s) - 1)
        # print(cache)
        return res


examples = [
    {
        "input": {
            "s": "aaabbb",
        },
        "output": 2
    }, {
        "input": {
            "s": "aba",
        },
        "output": 2
    }, {
        "input": {
            "s": "ababc",
        },
        "output": 4
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
