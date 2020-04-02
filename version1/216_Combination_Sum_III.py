"""
Find all possible combinations of k numbers that add up to a number n,
 given that only numbers from 1 to 9 can be used and
 each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""


def combination_sum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    res = []
    dfs(k, 1, 10, [], 0, n, res)
    return res


def dfs(k, start, end, previous, previous_sum, target, res):
    if start > end:
        return
    if len(previous) == k:
        if previous_sum == target:
            res.append(previous[:])
    else:
        for i in range(start, end):
            previous.append(i)
            previous_sum += i
            dfs(k, i + 1, end, previous, previous_sum, target, res)
            previous_sum -= i
            previous.pop()


examples = [
    {
        "k": 3,
        "n": 7,
        "res": [[1, 2, 4]]
    }, {
        "k": 3,
        "n": 9,
        "res": [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    }, {
        "k": 1,
        "n": 19,
        "res": [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    }
]


for example in examples:
    print combination_sum3(example["k"], example["n"])
