"""
On the first row, we write a 0.
Now in every subsequent row,
we look at the previous row and replace each occurrence of 0 with 01,
and each occurrence of 1 with 10.

Given row N and index K,
return the K-th indexed symbol in row N.
(The values of K are 1-indexed.) (1 indexed).

Examples:
Input:
    N = 1, K = 1
Output:
    0

Input:
    N = 2, K = 1
Output:
    0

Input:
    N = 2, K = 2
Output:
    1

Input:
    N = 4, K = 5
Output:
    1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:
N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1 or K == 1:
            return 0
        else:
            v = 2 ** (N - 2)
            if K <= v:
                return self.kthGrammar(N - 1, K)
            else:

                return 1 - self.kthGrammar(N - 1, K - v)


examples = [
    {
        "input": {
            "N": 1,
            "K": 1
        },
        "output": 0
    }, {
        "input": {
            "N": 2,
            "K": 1
        },
        "output": 0
    }, {
        "input": {
            "N": 2,
            "K": 2
        },
        "output": 1
    }, {
        "input": {
            "N": 4,
            "K": 5
        },
        "output": 1
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
