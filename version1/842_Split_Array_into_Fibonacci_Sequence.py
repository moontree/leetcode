"""
Given a string S of digits, such as S = "123456579",
we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally,
a Fibonacci-like sequence is a list F of non-negative integers such that:

    0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
    F.length >= 3;
    and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces,
each piece must not have extra leading zeroes,
except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S,
or return [] if it cannot be done.

Example 1:

Input:
    "123456579"
Output:
    [123,456,579]

Example 2:

Input:
    "11235813"
Output:
    [1,1,2,3,5,8,13]

Example 3:

Input:
    "112358130"
Output:
    []
Explanation:
    The task is impossible.

Example 4:
Input:
    "0123"
Output:
    []
Explanation:
    Leading zeroes are not allowed, so "01", "2", "3" is not valid.


Example 5:

Input:
    "1101111"
Output:
    [110, 1, 111]
Explanation:
    The output [11, 0, 11, 11] would also be accepted.

Note:

    1 <= S.length <= 200
    S contains only digits.
"""


class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        max_int = (1 << 31) - 1

        def fib(a, b, s):
            la, lb = len(a), len(b)
            sc = la + lb
            res = [int(a), int(b)]
            while sc < len(s):
                c = int(a) + int(b)
                if c > max_int:
                    return []
                lc = len(str(c))
                if s[sc: sc + lc] == str(c):
                    res.append(c)
                    sc += lc
                    a, b = b, c
                else:
                    return []
            if sc == len(s):
                return res
            else:
                return []

        max_len = len(str(max_int)) + 1
        for i in range(1, min(len(S), max_len)):
            for j in range(i + 1, min(len(S), i + max_len)):
                if len(S) - j < max(i, j - i):  # No room for the sum
                    break
                a, b = S[:i], S[i:j]
                if len(a) > 1 and a[0] == 0:
                    continue
                elif len(b) > 1 and b[0] == 0:
                    continue
                else:
                    res = fib(a, b, S)
                    if len(res):
                        valid = True
                        for v in res:
                            if v > max_int:
                                valid = False
                                break
                        if valid:
                            return res
        return []


examples = [
    {
        "input": {
            "S": "123456579",
        },
        "output": [123, 456, 579]
    }, {
        "input": {
            "S": "11235813",
        },
        "output": [1, 1, 2, 3, 5, 8, 13]
    }, {
        "input": {
            "S": "112358130",
        },
        "output": []
    }, {
        "input": {
            "S": "0123",
        },
        "output": []
    }, {
        "input": {
            "S": "1101111",
        },
        "output": [11, 0,  11, 11]
    }, {
        "input": {
            "S": "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511",
        },
        "output": []
    }, {
        "input": {
            "S": "3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909",
        },
        "output": []
    },
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