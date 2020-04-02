"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""
import itertools


def is_additive_number(num):
    """
    :type num: str
    :rtype: bool
    """
    n = len(num)
    for i, j in itertools.combinations(range(1, n), 2):
        a, b = num[:i], num[i:j]
        if a != str(int(a)) or b != str(int(b)):
            continue
        else:
            while j < n:
                c = str(int(a) + int(b))
                if not num[j:].startswith(c):
                    break
                else:
                    j += len(c)
                    a, b = b, c
            if j == n:
                return True
    return False


examples = [
    {
        "num": "112358",
        "res": True
    }
]


for example in examples:
    print is_additive_number(example["num"])