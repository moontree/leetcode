"""
For strings S and T,
we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.



Example 1:

Input:
    str1 = "ABCABC", str2 = "ABC"
Output:
    "ABC"

Example 2:

Input:
    str1 = "ABABAB", str2 = "ABAB"
Output:
    "AB"

Example 3:

Input:
    str1 = "LEET", str2 = "CODE"
Output: ""

Note:
    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] and str2[i] are English uppercase letters.
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        while str2:
            n = len(str2)
            while len(str1) >= n:
                if str1[:n] != str2:
                    return ""
                str1 = str1[n:]
            str1, str2 = str2, str1
        return str1


examples = [
    {
        "input": {
            "str1": "ABCABC",
            "str2": "ABC"
        },
        "output": "ABC"
    }, {
        "input": {
            "str1": "ABABAB",
            "str2": "ABAB"
        },
        "output": "AB"
    },  {
        "input": {
            "str1": "LEET",
            "str2": "CODE"
        },
        "output": ""
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
