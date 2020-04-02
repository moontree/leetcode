"""
=========================
Project -> File: leetcode -> 1304_Find_N_Unique_Integers_Sum_up_to_Zero.py
Author: zhangchao
=========================
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input:
    n = 5
Output:
    [-7,-1,1,3,4]
Explanation:
    These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input:
    n = 3
Output:
    [-1,0,1]

Example 3:

Input:
    n = 1
Output:
    [0]


Constraints:
    1 <= n <= 1000
"""


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        p = n / 2
        res = []
        for i in range(1, p + 1):
            res.extend([i, -i])
        if n % 2 == 1:
            res.append(0)
        return res


examples = [
    {
        "input": {
            "n": 1,
        },
        "output": [0]
    }, {
        "input": {
            "n": 3,
        },
        "output": [-1, 0, 1]
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
