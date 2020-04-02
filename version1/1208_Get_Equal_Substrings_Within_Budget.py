"""
You are given two strings s and t of the same length.
You want to change s to t.
Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is,
the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t
with a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.


Example 1:

Input:
    s = "abcd", t = "bcdf", maxCost = 3
Output:
    3
Explanation:
    "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

Example 2:

Input:
    s = "abcd", t = "cdef", maxCost = 3
Output:
    1
Explanation:
    Each character in s costs 2 to change to charactor in t, so the maximum length is 1.

Example 3:

Input:
    s = "abcd", t = "acde", maxCost = 0
Output:
    1
Explanation:
    You can't make any change, so the maximum length is 1.


Constraints:
    1 <= s.length, t.length <= 10^5
    0 <= maxCost <= 10^6
    s and t only contain lower case English letters.
"""


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        diffs = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        l, r, cost, res = 0, 0, 0, 0
        for i, d in enumerate(diffs):
            cost += d
            if cost <= maxCost:
                res = max(i - l + 1, res)
            else:
                while cost > maxCost:
                    cost -= diffs[l]
                    l += 1
        return res


examples = [
    {
        "input": {
            "s": "abcd",
            "t": "bcdf",
            "maxCost": 3
        },
        "output": 3
    }, {
        "input": {
            "s": "abcd",
            "t": "cdef",
            "maxCost": 3
        },
        "output": 1
    }, {
        "input": {
            "s": "abcd",
            "t": "acde",
            "maxCost": 0
        },
        "output": 1
    }, {
        "input": {
            "s": "krrgw",
            "t": "zjxss",
            "maxCost": 19
        },
        "output": 2
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
