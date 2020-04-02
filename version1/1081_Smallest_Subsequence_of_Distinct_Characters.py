"""
Return the lexicographically smallest subsequence of text that contains
all the distinct characters of text exactly once.


Example 1:

Input: "cdadabcc"
Output: "adbc"

Example 2:

Input: "abcd"
Output: "abcd"

Example 3:

Input: "ecbacba"
Output: "eacb"

Example 4:

Input: "leetcode"
Output: "letcod"


Note:

    1 <= text.length <= 1000
    text consists of lowercase English letters.
"""


class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        cache = {}
        for c in text:
            cache[c] = cache.get(c, 0) + 1
        q = []
        for c in text:
            cache[c] -= 1
            if c in q:
                continue
            while q and q[-1] > c and cache[q[-1]] > 0:
                q.pop()
            q.append(c)
            print c, q
        res = ''.join(q)

        return res


examples = [
    {
        "input": {
            "text": "cdadabcc",
        },
        "output": "adbc"
    }, {
        "input": {
            "text": "abcd",
        },
        "output": "abcd"
    }, {
        "input": {
            "text": "ecbacba",
        },
        "output": "eacb"
    }, {
        "input": {
            "text": "leetcode",
        },
        "output": "letcod"
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
