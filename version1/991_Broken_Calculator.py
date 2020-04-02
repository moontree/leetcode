"""
On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.


Example 1:

Input:
    X = 2, Y = 3
Output:
    2
Explanation:
    Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:

Input:
    X = 5, Y = 8
Output:
    2
Explanation:
    Use decrement and then double {5 -> 4 -> 8}.

Example 3:

Input:
    X = 3, Y = 10
Output:
    3
Explanation:
    Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Example 4:

Input:
    X = 1024, Y = 1
Output:
    1023
Explanation:
    Use decrement operations 1023 times.


Note:
    1 <= X <= 10^9
    1 <= Y <= 10^9
"""


class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        step = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
            else:
                Y /= 2
            step += 1
        step += X - Y
        return step


examples = [
    {
        "input": {
            "X": 2,
            "Y": 3,
        },
        "output": 2
    }, {
        "input": {
            "X": 5,
            "Y": 8,
        },
        "output": 2
    }, {
        "input": {
            "X": 3,
            "Y": 10,
        },
        "output": 3
    }, {
        "input": {
            "X": 1024,
            "Y": 1,
        },
        "output": 1023
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
