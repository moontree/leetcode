"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
1. 123
2. 132
3. 213
4. 231
5. 312
6. 321
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


def get_permutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    k = k - 1
    nums = [1]
    res = ""
    for i in range(1, n):
        nums.append(nums[-1] * i)
    indexes = []
    for i in range(n, 0, -1):
        index = k / nums[i - 1]
        k = k % nums[i - 1]
        indexes.append(index)
    print indexes
    rest = range(1, n + 1)
    for i in indexes:
        res += str(rest[i])
        rest.pop(i)
    return res


print get_permutation(5, 120)
