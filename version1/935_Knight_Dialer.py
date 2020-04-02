"""
A chess knight can move as indicated in the chess diagram below:
1 2 3
4 5 6
7 8 9
  0
This time, we place our chess knight on any numbered key of a phone pad (indicated above),
and the knight makes N-1 hops.
Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight),
it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:
Input:
    1
Output:
    10

Example 2:
Input:
    2
Output:
    20

Example 3:
Input:
    3
Output:
    46


Note:
    1 <= N <= 5000
"""


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        base = 10 ** 9 + 7

        nums = [1, 1, 1, 1]# {1, 3, 7, 9}, {2, 8}, {4, 6}, {0}
        for _ in range(N - 1):
            tmp = [0, 0, 0, 0]
            tmp[0] = (nums[1] + nums[2]) % base
            tmp[1] = (2 * nums[0]) % base
            tmp[2] = (nums[3] + 2 * nums[0]) % base
            tmp[3] = (2 * nums[2]) % base
            nums = tmp[:]

        return (4 * nums[0] + 2 * nums[1] + 2 * nums[2] + nums[3]) % base
        # nums = [1 for _ in range(10)]
        # map = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        # base = 10 ** 9 + 7
        # print len(map)
        # for _ in range(N - 1):
        #     tmp = [0 for _ in range(10)]
        #     for i in range(10):
        #         for v in map[i]:
        #             tmp[i] += nums[v]
        #         tmp[i] %= base
        #     nums = tmp
        #     print nums
        # return sum(nums) % base

examples = [
    {
        "input": {
            "N": 1,
        },
        "output": 10
    }, {
        "input": {
            "N": 2
        },
        "output": 20
    }, {
        "input": {
            "N": 3,
        },
        "output": 46
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
