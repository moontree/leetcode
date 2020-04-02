# --*-- coding: utf-8 --*--
"""
In the computer world,
use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively.
 On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s.
Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""


def find_max_form(strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    records = []
    for s in strs:
        records.append((s.count("0"), s.count("1")))
    records.sort()
    memo = [[[None for _ in xrange(n + 1)] for _ in xrange(m + 1)] for _ in xrange(len(strs))]

    def dfs(index, m, n):
        print index, m, n
        if m < 0 or n < 0:
            return -float("inf")
        if index < len(records):
            a, b = records[index]
            memo[index][m][n] = max(dfs(index + 1, m, n), 1 + dfs(index + 1, m - a, n - b))
            return memo[index][m][n]
        else:
            return 0

    return dfs(0, m, n)


examples = [
    {
        "input": {
            "strs": ["10", "0001", "111001", "1", "0"],
            "m": 5,
            "n": 3
        },
        "output": 4
    }, {
        "input": {
            "strs": ["10", "0", "1"],
            "m": 1,
            "n": 1
        },
        "output": 2
    }
]


for example in examples:
    print find_max_form(**example["input"])
