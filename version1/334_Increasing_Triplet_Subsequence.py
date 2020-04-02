"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""


def increasing_triplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    cache = [None, None, None]
    for n in nums:
        for i in xrange(3):
            v = cache[i]
            if v is None or n <= v:
                cache[i] = n
                break
    if cache[-1] is None:
        return False
    return True


examples = [
    {
        "nums": [1, 2, 3, 4, 5],
        "res": True
    }, {
        "nums": [5, 4, 3, 2, 1],
        "res": False
    }, {
        "nums": [4, 5, 1, 2, 3],
        "res": True
    }, {
        "nums": [4, 5, 1, 6],
        "res": True
    }
]


for example in examples:
    print increasing_triplet(example["nums"])
