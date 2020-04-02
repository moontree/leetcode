"""
You are given an array of positive and negative integers.
 If a number n at an index is positive, then move forward n steps.
 Conversely, if it's negative (-n), move backward n steps.
 Assume the first element of the array is forward next to the last element,
  and the last element is backward next to the first element.
  Determine if there is a loop in this array.
   A loop starts and ends at a particular index with more than 1 element along the loop.
   The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?


"""


def circular_array_loop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    step, idx, n = 0, 0, len(nums)
    for i, v in enumerate(nums):
        start, cur, step = i, i, 0
        flag = 1 if v > 0 else -1
        while True:
            ni = (n + nums[cur] + cur) % n
            if cur == ni:
                break
            else:
                cur = ni
            # print cur
            if nums[cur] * flag < 0:
                break
            step += 1
            if cur == start:
                break
        if step < 2:
            continue
        else:
            return True
    return False


examples = [
    {
        "nums": [2, -1, 1, 2, 2],
        "res": True
    }, {
        "nums": [-1, 2],
        "res": False
    }, {
        "nums": [-1, -2, -3, -4, -5],
        "res": True
    }, {
        "nums": [2, -1, 1, -2, -2],
        "res": False
    }
]


for example in examples:
    print "---"
    print circular_array_loop(example["nums"])
