"""
We have a sorted set of digits D,
a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.
(Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.
For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.



Example 1:

Input:
    D = ["1","3","5","7"],
    N = 100
Output:
    20
Explanation:
    The 20 numbers that can be written are:
    1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:

Input:
    D = ["1","4","9"], N = 1000000000
Output:
    29523
Explanation:
    We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
    81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
    2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
    In total, this is 29523 integers that can be written using the digits of D.


Note:

    D is a subset of digits '1'-'9' in sorted order.
    1 <= N <= 10^9
"""


class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        nums = []
        while N:
            nums.append(N % 10)
            N /= 10
        nums = nums[::-1]
        d = [int(v) for v in D]

        def helper(a, d, i):
            if len(a) == i:
                return 1
            n = len(a) - i - 1
            res = 0
            count = 0
            for c in d:
                if c < a[i]:
                    count += 1
                elif c == a[i]:
                    res += helper(a, d, i + 1)
                    break
            res += (len(d) ** n) * count
            return res

        ans = 0
        tmp = 1
        for i in range(1, len(nums)):
            tmp *= len(d)
            ans += tmp
        ans += helper(nums, d, 0)
        return ans


examples = [
    {
        "input": {
            "D": ["1", "3", "5", "7"],
            "N": 100,
        },
        "output": 20
    }, {
        "input": {
            "D": ["1", "4", "9"],
            "N": 1000000000,
        },
        "output": 29523
    }, {
        "input": {
            "D": ["7"],
            "N": 8,
        },
        "output": 1
    }, {
        "input": {
            "D": ["3", "4", "8"],
            "N": 4,
        },
        "output": 2
    }
]

print(3 ** 9)
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
