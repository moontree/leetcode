"""
Given 2 integers n and start.
Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

p[0] = start
p[i] and p[i+1] differ by only one bit in their binary representation.
p[0] and p[2^n -1] must also differ by only one bit in their binary representation.


Example 1:

Input:
    n = 2, start = 3
Output:
    [3,2,0,1]
Explanation:
    The binary representation of the permutation is (11,10,00,01).
    All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]

Example 2:

Input:
    n = 3, start = 2
Output:
    [2,6,7,5,4,0,1,3]
Explanation:
    The binary representation of the permutation is (010,110,111,101,100,000,001,011).

Constraints:
    1 <= n <= 16
    0 <= start < 2 ^ n
"""


class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        nums = [0, 1]
        for i in range(2, n + 1):
            base = 1 << (i - 1)
            nums = nums + [base + v for v in nums[::-1]]
        i = nums.index(start)
        return nums[i:] + nums[:i]


examples = [
    {
        "input": {
            "n": 2,
            "start": 3
        },
        "output": [3, 2, 0, 1]
    }, {
        "input": {
            "n": 3,
            "start": 2
        },
        "output": [2, 6, 7, 5, 4, 0, 1, 3]
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
