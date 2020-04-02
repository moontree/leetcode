"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
You must use only standard operations of a queue -- which means only push to back,
 peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively.
 You may simulate a queue by using a list or deque (double-ended queue),
  as long as you use only standard operations of a queue.
You may assume that all operations are valid
 (for example, no pop or top operations will be called on an empty stack).
"""


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if len(self.queue1) == 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
            while len(self.queue1):
                self.queue2.append(self.queue1.pop(0))
            self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue1.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print param_2
print param_3
print param_4
