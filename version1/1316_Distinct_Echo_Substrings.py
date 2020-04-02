"""
Return the number of distinct non-empty substrings of text
that can be written as the concatenation of some string with itself (
i.e. it can be written as a + a where a is some string).



Example 1:

Input:
    text = "abcabcabc"
Output:
    3
Explanation:
    The 3 substrings are "abcabc", "bcabca" and "cabcab".

Example 2:

Input:
    text = "leetcodeleetcode"
Output:
    2
Explanation:
    The 2 substrings are "ee" and "leetcodeleetcode".


Constraints:

    1 <= text.length <= 2000
    text has only lowercase English letters.
"""


class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        cache = {}
        n = len(text)
        for i in range(n):
            rl = n - i
            for l in range(1, rl + 1):
                s = text[i: i + l]
                if s == text[i + l: i + 2 * l]:
                    cache[s] = 1
        return len(cache)


examples = [
    {
        "input": {
            "text": "abcabcabc",
        },
        "output": 3
    }, {
        "input": {
            "text": "leetcodeleetcode",
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
