"""
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


examples = [
    {
        "num": "1432219",
        "k": 3,
        "res": "1219"
    }, {
        "num": "10200",
        "k": 1,
        "res": "200"
    }, {
        "num": "10",
        "k": 2,
        "res": "0"
    }, {
        "num": "789456312",
        "k": 2,
        "res": "7456312"
    }, {
        "num": "789456312",
        "k": 3,
        "res": "456312"
    }, {
        "num": "9",
        "k": 1,
        "res": "0"
    }
]


def remove_k_digits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack = ["0"]
    i = 0
    deleted = 0
    while i < len(num) and deleted < k:
        if stack[-1] < num[i]:
            stack.append(num[i])
            i += 1
        else:
            while len(stack) and stack[-1] > num[i] and deleted < k:
                stack.pop()
                deleted += 1
            stack.append(num[i])
            i += 1
    while deleted < k:
        stack.pop()
        deleted += 1
    res = "".join(stack) + num[i:]
    for i in range(len(res)):
        if res[i] != "0":
            return res[i:]
    return "0"


for example in examples:
    print remove_k_digits(example["num"], example["k"])
