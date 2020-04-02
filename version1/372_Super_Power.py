"""
Your task is to calculate ab mod 1337 where a is a positive integer
 and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
"""


def super_pow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    res = 1
    base = a % 1337
    for v in b[::-1]:
        bit_mod = 1
        new_base = 1
        for i in xrange(10):
            new_base = new_base * base % 1337
            if i < v:
                bit_mod = new_base
        print base, bit_mod
        res = (res * bit_mod) % 1337
        base = new_base
    return res


def super_pow_2(a, b):
    result = 1
    for digit in b:
        result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
    return result


examples = [
    {
        "input": {
            "a": 2,
            "b": [3]
        },
        "output": 8
    }, {
        "input": {
            "a": 2,
            "b": [1, 0]
        },
        "output": 1024
    }, {
        "input": {
            "a": 1,
            "b": [4,3,3,8,5,2]
        },
        "output": 1024
    }
]


for example in examples:
    print "-----"
    print super_pow(**example["input"])
