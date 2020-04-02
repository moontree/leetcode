"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    try:
        while fast:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    except:
        return False
