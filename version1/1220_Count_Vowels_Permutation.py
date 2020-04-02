"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input:
    n = 1
Output:
    5
Explanation:
    All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:

Input:
    n = 2
Output:
    10
Explanation:
    All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3:

Input:
    n = 5
Output:
    68


Constraints:

    1 <= n <= 2 * 10^4
"""


class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1, 1, 1, 1, 1]
        for i in range(n - 1):
            nums = [nums[1] + nums[4] + nums[2], nums[0] + nums[2], nums[1] + nums[3], nums[2], nums[3] + nums[2]]
        return sum(nums) % (10 ** 9 + 7)


examples = [
    {
        "input": {
            "n": 1,
        },
        "output": 5
    }, {
        "input": {
            "n": 2,
        },
        "output": 10
    }, {
        "input": {
            "n": 5,
        },
        "output": 68
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
