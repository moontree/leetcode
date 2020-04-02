"""
Given an integer array of size n,
find all elements that appear more than n / 3 times.
The algorithm should run in linear time and in O(1) space.
"""


def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    a, b = None, None
    na, nb = 0, 0
    for v in nums:
        if a is None and b != v:
            a = v
            na += 1
        elif b is None and a != v:
            b = v
            nb += 1
        else:
            if v == a:
                na += 1
            elif v == b:
                nb += 1
            else:
                na -= 1
                nb -= 1
                if na == 0:
                    a = None
                if nb == 0:
                    b = None
    res = []
    na = 0
    nb = 0
    for v in nums:
        if v == a:
            na += 1
        if v == b:
            nb += 1
    if a is not None and na > len(nums) / 3:
        res.append(a)
    if b is not None and nb > len(nums) / 3:
        res.append(b)
    return res


examples = [
    {
        "nums": [1, 1, 2],
        "res": [1]
    }, {
        "nums": [1, 1, 2, 2, 3],
        "res": [1, 2]
    }, {
        "nums": [3, 3, 3, 1, 1, 2, 2, 4],
        "res": [3]
    }, {
        "nums": [-1, 1, 1, 1, 2, 1],
        "res": [1]
    }
]


for example in examples:
    print majority_element(example["nums"])
