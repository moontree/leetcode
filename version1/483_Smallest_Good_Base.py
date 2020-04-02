"""
For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

Example 1:
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
"""
import math


def smallest_good_base(n):
    """
    :type n: str
    :rtype: str
    """
    n = long(n)
    max_length = int(math.log(n, 2) + 1)
    for l in xrange(max_length, 1, -1):
        k = int(n ** (1.0 / (l - 1)))
        val = (k ** l - 1) / (k - 1)
        if val == n:
            return str(k)
    return str(n - 1)


examples = [
    {
        "n": "13",
        "res": "3",
    }, {
        "n": "4681",
        "res": "8",
    }, {
        "n": "1000000000000000000",
        "res": "999999999999999999",
    }, {
        "n": "2251799813685247",
        "res": "2",
    }, {
        "n": "727004545306745403",
        "res": "727004545306745402",
    }
]


for example in examples:
    print "----"
    print smallest_good_base(example["n"])
