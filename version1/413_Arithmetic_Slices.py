"""
A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given.
 A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""


def number_of_arithmetic_slices(A):
    """
    :type A: List[int]
    :rtype: int
    """
    diffs = []
    for i in xrange(1, len(A)):
        diffs.append(A[i] - A[i - 1])
    lens = []
    diff, start = None, 0
    for i, v in enumerate(diffs):
        if diff is None:
            diff = v
        else:
            if diff == v:
                continue
            else:
                lens.append(i - start)
                start = i
                diff = v
    lens.append(len(diffs) - start)
    res = 0
    for v in lens:
        if v > 1:
            res += v * (v - 1) / 2
    return res


examples = [
    {
        "A": [1, 2, 3, 4],
        "res": 3
    }, {
        "A": [1,2,3,8,9,10],
        "res": 2
    }
]


for example in examples:
    print number_of_arithmetic_slices(example["A"])
