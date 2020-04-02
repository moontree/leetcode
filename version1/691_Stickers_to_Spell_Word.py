"""
=========================
Project -> File: leetcode -> 691_Stickers_to_Spell_Word.py
Author: zhangchao
=========================
We are given N different types of stickers.
Each sticker has a lowercase English word on it.

You would like to spell out the given target string by
cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want,
and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target?
If the task is impossible, return -1.

Example 1:

Input:
    ["with", "example", "science"], "thehat"
Output:
    3
Explanation:
    We can use 2 "with" stickers, and 1 "example" sticker.
    After cutting and rearrange the letters of those stickers, we can form the target "thehat".
    Also, this is the minimum number of stickers necessary to form the target string.

Example 2:

Input:
    ["notice", "possible"], "basicbasic"
Output:
    -1
Explanation:
    We can't form the target "basicbasic" from cutting letters from the given stickers.

Note:
    stickers has length in the range [1, 50].
    stickers consists of lowercase English words (without apostrophes).
    target has length in the range [1, 15], and consists of lowercase English letters.
    In all test cases, all words were chosen randomly from the 1000 most common US English words,
    and the target was chosen as a concatenation of two random words.
    The time limit may be more challenging than usual.
    It is expected that a 50 sticker test case can be solved within 35ms on average.
"""
import copy


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        base = ord('a')
        words = []
        for sticker in stickers:
            tmp = [0 for _ in range(26)]
            for c in sticker:
                tmp[ord(c) - base] += 1
            words.append(tmp)

        cache = {}

        def helper(s):
            if not s:
                return 0
            if s not in cache:
                res = float('inf')
                counts = [0 for _ in range(26)]
                for c in s:
                    counts[ord(c) - base] += 1
                for word in words:
                    if word[ord(s[0]) - base] == 0:
                        continue
                    ss = ""
                    for j in range(26):
                        if counts[j] > word[j]:
                            ss += chr(base + j) * (counts[j] - word[j])
                    res = min(res, helper(ss) + 1)
                cache[s] = res
            return cache[s]
        res = helper(target)
        if res > 20:
            res = -1
        return res


examples = [
    {
        "input": {
            "stickers": ["with", "example", "science"],
            "target": "thehat"
        },
        "output": 3
    }, {
        "input": {
            "stickers": ["notice", "possible"],
            "target": "basicbasic"
        },
        "output": -1
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
