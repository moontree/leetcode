"""
Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
"""

examples = [
    {
        "x": 2.0,
        "y": 10,
        "res": 1024
    }, {
        "x": 2.1,
        "y": 3,
        "res": 9.26100
    }, {
        "x": 2,
        "y": -3,
        "res": 9.26100
    }
]


def my_power(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1 / x
    half = my_power(x, n / 2)
    if n % 2 == 1:
        return half * half * x
    else:
        return half * half


for example in examples:
    cache = {}
    print my_power(example["x"], example["y"])
