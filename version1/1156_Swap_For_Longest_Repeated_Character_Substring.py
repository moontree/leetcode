"""
Given a string text, we are allowed to swap two of the characters in the string.
Find the length of the longest substring with repeated characters.



Example 1:

Input:
    text = "ababa"
Output:
    3
Explanation:
    We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'.
    Then, the longest repeated character substring is "aaa", which its length is 3.

Example 2:

Input:
    text = "aaabaaa"
Output:
    6
Explanation:
    Swap 'b' with the last 'a' (or the first 'a'),
    and we get longest repeated character substring "aaaaaa",
    which its length is 6.

Example 3:

Input:
    text = "aaabbaaa"
Output:
    4

Example 4:
Input:
    text = "aaaaa"
Output:
    5
Explanation:
    No need to swap, longest repeated character substring is "aaaaa", length is 5.

Example 5:

Input:
    text = "abcdef"
Output:
    1

Constraints:

    1 <= text.length <= 20000
    text consist of lowercase English characters only.
"""


class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        cache = {}
        s, cc = 0, text[0]
        res = 0
        for i, c in enumerate(text):
            if c == cc:
                continue
            else:
                if cc not in cache:
                    cache[cc] = []
                cache[cc].append([s, i - 1])
                cc = c
                s = i
        if cc not in cache:
            cache[cc] = []
        cache[cc].append([s, len(text) - 1])
        print cache

        for key in cache:
            partions = cache[key]
            if len(partions) == 1:
                res = max(res, partions[0][1] - partions[0][0] + 1)
            else:
                for i in range(1, len(partions)):
                    if partions[i][0] - partions[i - 1][1] == 2:
                        if len(partions) == 2:
                            res = max(res, partions[i][1] - partions[i - 1][0])
                        else:
                            res = max(res, partions[i][1] - partions[i - 1][0] + 1)
                    else:
                        res = max(res, partions[i][1] - partions[i][0] + 2,  partions[i - 1][1] - partions[i - 1][0] + 2)

        return res


examples = [
    {
        "input": {
            "text": "ababa",
        },
        "output": 3
    }, {
        "input": {
            "text": "aaabaaa",
        },
        "output": 6
    }, {
        "input": {
            "text": "aaabbaaa",
        },
        "output": 4
    }, {
        "input": {
            "text": "aaaaa",
        },
        "output": 5
    }, {
        "input": {
            "text": "abcdef",
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
