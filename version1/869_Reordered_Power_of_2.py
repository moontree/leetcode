"""
Starting with a positive integer N,
we reorder the digits in any order (including the original order)
such that the leading digit is not zero.

Return true if and only if we can do this in a way
such that the resulting number is a power of 2.



Example 1:
Input:
    1
Output:
    true

Example 2:
Input:
    10
Output:
    false

Example 3:
Input:
    16
Output:
    true

Example 4:
Input:
    24
Output:
    false

Example 5:
Input:
    46
Output:
    true

Note:
    1 <= N <= 10^9
"""


class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        def check(a, b):
            cache = {}
            for v in a:
                cache[v] = cache.get(v, 0) + 1
            for v in b:
                cache[v] = cache.get(v, 0) - 1
                if cache[v] < 0:
                    return False
            for v in cache.values():
                if v != 0:
                    return False
            return True

        nums = []
        v = 1
        for i in range(0, 31):
            nums.append(v)
            v = (v << 1)
        for n in nums:
            if len(str(n)) == len(str(N)):
                if check(str(n), str(N)):
                    return True
        return False


examples = [
    {
        "input": {
            "N": 1
        },
        "output": True
    }, {
        "input": {
            "N":  10
        },
        "output": False
    }, {
        "input": {
            "N":  16
        },
        "output": True
    }, {
        "input": {
            "N":  24
        },
        "output": False
    }, {
        "input": {
            "N":  46
        },
        "output": True
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']
