"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
Beyond that, now the encoded string can also contain the character '*',
which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*',
return the total number of ways to decode it.

Also, since the answer may be very large,
you should return the output mod 10^9 + 7.

Example 1:
Input:
    "*"
Output:
    9
Explanation:
    The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:
Input:
    "1*"
Output:
    9 + 9 = 18
Note:
    The length of the input string will fit in range [1, 105].
    The input string will only contain the character '*' and digits '0' - '9'.
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 10 ** 9 + 7
        dp_s = [0]  # s[i] is single
        dp_d = [0]  # s[i] is double, and is end
        res = [1]
        for i, c in enumerate(s):
            if i == 0:
                dp_d.append(0)
                dp_s.append(9 if c == '*' else 1)
                if c == '0':
                    dp_s[-1] = 0
            elif c == '*':
                dp_s.append(9 * res[-1] % base)
                if s[i - 1] == '1':
                    dp_d.append(9 * res[-2] % base)
                elif s[i - 1] == '2':
                    dp_d.append(6 * res[-2] % base)
                elif s[i - 1] == '*':
                    dp_d.append(15 * res[-2] % base)
                else:
                    dp_d.append(0)
            else:
                if c == '0':
                    dp_s.append(0)
                else:
                    dp_s.append(res[-1] % base)
                if s[i - 1] == '1':
                    dp_d.append(res[-2] % base)
                elif s[i - 1] == '2' and c < '7':
                    dp_d.append(res[-2] % base)
                elif s[i - 1] == '*':
                    if c < '7':
                        dp_d.append(2 * res[-2] % base)
                    else:
                        dp_d.append(res[-2] % base)
                else:
                    dp_d.append(0)
            res.append((dp_d[-1] + dp_s[-1]) % base)
        return res[-1]


examples = [
    {
        "input": {
            "s": "*",
        },
        "output": 9
    }, {
        "input": {
            "s": "1*",
        },
        "output": 18
    }, {
        "input": {
            "s": "**",
        },
        "output": 96
    }, {
        "input": {
            "s": "0",
        },
        "output": 0
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
