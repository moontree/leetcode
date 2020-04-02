class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.head = Node(-1)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.count <= index:
            return -1
        c = 0
        cur = self.head.next
        while cur:
            if c == index:
                return cur.val
            else:
                cur = cur.next
                c += 1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        cur = self.head
        self.count += 1
        node.next = cur.next
        node.prev = cur
        cur.next = node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        self.count += 1
        cur = self.head
        while cur.next:
            cur = cur.next
        node.prev = cur
        cur.next = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.count:
            return
        elif index == self.count:
            self.addAtTail(val)
        else:
            c = 0
            cur = self.head
            while c < index:
                cur = cur.next
                c += 1
            node = Node(val)
            self.count += 1
            cur.next.prev = node
            node.next = cur.next
            node.prev = cur
            cur.next = node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.count:
            return
        c = 0
        cur = self.head
        while c < index:
            cur = cur.next
            c += 1
        if c == self.count - 1:
            cur.next = None
        else:
            cur.next.next.prev = cur
            cur.next = cur.next.next
        self.count -= 1

    def _print(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
        print None

examples = [
    {
        "operations": ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"],
        "params":[[],[1],[3],[1,2],[-1],[1],[-3]]
    }
]



for example in examples:
    obj = MyLinkedList()
    for i in range(1, len(example['operations'])):
        func = getattr(obj, example['operations'][i])
        if len(example['params']) == 1:
            val = func(obj, example['params'][0])
        elif len(example['params']) == 0:
            val = func(obj)
        obj._print()