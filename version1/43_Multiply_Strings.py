'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

examples = [
    {
        "input":{
            "num1": "312",
            "num2": "123"
        },
        "output": str(312 * 123)
    },{
        "input":{
            "num1": "0",
            "num2": "4124140"
        },
        "output": str(0 * 4124140)
    }
]
import numpy as np

def multiply2(nums, num):
    res = [0]* len(nums)
    c = 0
    for i in range(len(nums)):
        tmp = nums[i] * num + c
        res[i] = tmp % 10
        c = tmp / 10
    if c > 0:
        res.append(c)
    return res

def add(num1, num2):
    count = max(len(num1), len(num2))
    res = [0] * count
    c = 0
    for i in range(count):
        n1 = n2 = 0
        if i < len(num1):
            n1 = num1[i]
        if i < len(num2):
            n2 = num2[i]
        tmp = n1 + n2 + c
        res[i] = tmp % 10
        c = tmp / 10
    if c > 0:
        res.append(c)
    return res

def adds(nums):
    max_len = max([len(i) for i in nums])
    for num in nums:
        num += [0] * (max_len - len(num))
    c = 0
    res = [0] * max_len
    for i in range(max_len):
        tmp = sum([num[i] for num in nums]) + c
        res[i] = tmp % 10
        c = tmp / 10
    while c > 0:
        res.append(c % 10)
        c = c / 10
    return res

def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    n1 = [int(i) for i in num1][::-1]
    n2 = [int(i) for i in num2][::-1]
    res = [0]
    middle = []
    for i in range(len(n2)):
        mul_res = multiply2(n1, n2[i])
        middle.append([0] * i + mul_res)
    res = adds(middle)
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    ans = "".join([str(i) for i in res[::-1]])
    return ans

for example in examples:
    print multiply(example["input"]["num1"], example["input"]["num2"]), example["output"]