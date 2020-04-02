"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
"""


def total_hamming_distance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # records = [0] * 33
    # for n in nums:
    #     for i, v in enumerate(bin(n)[2:][::-1]):
    #         if v == "1":
    #             records[i] += 1
    # return sum(n * (len(nums) - n) for n in records)
    res = 0
    for i in xrange(32):
        count = 0
        for n in nums:
            count += (n >> i) & 1
        res += count * (len(nums) - count)
    return res


examples = [
    {
        "nums": [4, 14, 2],
        "res": 6
    }, {
        "nums": [1, 2, 4, 6, 7],
        "res": 6
    }
]


for example in examples:
    print total_hamming_distance(example["nums"])
