"""
For some fixed N,
an array A is beautiful if it is a permutation of the integers 1, 2, ..., N,
such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)



Example 1:

Input:
    4
Output:
    [2, 1, 4, 3]

Example 2:

Input:
    5
Output:
    [3, 1, 2, 5, 4]


Note:

1 <= N <= 1000

"""


class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        def helper(nums):
            if len(nums) < 3:
                return nums
            else:
                nums = helper(nums[::2]) + helper(nums[1::2])
                return nums

        res = range(1, N + 1)
        return helper(res)


examples = [
    {
        "input": {
            "N": 4,
        },
        "output": [2, 1, 4, 3]
    }, {
        "input": {
            "N": 5,
        },
        "output": [3, 1, 2, 5, 4]
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
