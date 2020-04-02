"""
=========================
Project -> File: leetcode -> 1307_Verbal_Arithmetic_Puzzle.py
Author: zhangchao
=========================
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

    Each character is decoded as one digit (0 - 9).
    Every pair of different characters they must map to different digits.
    Each words[i] and result are decoded as one number without leading zeros.
    Sum of numbers on left side (words) will equal to the number on right side (result).
    Return True if the equation is solvable otherwise return False.


Example 1:

Input:
    words = ["SEND","MORE"], result = "MONEY"
Output:
    true
Explanation:
    Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
    Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652

Example 2:

Input:
    words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output:
    true
Explanation:
    Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
    Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214

Example 3:

Input:
    words = ["THIS","IS","TOO"], result = "FUNNY"
Output:
    true

Example 4:

Input:
    words = ["LEET","CODE"], result = "POINT"
Output:
    false


Constraints:

    2 <= words.length <= 5
    1 <= words[i].length, result.length <= 7
    words[i], result contains only upper case English letters.
    Number of different characters used on the expression is at most 10.
"""


class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
        """
        cache = {}
        for word in words:
            for i, c in enumerate(word[::-1]):
                cache[c] = cache.get(c, 0) + 10 ** i
        for i, c in enumerate(result[::-1]):
            cache[c] = cache.get(c, 0) - 10 ** i

        nz = {}
        for word in words + [result]:
            nz[word[0]] = 1

        pairs = [[v, k] for k, v in cache.items()]
        pairs.sort(key=lambda x: -abs(x[0]))
        # print pairs
        used = {}

        n = len(cache)
        used = {}
        cv = {}

        def find_range(pre_sum, i):
            pos, neg = [], []
            for v, c in pairs[i + 1:]:
                if v < 0:
                    neg.append(v)
                else:
                    pos.append(v)
            rest = [v for v in range(10) if used.get(v, 0) == 0]
            # print '---', i, neg, pos, 'rest: ', rest, used, cv
            l, r = 0, len(rest) - 1
            max_val, min_val = pre_sum, pre_sum
            for ii in range(len(neg)):
                max_val += neg[ii] * rest[l]
                l += 1
            for ii in range(len(pos)):
                max_val += pos[ii] * rest[r]
                r -= 1
            l, r = 0, len(rest) - 1
            for ii in range(len(pos)):
                min_val += pos[ii] * rest[l]
                l += 1
            for ii in range(len(neg)):
                min_val += neg[ii] * rest[r]
                r -= 1
            # print '---find_range', pairs[i], max_val, min_val
            if pairs[i][0] == 0:
                return -min_val , -max_val
            return -min_val / pairs[i][0], -max_val / pairs[i][0]

        def helper(cv, pre_sum, i):
            if i == n:
                s = 0
                for k in cache:
                    s += cache[k] * cv[k]
                if s == 0:
                    return True
            else:
                c = pairs[i][1]
                ll, rr = find_range(pre_sum, i)
                l = max(0, min(ll, rr) - 1)
                r = min(10, max(ll, rr) + 1)
                # print pairs[i], pre_sum, ll, rr, l, r, cv
                for vv in range(l, r):
                    if vv == 0 and c in nz:
                        continue
                    if used.get(vv, 0) == 0:
                        cv[c] = vv
                        used[vv] = 1
                        pre_sum += vv * pairs[i][0]
                        if helper(cv, pre_sum, i + 1):
                            return True
                        used[vv] = 0
                        pre_sum -= vv * pairs[i][0]
                        # del cv[chars[i]]
                return False

        return helper(cv, 0, 0)


examples = [
    {
        "input": {
            "words": ["SEND", "MORE"],
            "result": "MONEY"
        },
        "output": True
    }, {
        "input": {
            "words": ["SIX", "SEVEN", "SEVEN"],
            "result": "TWENTY"
        },
        "output": True
    }, {
        "input": {
            "words": ["THIS", "IS", "TOO"],
            "result": "FUNNY"
        },
        "output": True
    }, {
        "input": {
            "words": ["LEET", "CODE"],
            "result": "POINT"
        },
        "output": False
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
