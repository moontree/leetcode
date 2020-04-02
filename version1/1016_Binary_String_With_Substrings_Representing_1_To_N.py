"""
Given a binary string S (a string consisting only of '0' and '1's)
and a positive integer N, return true if and only if for every integer X from 1 to N,
the binary representation of X is a substring of S.



Example 1:

Input:
    S = "0110", N = 3
Output:
    true

Example 2:

Input:
    S = "0110", N = 4
Output:
    false

Note:

    1 <= S.length <= 1000
    1 <= N <= 10^9
"""


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        if N < 2:
            return '1' in S
        i = 1
        while i <= N:
            if bin(i)[2:] not in S:
                return False
            i += 1
        return True


examples = [
    {
        "input": {
            "S": "0110",
            "N": 3
        },
        "output": True
    }, {
        "input": {
            "S": "0110",
            "N": 4
        },
        "output": False
    }, {
        "input": {
            "S": "1",
            "N": 1
        },
        "output": True
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
