"""
Your car starts at position 0 and speed +1 on an infinite number line.
(Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following:
if your speed is positive then speed = -1 , otherwise speed = 1.
(Your position stays the same.)

For example,
after commands "AAR",
your car goes to positions 0->1->3->3,
and your speed goes to 1->2->4->-1.

Now for some target position,
say the length of the shortest sequence of instructions to get there.

Example 1:
Input:
    target = 3
Output:
    2
Explanation:
    The shortest instruction sequence is "AA".
    Your position goes from 0->1->3.

Example 2:
Input:
    target = 6
Output:
    5
Explanation:
    The shortest instruction sequence is "AAARA".
    Your position goes from 0->1->3->7->7->6.

Note:

    1 <= target <= 10000.
"""
import math


class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(target + 1)]
        dp[0] = 0
        for i in range(1, target + 1):
            for forward in range(1, int(math.log(i * 2, 2)) + 1):
                j = 2 ** forward - 1
                if j == i:
                    dp[i] = min(dp[i], forward)
                elif j > i:
                    dp[i] = min(dp[i], forward + 1 + dp[j - i])
                else:
                    for back in range(forward):
                        k = 2 ** back - 1
                        dp[i] = min(dp[i], dp[i - j + k] + forward + back + 2)
        print dp
        return dp[target]


examples = [
    {
        "input": {
            "target": 3,
        },
        "output": 2
    }, {
        "input": {
            "target": 6,
        },
        "output": 5
    }, {
        "input": {
            "target": 4,
        },
        "output": 5
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
