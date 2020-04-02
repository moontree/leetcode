"""
=========================
Project -> File: leetcode -> 1390_Four_Divisors.py
Author: zhangchao
=========================
Given an integer array nums,
return the sum of divisors of the integers in that array that have exactly four divisors.
If there is no such integer in the array, return 0.

Example 1:

Input:
    nums = [21,4,7]
Output:
    32
Explanation:
    21 has 4 divisors: 1, 3, 7, 21
    4 has 3 divisors: 1, 2, 4
    7 has 2 divisors: 1, 7
    The answer is the sum of divisors of 21 only.


Constraints:

    1 <= nums.length <= 10^4
    1 <= nums[i] <= 10^5
"""


class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(n):
            res, c = 0, 0
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    if i == n / i:
                        res += i
                        c += 1
                    else:
                        res += i + n / i
                        c += 2
                if c > 4:
                    break
            if c == 4:
                return True, res
            return False, 0

        ans = 0
        for n in nums:
            valid, tmp = helper(n)
            if valid:
                print n, tmp
                ans += tmp
        return ans


examples = [
    {
        "input": {
            "nums": [21, 4, 7],
        },
        "output": 32
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
