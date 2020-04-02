"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input:
    s = "RLRRLLRLRL"
Output:
    4
Explanation:
    s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input:
    s = "RLLLLRRRLR"
Output:
    3
Explanation:
    s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input:
    s = "LLLLRRRR"
Output:
    1
Explanation:
    s can be split into "LLLLRRRR".

Example 4:

Input:
    s = "RLRRRLLRLL"
Output:
    2
Explanation:
    s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


Constraints:

    1 <= s.length <= 1000
    s[i] = 'L' or 'R'
"""


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag, n = None, 0
        res = 0
        for c in s:
            if flag is None:
                flag = c
                n += 1
            elif flag == c:
                n += 1
            else:
                n -= 1
            if n == 0:
                res += 1
                flag, n = None, 0
        return res


examples = [
    {
        "input": {
            "s": "RLRRLLRLRL",
        },
        "output": 4
    }, {
        "input": {
            "s": "RLLLLRRRLR",
        },
        "output": 3
    }, {
        "input": {
            "s": "LLLLRRRR",
        },
        "output": 1
    }, {
        "input": {
            "s": "RLRRRLLRLL",
        },
        "output": 2
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
