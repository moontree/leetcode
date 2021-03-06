"""
Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

Each a_i is a non-empty string;
Their concatenation a_1 + a_2 + ... + a_k is equal to text;
For all 1 <= i <= k,  a_i = a_{k+1 - i}.


Example 1:

Input:
    text = "ghiabcdefhelloadamhelloabcdefghi"
Output:
    7
Explanation:
    We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

Example 2:

Input:
    text = "merchant"
Output:
    1
Explanation:
    We can split the string on "(merchant)".

Example 3:

Input:
    text = "antaprezatepzapreanta"
Output:
    11
Explanation:
    We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".

Example 4:

Input:
    text = "aaa"
Output:
    3
Explanation:
    We can split the string on "(a)(a)(a)".


Constraints:

    text consists only of lowercase English characters.
    1 <= text.length <= 1000
"""


class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        if len(text) < 2:
            return len(text)
        d = len(text)
        p = d / 2 + 1
        for l in range(p):
            if text[:l] == text[-l:]:
                return self.longestDecomposition(text[l: -l]) + 2
        return 1


examples = [
    {
        "input": {
            "text": "ghiabcdefhelloadamhelloabcdefghi",
        },
        "output": 7
    },  {
        "input": {
            "text": "merchant",
        },
        "output": 1
    },  {
        "input": {
            "text": "antaprezatepzapreanta",
        },
        "output": 11
    },  {
        "input": {
            "text": "aaa",
        },
        "output": 3
    },  {
        "input": {
            "text": "elvtoelvto",
        },
        "output": 2
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
