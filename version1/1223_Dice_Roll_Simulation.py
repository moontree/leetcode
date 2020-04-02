"""
A die simulator generates a random number from 1 to 6 for each roll.
You introduced a constraint to the generator such that
it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n,
return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input:
    n = 2, rollMax = [1,1,2,2,2,3]
Output:
    34
Explanation:
    There will be 2 rolls of die, if there are no constraints on the die,
    there are 6 * 6 = 36 possible combinations.
    In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively,
    therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

Example 2:

Input:
    n = 2, rollMax = [1,1,1,1,1,1]
Output:
    30

Example 3:

Input:
    n = 3, rollMax = [1,1,1,2,2,3]
Output:
    181


Constraints:

    1 <= n <= 5000
    rollMax.length == 6
    1 <= rollMax[i] <= 15
"""


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        cache = {
            0: [0 for _ in range(6)],
            1: [1 for _ in range(6)]
        }

        base = 10 ** 9 + 7
        for l in range(2, n + 1):
            cache[l] = [0 for _ in range(6)]
            for cur in range(6):
                s = max(0, l - rollMax[cur])
                for i in range(s, l):
                    cache[l][cur] += sum(cache[i]) - cache[i][cur]
                    if i == 0:
                        cache[l][cur] += 1
                cache[l][cur] %= base
        return sum(cache[l]) % base


examples = [
    {
        "input": {
            "n": 2,
            "rollMax": [1, 1, 2, 2, 2, 3]
        },
        "output": 34
    }, {
        "input": {
            "n": 2,
            "rollMax": [1, 1, 1, 1, 1, 1]
        },
        "output": 30
    }, {
        "input": {
            "n": 3,
            "rollMax": [1, 1, 1, 2, 2, 3]
        },
        "output": 181
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
