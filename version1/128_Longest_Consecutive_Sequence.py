"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def longest_consecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


examples = [
    {
        "nums": [100, 4, 200, 1, 2, 3],
        "res": 4
    }, {
        "nums": [0, -1],
        "res": 2
    }
]


for example in examples:
    print longest_consecutive(example["nums"])