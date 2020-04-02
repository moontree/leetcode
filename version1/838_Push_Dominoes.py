"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides,
it stays still due to the balance of the forces.

For the purposes of this question,

we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state.
S[i] = 'L', if the i-th domino has been pushed to the left;
S[i] = 'R', if the i-th domino has been pushed to the right;
S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.

Example 1:

Input:
    ".L.R...LR..L.."
Output:
    "LL.RR.LLRRLL.."

Example 2:

Input:
    "RR.L"
Output:
    "RR.L"
Explanation:
    The first domino expends no additional force on the second domino.
Note:

    0 <= N <= 10^5
    String dominoes contains only 'L', 'R' and '.'

"""


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        res, tmp = '', ''
        for c in dominoes:
            if c == '.':
                tmp += c
            elif c == 'R':
                if tmp:
                    res += tmp[0] * len(tmp)
                tmp = 'R'
            elif c == 'L':
                count = len(tmp) + 1
                cc = count / 2
                if tmp and tmp[0] == 'R':
                    if count % 2 == 0:
                        res += 'R' * cc + 'L' * cc
                    else:
                        res += 'R' * cc + '.' + 'L' * cc
                else:
                    res += 'L' * count
                tmp = ''
        if tmp:
            res += tmp[0] * len(tmp)
        return res


examples = [
    {
        "input": {
            "dominoes": ".L.R...LR..L.."
        },
        "output": "LL.RR.LLRRLL.."
    }, {
        "input": {
            "dominoes": "RR.L"
        },
        "output": "RR.L"
    }, {
        "input": {
            "dominoes": ".L.R."
        },
        "output": "LL.RR"
    }, {
        "input": {
            "dominoes":"R.R.L"
        },
        "output": "RRR.L"
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']



