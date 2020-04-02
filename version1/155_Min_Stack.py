"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    _stack = []
    _min_stack = [float('inf')]
    def __init__(self):
        self._stack = []
        self._min_stack = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        self._min_stack.append(min(x, self._min_stack[-1]))

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()
        self._min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_stack[-1]
