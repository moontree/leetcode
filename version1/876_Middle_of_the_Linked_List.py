"""
Given a non-empty,
singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input:
    [1,2,3,4,5]
Output:
    Node 3 from this list (Serialization: [3,4,5])
    The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
    Note that we returned a ListNode object ans, such that:
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input:
    [1,2,3,4,5,6]
Output:
    Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.
"""
import list_helper


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1, h2 = head, head
        while h2 and h2.next:
            h1 = h1.next
            h2 = h2.next
            if h2:
                h2 = h2.next
        return h1


examples = [
    {
        "input": {
            "nums": [1, 2, 3, 4, 5],
        },
        "output": 3
    }, {
        "input": {
            "nums": [1, 2, 3, 4, 5, 6],
        },
        "output": 4
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']

