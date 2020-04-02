"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
1, 2, 3, ..., n: num is g(n)
if i is root, num is f(i, n)
g(n) = sum(f(i, n))
f(i, n): 
left : 1, 2, ..., i - 1
right : i + 1, ..., n
"""


def num_trees(n):
    """
    :type n: int
    :rtype: int
    """
    nums = [1, 1]
    if n < 2:
        return 1
    else:
        for j in range(2, n + 1):
            res = 0
            for i in range(1, j + 1):
                res += nums[i - 1] * nums[j - i]
            nums.append(res)
        return nums[-1]


print num_trees(3)
