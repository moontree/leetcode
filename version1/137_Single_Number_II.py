"""
Given an array of integers,
 every element appears three times except for one,
 which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # a, b = 0, 0
    # for n in nums:
    #     a, b = ~a & n | a & ~(b & n), (a & n) ^ b
    # return a
    ans = 0
    for i in range(32):
        count = 0
        for n in nums:
            count += ((n >> i) & 0x1)
        ans |= (count % 3) << i
    return ans if ans < pow(2, 31) else ans - pow(2, 32)


examples = [
    {
        "nums": [5, 5, 5, 7, 6, 6, 6]
    }, {
        "nums": [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
    }
]


for example in examples:
    print single_number(example["nums"])
