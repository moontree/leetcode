"""
Given a positive integer n,
find the number of non-negative integers less than or equal to n,
whose binary representations do NOT contain consecutive ones.

Example 1:
Input:
    5
Output:
    5
Explanation:
    Here are the non-negative integers <= 5 with their corresponding binary representations:
    0 : 0
    1 : 1
    2 : 10
    3 : 11
    4 : 100
    5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Note: 1 <= n <= 10*9
"""


class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        odd_cache = {1: 1, 0: 1}
        even_cache = {1: 1, 0: 1}

        def odd(n):  # last is 1
            if n not in odd_cache:
                if n % 2 == 1:
                    odd_cache[n] = even(n / 2)
                else:
                    odd_cache[n] = even(n / 2 - 1)
            return odd_cache[n]

        def even(n):  # last is 0
            if n not in even_cache:
                even_cache[n] = even(n / 2) + odd(n / 2)
            return even_cache[n]

        return odd(num) + even(num)


examples = [
    {
        "input": {
            "num": 5,
        },
        "output": 5
    }, {
        "input": {
            "num": 1,
        },
        "output": 2
    },  {
        "input": {
            "num": 10,
        },
        "output": 8
    }, {
        "input": {
            "num": 80634655,
        },
        "output": 439204
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
