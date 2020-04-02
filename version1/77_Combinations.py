"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if n < k or k == 0:
        return [[]]
    if k == n:
        return [range(1, n + 1)]
    if k == 1:
        return [[i] for i in range(1, n + 1)]
    else:
        res1 = combine(n - 1, k)
        res2 = combine(n - 1, k - 1)
        res = [[n] + p for p in res2]
        res += res1
        return res


print combine(4, 2)