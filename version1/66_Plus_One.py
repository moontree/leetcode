"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


def plus_one(digits):
    c = 1
    for i in range(len(digits) - 1, -1, -1):
        tmp = digits[i] + c
        digits[i] = tmp % 10
        c = tmp / 10
    if c > 0:
        digits = [c] + digits
    return digits


examples = [
    {
        "digits": [0],
        "res": [1]
    }, {
        "digits": [9, 9],
        "res": [1, 0, 0]
    }, {
        "digits": [0],
        "res": [1]
    }
]


for example in examples:
    print plus_one(example["digits"])
