"""
=========================
Project -> File: leetcode -> 1190_Reverse_Substrings_Between_Each_Pair_of_Parentheses.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/7 8:34 PM
=========================
"""
"""
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.


Example 1:
Input: 
    s = "(abcd)"
Output: 
    "dcba"

Example 2:

Input: 
    s = "(u(love)i)"
Output: 
    "iloveu"
Explanation: 
    The substring "love" is reversed first, then the whole string is reversed.
    
Example 3:
Input: 
    s = "(ed(et(oc))el)"
Output: 
    "leetcode"
Explanation: 
    First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:
Input: 
    s = "a(bcdefghijkl(mno)p)q"
Output: 
    "apmnolkjihgfedcbq"
 
Constraints:

    0 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It's guaranteed that all parentheses are balanced.
"""


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = []
        for c in s:
            if c == '(':
                q.append(c)
            elif c == ')':
                tmp = ""
                while q and q[-1] != '(':
                    tmp += q.pop()[::-1]
                q.pop()
                q.append(tmp)
            else:
                q.append(c)
        return ''.join(q)


examples = [
    {
        "input": {
            "s": "(abcd)",
        },
        "output": "dcba"
    }, {
        "input": {
            "s": "(u(love)i)",
        },
        "output": "iloveu"
    }, {
        "input": {
            "s": "(ed(et(oc))el)",
        },
        "output": "leetcode"
    }, {
        "input": {
            "s": "a(bcdefghijkl(mno)p)q",
        },
        "output": "apmnolkjihgfedcbq"
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
