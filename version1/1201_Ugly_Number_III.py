"""
=========================
Project -> File: leetcode -> 1201_Ugly_Number_III.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/9 6:31 PM
=========================
"""
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.

 

Example 1:

Input: 
    n = 3, a = 2, b = 3, c = 5
Output:
    4
Explanation:
    The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
    
Example 2:

Input: 
    n = 4, a = 2, b = 3, c = 4
Output: 
    6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

Example 3:

Input: 
    n = 5, a = 2, b = 11, c = 13
Output: 
    10
Explanation: 
    The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
    
Example 4:

Input: 
    n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 
    1999999984
 

Constraints:

    1 <= n, a, b, c <= 10^9
    1 <= a * b * c <= 10^18
    It's guaranteed that the result will be in range [1, 2 * 10^9]
"""


class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        def gcd(a, b):
            if a > b:
                a, b = b, a
            while a:
                a, b = b % a, a
            return b

        c1, c2, c3 = gcd(a, b), gcd(a, c), gcd(b, c)
        # print(c1, c2, c3)
        v1, v2, v3 = a * b / c1, a * c / c2, b * c / c3
        v4 = c * v1 / gcd(v1, c)

        print(v1, v2, v3, v4)

        def count(m):
            return m / a + m / b + m / c - m / v1 - m / v2 - m / v3 + m / v4

        l, r = 0, 2 * (10 ** 9) + 1

        while True:
            mid = (l + r) / 2
            v = count(mid)
            if n == v:
                print(l, mid, v)
                for res in range(mid, l - 1, -1):
                    if res % a == 0 or res % b == 0 or res % c == 0:
                        return res
            elif v < n:
                l = mid + 1
            else:
                r = mid - 1


examples = [
    {
        "input": {
            "n": 3,
            "a": 2,
            "b": 3,
            "c": 5
        },
        "output": 4
    }, {
        "input": {
            "n": 4,
            "a": 2,
            "b": 3,
            "c": 4
        },
        "output": 6
    }, {
        "input": {
            "n": 5,
            "a": 2,
            "b": 11,
            "c": 13
        },
        "output": 10
    }, {
        "input": {
            "n": 1000000000,
            "a": 2,
            "b": 217983653,
            "c": 336916467
        },
        "output": 1999999984
    }, {
        "input": {
            "n": 7,
            "a": 7,
            "b": 7,
            "c": 7
        },
        "output": 49
    }, {
        "input": {
            "n": 8,
            "a": 5,
            "b": 7,
            "c": 3
        },
        "output": 14
    }, {
        "input": {
            "n": 10000,
            "a": 2,
            "b": 4,
            "c": 8
        },
        "output": 20000
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
