class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    current = head
    while current and current.next:
        print current.val, '->',
        current = current.next
    if current:
        print current.val


def generate_list_from_array(nums):
    head = ListNode(-1)
    tail = head
    for p in nums:
        node = ListNode(p)
        tail.next = node
        tail = tail.next
    return head.next
