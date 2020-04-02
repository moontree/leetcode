"""
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears
n/4 times where n is the length of the string.

Return the minimum length of the substring
that can be replaced with any other string of the same length
to make the original string s balanced.

Return 0 if the string is already balanced.


Example 1:

Input:
    s = "QWER"
Output:
    0
Explanation:
    s is already balanced.

Example 2:

Input:
    s = "QQWE"
Output:
    1
Explanation:
    We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:

Input:
    s = "QQQW"
Output:
    2
Explanation:
    We can replace the first "QQ" to "ER".

Example 4:

Input:
    s = "QQQQ"
Output:
    3
Explanation:
    We can replace the last 3 'Q' to make s = "QWER".


Constraints:

    1 <= s.length <= 10^5
    s.length is a multiple of 4
    s contains only 'Q', 'W', 'E' and 'R'.
"""


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        for c in s:
            cache[c] = cache.get(c, 0) + 1
        p = len(s) / 4
        need = {}
        for key in cache:
            if cache[key] > p:
                need[key] = cache[key] - p
        if len(need) == 0:
            return 0
        cache = {}
        l = 0
        res = len(s)
        for i, c in enumerate(s):
            cache[c] = cache.get(c, 0) + 1
            while l < i and cache.get(s[l], 0) > need.get(s[l], 0):
                cache[s[l]] -= 1
                l += 1
            # check valid
            valid = True
            for cc in 'QWER':
                if cache.get(cc, 0) < need.get(cc, 0):
                    valid = False
                    break
            # print valid, l, i, s[l: i]
            if valid:
                res = min(res, i - l + 1)
        return res


examples = [
    {
        "input": {
            "s": "QWER",
        },
        "output": 0
    }, {
        "input": {
            "s": "QQWE",
        },
        "output": 1
    }, {
        "input": {
            "s": "QQQW",
        },
        "output": 2
    }, {
        "input": {
            "s": "QQQQ",
        },
        "output": 3
    }, {
        "input": {
            "s": "WWEQERQWQWWRWWERQWEQ",
        },
        "output": 4
    }, {
        "input": {
            "s": "WQWRQQQW",
        },
        "output": 3
    }, {
        "input": {
            "s": "WWWEQRQEWWQQQWQQQWEWEEWRRRRRWWQE",
        },
        "output": 5
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
