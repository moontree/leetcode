"""
Given a positive integer N,
find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.


Example 1:

Input:
    22
Output:
    2
Explanation:
    22 in binary is 0b10110.
    In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
    The first consecutive pair of 1's have distance 2.
    The second consecutive pair of 1's have distance 1.
    The answer is the largest of these two distances, which is 2.

Example 2:

Input:
    5
Output:
    2
Explanation:
    5 in binary is 0b101.

Example 3:

Input:
    6
Output:
    1
Explanation:
    6 in binary is 0b110.

Example 4:

Input:
    8
Output:
    0
Explanation:
    8 in binary is 0b1000.
    There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.


Note:

    1 <= N <= 10^9
"""


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        q = []
        res, l, r = 0, -1, -1
        while N:
            q.append(N % 2)
            N /= 2
        for i, v in enumerate(q):
            if v == 1:
                if l == -1:
                    l = i
                elif r == -1:
                    r = i
                else:
                    l, r = r, i
                if r != -1:
                    res = max(res, r - l)
        return res


examples = [
    {
        "input": {
            "N":  22
        },
        "output": 2
    }, {
        "input": {
            "N":  5
        },
        "output": 2
    }, {
        "input": {
            "N":  6
        },
        "output": 1
    }, {
        "input": {
            "N":  8
        },
        "output": 0
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
