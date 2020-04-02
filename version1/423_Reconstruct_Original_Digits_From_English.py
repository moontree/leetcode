"""
Given a non-empty string containing an out-of-order English representation of digits 0-9,
output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits.
 That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

"""


def original_digits(s):
    """
    :type s: str
    :rtype: str
    """
    records = {}
    for c in s:
        records[c] = records.get(c, 0) + 1
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    order = [[6, "x"], [7, "s"], [5, "v"], [8, "g"], [3, "h"], [4, "f"], [2, "t"], [0, "z"], [1, "o"], [9, "i"]]
    nums = [0] * 10
    for digit, c in order:
        count = records.get(c, 0)
        nums[digit] = count
        if count > 0:
            for c in digits[digit]:
                records[c] -= count
    res = "".join([str(i) * nums[i] for i in xrange(10)])
    return res


def original_digits_II(s):
    digits = [0] * 10
    # first pass digits
    digits[0] = s.count('z')
    digits[2] = s.count('w')
    digits[4] = s.count('u')
    digits[6] = s.count('x')
    digits[8] = s.count('g')
    # second pass digits
    digits[1] = s.count('o') - digits[0] - digits[2] - digits[4]
    digits[3] = s.count('h') - digits[8]
    digits[5] = s.count('f') - digits[4]
    digits[7] = s.count('s') - digits[6]
    # third pass digit
    digits[9] = s.count('i') - digits[5] - digits[6] - digits[8]

    number = ""
    for index in xrange(len(digits)):
        count = digits[index]
        if count > 0:
            number += count * str(index)
    return number


examples = [
    {
        "s": "owoztneoer",
        "res": "012"
    }, {
        "s": "fviefuro",
        "res": "45"
    }
]


for example in examples:
    print original_digits(example["s"])
