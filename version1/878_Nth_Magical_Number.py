"""
A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.
Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input:
    N = 1, A = 2, B = 3
Output:
    2

Example 2:

Input:
    N = 4, A = 2, B = 3
Output:
    6

Example 3:

Input:
    N = 5, A = 2, B = 4
Output:
    10

Example 4:

Input:
    N = 3, A = 6, B = 4
Output:
    8

Note:

    1 <= N <= 10^9
    2 <= A <= 40000
    2 <= B <= 40000
"""


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        m = 10 ** 9 + 7
        a, b = max(A, B), min(A, B)
        while b:
            a, b = b, a % b
        v = A * B / a
        l, r = 0, 10 ** 14

        def count(num):
            return num / A + num / B - num / v

        while l < r:
            mid = (l + r) // 2
            if count(mid) >= N:
                r = mid
            else:
                l = mid + 1
        return l % (10 ** 9 + 7)
        # gn = v / A + v / B - 1
        # print v, gn
        # blocks, idx = N / gn, N % gn
        #
        # c = 0
        # offset, na, nb = 0, A, B
        # while c < idx:
        #     if na < nb:
        #         offset = na
        #         na += A
        #     else:
        #         offset = nb
        #         nb += B
        #     c += 1
        # return (blocks * v + offset) % m


examples = [
    {
        "input": {
            "N": 1,
            "A": 2,
            "B": 3
        },
        "output": 2
    }, {
        "input": {
            "N": 4,
            "A": 2,
            "B": 3
        },
        "output": 6
    }, {
        "input": {
            "N": 5,
            "A": 2,
            "B": 4
        },
        "output": 10
    }, {
        "input": {
            "N": 3,
            "A": 6,
            "B": 4
        },
        "output": 8
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
