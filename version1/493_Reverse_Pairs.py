"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
"""
import bisect


def reverse_pairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    def count(start, end):
        if start >= end:
            return 0
        mid = (end + start) / 2
        total_count = count(start, mid) + count(mid + 1, end)
        i, j = start, mid + 1
        while i <= mid:
            while j <= end and nums[i] > nums[j] * 2:
                j += 1
            total_count += j - (mid + 1)
            i += 1
        nums[start: end + 1] = sorted(nums[start: end + 1])
        return total_count

    return count(0, len(nums) - 1)
    # class Node:
    #     def __init__(self, val):
    #         self.val = val
    #         self.cnt = 1
    #         self.left = None
    #         self.right = None
    #
    # def search(root, val):
    #     if root is None:
    #         return 0
    #     elif root.val == val:
    #         return root.cnt
    #     elif root.val > val:
    #         return root.cnt + search(root.left, val)
    #     else:
    #         return search(root.right, val)
    #
    # def insert(root, val):
    #     if root is None:
    #         root = Node(val)
    #         return root
    #     if root.val == val:
    #         root.cnt += 1
    #     elif root.val < val:
    #         root.cnt += 1
    #         root.right = insert(root.right, val)
    #     else:
    #         root.left = insert(root.left, val)
    #     return root
    #
    # tree = None
    # res = 0
    # for n in nums:
    #     res += search(tree, n * 2 + 1)
    #     tree = insert(tree, n)
    # return res


examples = [
    {
        "nums": [1, 3, 2, 3, 1],
        "res": 2
    }, {
        "nums": [2, 4, 3, 5, 1],
        "res": 3
    }, {
        "nums": [-1, -1],
        "res": 1
    }
]


for example in examples:
    print "-----"
    print reverse_pairs(example["nums"])
