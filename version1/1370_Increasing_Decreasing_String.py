"""
=========================
Project -> File: leetcode -> 1370_Increasing_Decreasing_String.py
Author: zhangchao
=========================
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.

Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once
you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.


Example 1:

Input:
    s = "aaaabbbbcccc"
Output:
    "abccbaabccba"
Explanation:
    After steps 1, 2 and 3 of the first iteration, result = "abc"
    After steps 4, 5 and 6 of the first iteration, result = "abccba"
    First iteration is done. Now s = "aabbcc" and we go back to step 1
    After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
    After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input:
    s = "rat"
Output:
    "art"
Explanation:
    The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:

Input:
    s = "leetcode"
Output:
    "cdelotee"

Example 4:

Input:
    s = "ggggggg"
Output:
    "ggggggg"

Example 5:

Input:
    s = "spo"
Output:
    "ops"


Constraints:

    1 <= s.length <= 500
    s contains only lower-case English letters.
"""


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        nums = [0 for _ in range(26)]
        b = ord('a')
        for c in s:
            nums[ord(c) - b] += 1
        res = ''
        while len(res) < n:
            for i, v in enumerate(nums):
                if nums[i] > 0:
                    res += chr(i + b)
                    nums[i] -= 1
            for i, v in enumerate(nums):
                if nums[25 - i] > 0:
                    res += chr(25 - i + b)
                    nums[25 - i] -= 1
        return res


examples = [
    {
        "input": {
            "s": "aaaabbbbcccc",
        },
        "output": "abccbaabccba"
    }, {
        "input": {
            "s": "rat",
        },
        "output": "art"
    }, {
        "input": {
            "s": "leetcode",
        },
        "output": "cdelotee"
    }, {
        "input": {
            "s": "ggggggg",
        },
        "output": "ggggggg"
    }, {
        "input": {
            "s": "spo",
        },
        "output": "ops"
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
