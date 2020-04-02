"""
Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
 Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

"""
from list_helper import *
import random
import collections


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        cur = head
        self.nums = []
        while cur:
            self.nums.append(cur.val)
            cur = cur.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        step = random.randint(0, len(self.nums) - 1)
        return self.nums[step]

    def _get_random_of_stream(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        h = self._head
        if h is None:
            return None
        count = 0
        res = h.val
        while h:
            rv = random.randint(0, count)
            if rv == 0:
                res = h.val
            h = h.next
            count += 1
        return res


head = ListNode(1);
head.next = ListNode(2);
head.next.next = ListNode(3);
solution = Solution(head);
for i in xrange(5):
    print solution.getRandom()
