"""
Given a non-empty array of integers,
return the third maximum number in this array.
If it does not exist, return the maximum number.
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


def third_max(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a, b, c = -float("inf"), -float("inf"), -float("inf")
    for n in nums:
        if n == a or n == b or n == c:
            continue
        if n > a:
            a, b, c = n, a, b
        elif n > b:
            b, c = n, b
        elif n > c:
            c = n
        else:
            pass
    if c != -float("inf"):
        return c
    else:
        return a
examples = [
    {
        "nums": [1, 2, 3],
        "res": 1
    }, {
        "nums": [1, 2],
        "res": 1
    }, {
        "nums": [1, 2, 2, 3],
        "res": 1
    }
]


for example in examples:
    print third_max(example["nums"])