"""
n passengers board an airplane with exactly n seats.
The first passenger has lost the ticket and picks a seat randomly.
But after that, the rest of passengers will:

    Take their own seat if it is still available,
    Pick other seats randomly when they find their seat occupied
What is the probability that the n-th person can get his own seat?



Example 1:

Input:
    n = 1
Output:
    1.00000
Explanation:
    The first person can only get the first seat.

Example 2:

Input:
    n = 2
Output:
    0.50000
Explanation:
    The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).

Constraints:
    1 <= n <= 10^5
"""


class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 1:
            return 0.5


examples = [
    {
        "input": {
            "n": 1,
        },
        "output": 1.0
    }, {
        "input": {
            "n": 3,
        },
        "output": 0.5
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
