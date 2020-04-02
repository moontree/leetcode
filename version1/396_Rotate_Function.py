"""
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise,
we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""
"""
change think method, we can fix A and rotate F, as following
index_of_A  :   0   1   2   3   4   
F(0)        :   0   1   2   3   4
F(1)        :   1   2   3   4   0
F(2)        :   2   3   4   0   1
F(3)        :   3   4   0   1   2
F(4)        :   4   0   1   2   3
thus,
F(k) - F(k - 1) = sum(A) - n * A[n - k]
"""


def max_rotate_function(A):
    """
    :type A: List[int]
    :rtype: int
    """
    s, res, val = 0, 0, 0
    n = len(A)
    for i, v in enumerate(A):
        s += v
        val += i * v
    res = val
    for i in xrange(1, n):
        val = val + s - n * A[n - i]
        if res < val:
            res = val
    return res


examples = [
    {
        "A": [4, 3, 2, 6]
    }, {
        "A": [-2147483648,-2147483648]
    }, {
        "A": []
    }
]


for example in examples:
    print max_rotate_function(example["A"])
