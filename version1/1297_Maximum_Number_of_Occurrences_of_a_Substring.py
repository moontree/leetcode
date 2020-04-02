"""
Given a string s,
return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input:
    s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output:
    2
Explanation:
    Substring "aab" has 2 ocurrences in the original string.
    It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:

Input:
    s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output:
    2
Explanation:
    Substring "aaa" occur 2 times in the string. It can overlap.

Example 3:

Input:
    s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output:
    3

Example 4:

Input:
    s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output:
    0


Constraints:

    1 <= s.length <= 10^5
    1 <= maxLetters <= 26
    1 <= minSize <= maxSize <= min(26, s.length)
    s only contains lowercase English letters.
"""


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        res = 0
        l = minSize
        tmp = {}
        cache = {}
        for c in s[:l]:
            tmp[c] = tmp.get(c, 0) + 1
        if len(tmp) <= maxLetters:
            cache[s[:l]] = 1
            res = max(res, 1)
        for i in range(1, len(s) - l + 1):
            ss = s[i: i + l]
            tmp[ss[-1]] = tmp.get(ss[-1], 0) + 1
            tmp[s[i - 1]] -= 1
            if tmp[s[i - 1]] == 0:
                del tmp[s[i - 1]]
            if len(tmp) <= maxLetters:
                cache[ss] = cache.get(ss, 0) + 1
                res = max(res, cache[ss])
        return res


examples = [
    {
        "input": {
            "s": "aababcaab",
            "maxLetters": 2,
            "minSize": 3,
            "maxSize": 4
        },
        "output": 2
    }, {
        "input": {
            "s": "aaaa",
            "maxLetters": 1,
            "minSize": 3,
            "maxSize": 3
        },
        "output": 2
    }, {
        "input": {
            "s": "aabcabcab",
            "maxLetters": 2,
            "minSize": 2,
            "maxSize": 3
        },
        "output": 3
    }, {
        "input": {
            "s": "abcde",
            "maxLetters": 2,
            "minSize": 3,
            "maxSize": 3
        },
        "output": 0
    }, {
        "input": {
            "s": "bccaabac",
            "maxLetters": 2,
            "minSize": 2,
            "maxSize": 2
        },
        "output": 1
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
