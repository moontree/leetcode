"""
Let f(x) be the number of zeroes at the end of x!.
(Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end,
while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end.
Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input:
    K = 0
Output:
    5
Explanation:
    0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input:
    K = 5
Output:
    0
Explanation:
    There is no x such that x! ends in K = 5 zeroes.
Note:
    K will be an integer in the range [0, 10^9].
"""


class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def helper(n):
            count = 0
            while n:
                n /= 5
                count += n
            return count

        l, r = 0, 5 * K
        while l <= r:
            mid = (l + r) / 2
            c = helper(mid)

            if c < K:
                l = mid + 1
            elif c > K:
                r = mid - 1
            else:
                return 5

        return 0


examples = [
    {
        "input": {
            "K": 0
        },
        "output": 5
    }, {
        "input": {
            "K": 5
        },
        "output": 0
    }, {
        "input": {
            "K": 3
        },
        "output": 5
    }, {
        "input": {
            "K": 1
        },
        "output": 5
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
        print func(**example['input']) == example['output']
