"""
=========================
Project -> File: leetcode -> 1189_Maximum_Number_of_Balloons.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/7 8:29 PM
=========================
"""
"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.


Example 1:
Input: 
    text = "nlaebolko"
Output: 
    1

Example 2:
Input: text = "loonbalxballpoon"
    Output: 2

Example 3:
Input: 
    text = "leetcode"
Output: 
    0
 

Constraints:

    1 <= text.length <= 10^4
    text consists of lower case English letters only.
"""


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        cache = {}
        for c in text:
            cache[c] = cache.get(c, 0) + 1
        return min(cache.get('a', 0), cache.get('b', 0), cache.get('n', 0), cache.get('l', 0) / 2, cache.get('o', 0) / 2)


examples = [
    {
        "input": {
            "text": "nlaebolko",
        },
        "output": 1
    },  {
        "input": {
            "text": "loonbalxballpoon",
        },
        "output": 2
    },  {
        "input": {
            "text": "leetcode",
        },
        "output": 0
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
