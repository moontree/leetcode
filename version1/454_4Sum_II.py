"""
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
import bisect


def four_sum_count(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    AB, CD, count = {}, {}, 0
    for a in A:
        for b in B:
            val = a + b
            AB[val] = AB.get(val, 0) + 1
    for c in C:
        for d in D:
            val = c + d
            count += AB.get(-val, 0)
            # CD[val] = CD.get(val, 0) + 1
    ## use add instead of multiply, remove useless loop
    # for k in AB:
    #     count += AB[k] * CD.get(-k, 0)
    return count


examples = [
    {
        "input": {
            "A": [1, 2],
            "B": [-2, -1],
            "C": [-1, 2],
            "D": [0, 2]
        },
        "output": 2
    }
]

for example in examples:
    print four_sum_count(**example["input"])
