"""
Strings A and B are K-similar (for some non-negative integer K)
if we can swap the positions of two letters in A exactly K times
so that the resulting string equals B.

Given two anagrams A and B,
return the smallest K for which A and B are K-similar.

Example 1:

Input:
    A = "ab", B = "ba"
Output:
    1

Example 2:

Input:
    A = "abc", B = "bca"
Output:
    2

Example 3:

Input:
    A = "abac", B = "baca"
Output:
    2

Example 4:

Input:
    A = "aabc", B = "abca"
Output:
    2
Note:

    1 <= A.length == B.length <= 20
    A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
"""


class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        cache = {}

        def helper(a, b):
            if (a, b) in cache:
                return cache[(a, b)]
            if a == b:
                res = 0
                cache[(a, b)] = 0
                pass
            elif a[0] == b[0]:
                res = helper(a[1:], b[1:])
                cache[(a, b)] = res
            else:
                res = float('inf')
                for i in range(1, len(b)):
                    ra = a[1:]
                    if b[i] == a[0]:
                        rb = b[1: i] + b[0] + b[i + 1:]
                        v = helper(ra, rb)
                        if res > v:
                            res = v
                res += 1
                cache[(a, b)] = res
            return res

        res = helper(A, B)
        return res


examples = [
    {
        "input": {
            "A": "ab",
            "B": "ba",
        },
        "output": 1
    }, {
        "input": {
            "A": "abc",
            "B": "bca",
        },
        "output": 2
    }, {
        "input": {
            "A": "abac",
            "B": "baca",
        },
        "output": 2
    }, {
        "input": {
            "A": "aabc",
            "B": "abca",
        },
        "output": 2
    },
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
