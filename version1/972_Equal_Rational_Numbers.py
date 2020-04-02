"""
Given two strings S and T,
each of which represents a non-negative rational number,
return True if and only if they represent the same number.
The strings may use parentheses to denote the repeating part of the rational number.

In general a rational number can be represented using up to three parts:
an integer part, a non-repeating part, and a repeating part.
The number will be represented in one of the following three ways:

<IntegerPart> (e.g. 0, 12, 123)
<IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:

1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.


Example 1:

Input:
    S = "0.(52)", T = "0.5(25)"
Output:
    true
Explanation:
    Because "0.(52)" represents 0.52525252...,
    and "0.5(25)" represents 0.52525252525..... ,
    the strings represent the same number.

Example 2:

Input:
    S = "0.1666(6)", T = "0.166(66)"
Output:
    true

Example 3:
Input:
    S = "0.9(9)", T = "1."
Output:
    true
Explanation:
    "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
    "1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".

Note:
    Each part consists only of digits.
    The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
    1 <= <IntegerPart>.length <= 4
    0 <= <NonRepeatingPart>.length <= 4
    1 <= <RepeatingPart>.length <= 4
"""


class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def get_true_value(s):
            data = s.split('(')
            # process unrepeat
            dot = data[0].split('.')
            zero_count = 0
            if len(dot) > 1:
                zero_count = len(dot[1])
            base = 10 ** zero_count
            v1 = int(''.join(data[0].split('.')))

            if len(data) > 1:
                repeated = data[1][:-1]
                repeated_val = int(repeated)
                base2 = 10 ** len(repeated) - 1
                return v1 * base2 + repeated_val, base * base2
            return v1, base

        sv, tv = get_true_value(S), get_true_value(T)
        return sv[0] * tv[1] == sv[1] * tv[0]


examples = [
    {
        "input": {
            "S": "0.(52)",
            "T": "0.5(25)"
        },
        "output": True
    }, {
        "input": {
            "S": "0.1666(6)",
            "T": "0.166(66)"
        },
        "output": True
    }, {
        "input": {
            "S": "0.9(9)",
            "T": "1."
        },
        "output": True
    }, {
        "input": {
            "S": "1.9(9)",
            "T": "1."
        },
        "output": False
    }, {
        "input": {
            "S": "8.123(4567)",
            "T": "8.123(4566)"
        },
        "output": False
    }, {
        "input": {
            "S": "323.32(32)",
            "T": "323.323(23)"
        },
        "output": True
    }, {
        "input": {
            "S": "0.(0)",
            "T": "0"
        },
        "output": True
    }, {
        "input": {
            "S": "86.86(86)",
            "T": "86.8(68)"
        },
        "output": True
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
