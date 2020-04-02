"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0),
followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.



Example 1:

Input:
    "00110"
Output:
    1
Explanation:
    We flip the last digit to get 00111.

Example 2:

Input:
    "010110"
Output:
    2
Explanation:
    We flip to get 011111, or alternatively 000111.

Example 3:

Input:
    "00011000"
Output:
    2
Explanation:
    We flip to get 00000000.


Note:

    1 <= S.length <= 20000
    S only consists of '0' and '1' characters.
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        counts = []
        flag, count = None, 0
        for i, c in enumerate(S):
            if flag is None:
                flag, count = c, 1
            elif flag != c:
                counts.append([flag, count])
                flag, count = c, 1
            else:
                count += 1
        if count:
            counts.append([flag, count])
        n = len(counts)
        right = [0 for _ in range(len(counts) + 1)]
        for i in range(n)[::-1]:
            if counts[i][0] == "0":
                right[i] = right[i + 1] + counts[i][1]
            else:
                right[i] = right[i + 1]
        print right[:-1]
        res = len(S) + 1
        left = 0
        for i, [flag, nn] in enumerate(counts):
            res = min(res, left + right[i + 1])
            if flag == "1":
                left += nn
        return res


examples = [
    {
        "input": {
            "S": "00110",
        },
        "output": 1
    }, {
        "input": {
            "S": "010110",
        },
        "output": 2
    }, {
        "input": {
            "S": "00011000",
        },
        "output": 2
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
