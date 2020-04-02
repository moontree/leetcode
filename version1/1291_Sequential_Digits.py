"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input:
    low = 100, high = 300
Output:
    [123,234]

Example 2:

Input:
    low = 1000, high = 13000
Output:
    [1234,2345,3456,4567,5678,6789,12345]


Constraints:

    10 <= low <= high <= 10^9
"""


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        values = [
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789,
            ]
        res = []
        for v in values:
            if low <= v <= high:
                res.append(v)
            elif v > high:
                break
        return res


examples = [
    {
        "input": {
            "low": 100,
            "high": 300
        },
        "output": [123, 234]
    }, {
        "input": {
            "low": 1000,
            "high": 13000
        },
        "output": [1234, 2345, 3456, 4567, 5678, 6789, 12345]
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
