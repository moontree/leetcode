"""
A string S of lowercase letters is given.
Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left),
remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.



Example 1:

Input:
    S = "cba", K = 1
Output:
    "acb"
Explanation:
    In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
    In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".

Example 2:

Input:
    S = "baaca", K = 3
Output:
    "aaabc"
Explanation:
    In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
    In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".


Note:

1 <= K <= S.length <= 1000
S consists of lowercase letters only.
"""

# if K > 1, we can get any permute of S


class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            res = S
            for i in range(1, len(S)):
                tmp = S[i:] + S[:i]
                if res > tmp:
                    res = tmp
            return res
        if K > 1:
            chars = [c for c in S]
            chars.sort()
            return ''.join(chars)


examples = [
    {
        "input": {
            "S": "cba",
            "K": 1
        },
        "output": "acb"
    }, {
        "input": {
            "S": "baaca",
            "K": 3
        },
        "output": "aaabc"
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
