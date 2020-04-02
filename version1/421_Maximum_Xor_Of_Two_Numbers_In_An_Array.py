"""
Given a non-empty array of numbers, a0, a1, a2, ..., an-1 where 0 <= ai < 231.

Find the maximum result of ai XOR aj, where 0 <= i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
import collections


def find_maximum_xor(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # def Trie():
    #     return collections.defaultdict(Trie)
    #
    # root = Trie()
    # best = 0
    #
    # for num in nums:
    #     candidate = 0
    #     cur = this = root
    #     for i in range(32)[::-1]:
    #         curBit = num >> i & 1
    #         this = this[curBit]
    #         if curBit ^ 1 in cur:
    #             candidate += 1 << i
    #             cur = cur[curBit ^ 1]
    #         else:
    #             cur = cur[curBit]
    #     best = max(candidate, best)

    answer = 0
    for i in range(32)[::-1]:
        answer <<= 1
        prefixes = {num >> i for num in nums}
        answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
    return answer


examples= [
    {
        "nums": [3, 10, 5, 25, 2, 8],
        "res": 28
    }
]


for example in examples:
    print find_maximum_xor(example["nums"])