"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:

*
**
**

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
*
**
***
**

Because the 4th row is incomplete, we return 3.

"""


def arrange_coins(n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 0, n
    while l <= r:
        mid = (l + r) / 2
        val = mid * (mid + 1) / 2
        if val <= n:
            l = mid + 1
        else:
            r = mid - 1
    return l - 1


print arrange_coins(1)
print arrange_coins(2)
print arrange_coins(5)
print arrange_coins(8)
print arrange_coins(6)
