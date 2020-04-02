"""
Given an array A,
we can perform a pancake flip:
We choose some positive integer k <= A.length,
then reverse the order of the first k elements of A.
We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.
Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



Example 1:

Input:
    [3,2,4,1]
Output:
    [4,2,4,3]
Explanation:
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.

Example 2:

Input:
    [1,2,3]
Output:
    []
Explanation:
    The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.

Note:

    1 <= A.length <= 100
    A[i] is a permutation of [1, 2, ..., A.length]
"""


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        r = len(A) - 1
        while r >= 0:
            while r and A[r] == r + 1:
                r -= 1
            if r == 0:
                break
            idx = A.index(r + 1)
            A[:idx + 1] = A[:idx + 1][::-1]
            A[:r + 1] = A[: r + 1][::-1]
            res.append(idx + 1)
            res.append(r + 1)
            r -= 1
        return res


examples = [
    {
        "input": {
            "A": [3, 2, 4, 1],
        },
        "output": [4, 2, 4, 3]
    }, {
        "input": {
            "A": [1, 2, 3]
        },
        "output": []
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
