"""
Given an array of integers,
find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t
and the absolute difference between i and j is at most k.

"""


def contains_nearby_almost_duplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    buckets = {}
    for i, v in enumerate(nums):
        bucket_num, offset = (v / t, 1) if t else (v, 0)
        for idx in range(bucket_num - offset, bucket_num + offset + 1):
            if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                return True
        buckets[bucket_num] = nums[i]
        if len(buckets) > k:
            # Remove the bucket which is too far away. Beware of zero t.
            del buckets[nums[i - k] / t if t else nums[i - k]]
    return False


examples = [
    {
        "nums": [1, 4, 7, 9, 2, 7],
        "k": 3,
        "t": 1,
        "res": True
    }
]


for example in examples:
    print contains_nearby_almost_duplicate(example["nums"], example["k"], example["t"])
