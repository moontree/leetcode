"""
n a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input:
    [30,20,150,100,40]
Output:
    3
Explanation:
    Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input:
    [60,60,60]
Output:
    3
Explanation:
    All three pairs have a total duration of 120, which is divisible by 60.
"""


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        cache = {}
        for n in time:
            m = n % 60
            cache[m] = cache.get(m, 0) + 1
        res = 0
        for k, c in cache.items():
            if k == 0 or k == 30:
                res += c * (c - 1) / 2
            elif k < 30:
                res += c * cache.get(60 - k, 0)
        return res


examples = [
    {
        "input": {
            "time": [30, 20, 150, 100, 40],
        },
        "output": 3
    }, {
        "input": {
            "time": [60, 60, 60],
        },
        "output": 3
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
