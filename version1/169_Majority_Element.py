"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than n / 2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    e, c = None, -1
    for p in nums:
        if e is None:
            e, c = p, 1
        else:
            if p == e:
                c += 1
            else:
                c -= 1
                if c == 0:
                    e, c = p, 1
    return e


examples = [
    {
        "nums": [1, 2, 1, 3, 3, 4, 3, 3],
        "res": 3,
    }, {
        "nums": [1, 2, 1],
        "res": 1
    }, {
        "nums": [1],
        "res": 1
    }
]


for example in examples:
    print majority_element(example["nums"])
