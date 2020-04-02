"""
Given two strings A and B of lowercase letters,
return true if and only if we can swap two letters in A so that the result equals B.


Example 1:

Input:
    A = "ab", B = "ba"
Output:
    true

Example 2:

Input:
    A = "ab", B = "ab"
Output:
    false

Example 3:

Input:
    A = "aa", B = "aa"
Output:
    true

Example 4:

Input:
    A = "aaaaaaabc", B = "aaaaaaacb"
Output:
    true

Example 5:

Input:
    A = "", B = "aa"
Output:
    false

Note:

    0 <= A.length <= 20000
    0<= B.length <= 20000
    A and B consist only of lowercase letters.
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        cache = {}
        sa, sb = '', ''
        has_same = False
        for i in range(len(A)):
            cache[A[i]] = cache.get(A[i], 0) + 1
            if cache[A[i]] > 1:
                has_same = True
            if A[i] != B[i]:
                sa += A[i]
                sb += B[i]
                if len(sa) > 2:
                    return False
        if len(sa) == 2 and sa == sb[::-1]:
            return True
        return len(sa) == 0 and has_same


examples = [
    {
        "input": {
            "A": 'ab',
            "B": 'ba',
        },
        "output": True
    }, {
        "input": {
            "A": 'ab',
            "B": 'ab',
        },
        "output": False
    }, {
        "input": {
            "A": 'aa',
            "B": 'aa',
        },
        "output": True
    }, {
        "input": {
            "A": 'aaaaaaabc',
            "B": 'aaaaaaacb',
        },
        "output": True
    }, {
        "input": {
            "A": '',
            "B": 'aa',
        },
        "output": False
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
