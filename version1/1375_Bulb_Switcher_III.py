"""
=========================
Project -> File: leetcode -> 1375_Bulb_Switcher_III.py
Author: zhangchao
=========================
There is a room with n bulbs, numbered from 1 to n,
arranged in a row from left to right.
Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb.
A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.

Example 1:

Input:
    light = [2,1,3,5,4]
Output:
    3
Explanation:
    All bulbs turned on, are blue at the moment 1, 2 and 4.

Example 2:

Input:
    light = [3,2,4,1,5]
Output:
    2
Explanation:
    All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Example 3:

Input:
    light = [4,1,2,3]
Output:
    1
Explanation:
    All bulbs turned on, are blue at the moment 3 (index-0).
    Bulb 4th changes to blue at the moment 3.

Example 4:

Input:
    light = [2,1,4,3,6,5]
Output:
    3

Example 5:

Input:
    light = [1,2,3,4,5,6]
Output:
    6


Constraints:

    n == light.length
    1 <= n <= 5 * 10^4
    light is a permutation of  [1, 2, ..., n]
"""


class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        n, res = len(light), 0
        status = [0 for _ in range(n)]
        s = 0
        for i, v in enumerate(light):
            status[v - 1] = 1
            s += status[i]
            if v - 1 < i:
                s += 1
            if s == i + 1:
                res += 1
        return res


examples = [
    {
        "input": {
            "light": [2, 1, 3, 5, 4],
        },
        "output": 3
    }, {
        "input": {
            "light": [3, 2, 4, 1, 5],
        },
        "output": 2
    }, {
        "input": {
            "light": [4, 1, 2, 3],
        },
        "output": 1
    }, {
        "input": {
            "light": [2, 1, 4, 3, 6, 5],
        },
        "output": 3
    }, {
        "input": {
            "light": [1, 2, 3, 4, 5, 6],
        },
        "output": 6
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
