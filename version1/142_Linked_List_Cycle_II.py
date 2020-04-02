"""
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


def detect_cycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    fast = slow = head
    step = 0
    find = False
    try:
        while fast:
            fast = fast.next.next
            slow = slow.next
            step += 1
            if fast == slow:
                find = True
                break
        if find:
            slow = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None
    except:
        return None
