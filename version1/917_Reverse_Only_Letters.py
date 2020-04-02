"""
Given a string S,
return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.


Example 1:
Input:
    "ab-cd"
Output:
    "dc-ba"

Example 2:
Input:
    "a-bC-dEf-ghIj"
Output:
    "j-Ih-gfE-dCba"

Example 3:
Input:
    "Test1ng-Leet=code-Q!"
Output:
    "Qedo1ct-eeLg=ntse-T!"


Note:

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122
    S doesn't contain \ or "
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = [c for c in S]
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and (not s[l].isalpha()):
                l += 1
            while l < r and (not s[r].isalpha()):
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)


examples = [
    {
        "input": {
            "S": "ab-cd",
        },
        "output": "dc-ba"
    }, {
        "input": {
            "S": "a-bC-dEf-ghIj",
        },
        "output": "j-Ih-gfE-dCba"
    }, {
        "input": {
            "S": "Test1ng-Leet=code-Q!",
        },
        "output": "Qedo1ct-eeLg=ntse-T!"
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
