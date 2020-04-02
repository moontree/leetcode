"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


Example 1:

Input:
    "IDID"
Output:
    [0,4,1,3,2]

Example 2:

Input:
    "III"
Output:
    [0,1,2,3]

Example 3:

Input:
    "DDI"
Output:
    [3,2,0,1]

Note:

    1 <= S.length <= 10000
    S only contains characters "I" or "D".
"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        res = []
        l, r = 0, len(S)
        for flag in S:
            if flag == 'D':
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
        res.append(l)
        return res


examples = [
    {
        "input": {
            "S": "IDID",
        },
        "output": [0, 4, 1, 3, 2]
    }, {
        "input": {
            "S": "III",
        },
        "output": [0, 1, 2, 3]
    }, {
        "input": {
            "S": "DDI",
        },
        "output": [3, 2, 0, 1]
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
