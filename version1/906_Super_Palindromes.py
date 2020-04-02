"""
Let's say a positive integer is a superpalindrome if it is a palindrome,
and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings),
return the number of superpalindromes in the inclusive range [L, R].



Example 1:

Input:
    L = "4", R = "1000"
Output:
    4
Explanation:
    4, 9, 121, and 484 are superpalindromes.
    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.


Note:

    1 <= len(L) <= 18
    1 <= len(R) <= 18
    L and R are strings representing integers in the range [1, 10^18).
    int(L) <= int(R)

"""
import math


class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        def is_palindrome(n):
            v = str(n)
            l, r = 0, len(v) - 1
            while l < r:
                if v[l] == v[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def generate_palindrome(l):
            res = [[''], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]
            for i in range(2, l + 1):
                if i % 2 == 0:
                    tmp = []
                    base = i / 2 - 1
                    small = 1
                    if i > 2:
                        small = 0
                    for v in res[-2]:
                        for k in range(small, 10):
                            tmp.append(v[:base] + str(k) * 2 + v[base:])
                    res.append(tmp[:])
                elif i % 2 == 1:
                    tmp = []
                    base = i / 2
                    for v in res[-1]:
                        for k in range(10):
                            tmp.append(v[:base] + str(k) + v[base:])
                    res.append(tmp[:])
            return res

        # v = generate_palindrome(10)
        LL = int(math.sqrt(L))
        RR = int(math.sqrt(R)) + 1
        s, e = len(str(LL)), len(str(RR))
        palindromes = generate_palindrome(e)
        res = 0
        for l in range(s, e + 1):
            for i in palindromes[l]:
                i = int(i)
                sq = i * i
                if LL <= i <= RR and L <= sq <= R:
                    if is_palindrome(i) and is_palindrome(sq):
                        res += 1
        return res


examples = [
    {
        "input": {
            "L": 4,
            "R": 1000,
        },
        "output": 4
    }, {
        "input": {
            "L": 4,
            "R": 10 ** 18,
        },
        "output": 69
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

