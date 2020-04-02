"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.


"""


def compare(a, b):
    ab, ba = a + b, b + a
    if ab < ba:
        return 1
    elif ab > ba:
        return -1
    return 0


def largest_number(nums):
    num = [str(x) for x in nums]
    num.sort(cmp=lambda x, y: cmp(y + x, x + y))
    return "".join(num).lstrip('0') or '0'


examples = [
    {
        "nums": [9, 30, 34, 5, 3],
        "res": "9534330"
    }, {
        "nums": [0, 0],
        "res": "0"
    }
]


for example in examples:
    print largest_number(example["nums"])
