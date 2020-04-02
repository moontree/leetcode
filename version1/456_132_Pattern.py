"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak
such that i < j < k and ai < ak < aj.
 Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


def find_132_pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    small, large = None, []
    for n in nums[::-1]:
        if large is None:
            large.append(n)
        else:
            if small and small > n:
                    return True
            while large and large[-1] < n:
                small = large.pop()
            large.append(n)
    return False


examples = [
    {
        "nums": [1, 2, 3, 4],
        "res": False
    }, {
        "nums": [3, 1, 4, 2],
        "res": True
    }, {
        "nums": [-1, 3, 2, 0],
        "res": True
    }, {
        "nums": [3, 5, 0, 3, 4],
        "res": True
    }, {
        "nums": [-2, 1, -2],
        "res": False
    }
]


for example in examples:
    print "-----"
    print find_132_pattern(example["nums"])
