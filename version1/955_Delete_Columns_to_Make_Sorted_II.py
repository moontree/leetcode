"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices,
and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3},
then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions,
the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.



Example 1:

Input:
    ["ca","bb","ac"]
Output:
    1
Explanation:
    After deleting the first column, A = ["a", "b", "c"].
    Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
    We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.

Example 2:

Input:
    ["xc","yb","za"]
Output:
    0
Explanation:
    A is already in lexicographic order, so we don't need to delete anything.
    Note that the rows of A are not necessarily in lexicographic order:
    ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)

Example 3:

Input:
    ["zyx","wvu","tsr"]
Output:
    3
Explanation:
    We have to delete every column.

Note:
    1 <= A.length <= 100
    1 <= A[i].length <= 100
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        r, c = len(A), len(A[0])

        def helper(j, pairs):
            # pairs: [s, e]
            if j == c:
                return 0
            if len(pairs) == len(A):
                return 0
            tmp = []
            for s, e in pairs:
                ss = s
                for i in range(s, e):
                    if A[i][j] == A[ss][j]:
                        continue
                    elif A[ss][j] > A[i][j]:
                        return 1 + helper(j + 1, pairs)
                    else:
                        tmp.append([ss, i])
                        ss = i
                tmp.append([ss, e])
            return helper(j + 1, tmp)

        return helper(0, [[0, len(A)]])


examples = [
    {
        "input": {
            "A": ["ca", "bb", "ac"],
        },
        "output": 1
    }, {
        "input": {
            "A":  ["xc", "yb", "za"],
        },
        "output": 0
    }, {
        "input": {
            "A": ["zyx", "wvu", "tsr"],
        },
        "output": 3
    }, {
        "input": {
            "A": ["bwwdyeyfhc", "bchpphbtkh", "hmpudwfkpw", "lqeoyqkqwe", "riobghmpaa", "stbheblgao", "snlaewujlc", "tqlzolljas", "twdkexzvfx", "wacnnhjdis"],
        },
        "output": 4
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
