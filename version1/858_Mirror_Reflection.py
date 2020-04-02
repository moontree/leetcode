"""
There is a special square room with mirrors on each of the four walls.
Except for the southwest corner,
there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p,
and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.
(It is guaranteed that the ray will meet a receptor eventually.)


Example 1:

Input:
p = 2, q = 1
Output:
2
Explanation:
The ray meets receptor 2 the first time it gets reflected back to the left wall.


2    1


N    0

Note:

1 <= p <= 1000
0 <= q <= p

"""

"""
mirror when refelect
"""
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def helper(a, b):
            # a >= b
            while b:
                a, b = b, a % b
            return a

        v = helper(p, q)
        v = p * q / v
        x = v / q
        y = v / p
        # a, b = None, 0
        # for i in range(x - 1):
        #     a, b = b, a
        # if b is None:
        #     a, b = None, 2
        # else:
        #     a, b = 0, 1
        # for i in range(y - 1):
        #     a, b = b, a
        # print b
        # return b
        if x % 2 == 0:
            return 2
        elif y % 2 == 0:
            return 0
        else:
            return 1


examples = [
    {
        "input": {
            "p": 2,
            "q": 1
        },
        "output": 2
    }, {
        "input": {
            "p": 6,
            "q": 4
        },
        "output": 0
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']