"""
Alice and Bob have candy bars of different sizes:
A[i] is the size of the i-th bar of candy that Alice has,
and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends,
they would like to exchange one candy bar each so that after the exchange,
they both have the same total amount of candy.
(The total amount of candy a person has is the sum of the sizes of candy bars they have.)


Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange,
and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers,
you may return any one of them.
It is guaranteed an answer exists.



Example 1:

Input:
    A = [1,1],
    B = [2,2]
Output:
    [1,2]

Example 2:

Input:
    A = [1,2],
    B = [2,3]
Output:
    [1,2]

Example 3:

Input:
    A = [2], B = [1,3]
Output:
    [2,3]

Example 4:

Input:
    A = [1,2,5],
    B = [2,4]
Output:
    [5,4]

Note:

    1 <= A.length <= 10000
    1 <= B.length <= 10000
    1 <= A[i] <= 100000
    1 <= B[i] <= 100000
    It is guaranteed that Alice and Bob have different total amounts of candy.
    It is guaranteed there exists an answer.
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        cache = {b for b in B}
        ta, tb = sum(A), sum(B)
        target = (ta + tb) / 2
        diff = ta - target
        for a in A:
            if a - diff in cache:
                return [a, a - diff]


examples = [
    {
        "input": {
            "A": [1, 1],
            "B": [2, 2]
        },
        "output": [1, 2]
    }, {
        "input": {
            "A": [1, 2],
            "B": [2, 3]
        },
        "output": [1, 2]
    }, {
        "input": {
            "A": [2],
            "B": [1, 3]
        },
        "output": [2, 3]
    }, {
        "input": {
            "A": [1, 2, 5],
            "B": [2, 4]
        },
        "output": [5, 4]
    }, {
        "input": {
            "A": [35, 17, 4, 24, 10],
            "B": [63, 21],

        },
        "output": [24, 21]
    },
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