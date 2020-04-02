# -*- coding: utf-8 -*-
"""
You are given two jugs with capacities x and y litres.
There is an infinite amount of water supply available.
You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable,
you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True

Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""


class Solution(object):

    def can_measure_water(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        else:
            if x == z or y == z or x + y == z:
                return True
        """ 
        如何操作：
        给定a, b, a < b, gcd(a,b) = 1
        从任意整数k, 连续取b个数，与a相乘，然后模b，可以获得0, 1, ..., b - 1 的b个数
        you can get all 0 to b - 1 by:
        ak % b
        k = [i, i + b) for any i
        反证法证明
        假设少了至少一个数，则必然有一个数被获得过两遍,
        k1 * a % b == k2 * a % b, k <= k1 < k2 < k + b
        a * d % b = 0, 0 < d < b, 
        a % (b / gcd(b, d)) = 0
        与 gcd(a, b) = 1矛盾
        """
        # cal gcd
        a, b = x, y
        if x > y:
            a, b = y, x
        while a:
            a, b = b % a, a
        return z % b == 0


examples = [
    {
        "input":{
            "x": 3,
            "y": 5,
            "z": 4,
        },
        "res": True
    }, {
        "input": {
            "x": 2,
            "y": 6,
            "z": 5,
        },
        "res": False
    }, {
        "input": {
            "x": 1,
            "y": 2,
            "z": 3,
        },
        "res": True
    }, {
        "input": {
            "x": 104659,
            "y": 104677,
            "z": 142424,
        },
        "res": True
    }
]


solution = Solution()
for example in examples:
    print "----"
    print solution.can_measure_water(**example["input"])
