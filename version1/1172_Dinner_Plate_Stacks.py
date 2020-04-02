# --*-- encoding: utf-8 --*--
"""
=========================
Project -> File: leetcode -> 1172_Dinner_Plate_Stacks.py
Author: zhangchao
=========================
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0,
each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

    DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
    void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
    int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack,
    and returns -1 if all stacks are empty.
    int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack,
    and returns -1 if the stack with that given index is empty.

Example:

Input:
    ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
    [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output:
    [None,None,None,None,None,None,2,None,None,20,21,5,4,3,1,-1]

Explanation:
    DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
    D.push(1);
    D.push(2);
    D.push(3);
    D.push(4);
    D.push(5);         // The stacks are now:  2  4
                                               1  3  5
                                               ﹈ ﹈ ﹈
    D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                           1  3  5
                                                           ﹈ ﹈ ﹈
    D.push(20);        // The stacks are now: 20  4
                                               1  3  5
                                               ﹈ ﹈ ﹈
    D.push(21);        // The stacks are now: 20  4 21
                                               1  3  5
                                               ﹈ ﹈ ﹈
    D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                            1  3  5
                                                            ﹈ ﹈ ﹈
    D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                            1  3  5
                                                            ﹈ ﹈ ﹈
    D.pop()            // Returns 5.  The stacks are now:      4
                                                            1  3
                                                            ﹈ ﹈
    D.pop()            // Returns 4.  The stacks are now:   1  3
                                                            ﹈ ﹈
    D.pop()            // Returns 3.  The stacks are now:   1
                                                            ﹈
    D.pop()            // Returns 1.  There are no stacks.
    D.pop()            // Returns -1.  There are still no stacks.


Constraints:

    1 <= capacity <= 20000
    1 <= val <= 20000
    0 <= index <= 100000
    At most 200000 calls will be made to push, pop, and popAtStack.
"""
import heapq


class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.empty = []
        self.stacks = [[]]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.empty and (self.empty[0] >= len(self.stacks) or len(self.stacks[self.empty[0]]) == self.capacity):
            heapq.heappop(self.empty)
        if self.empty:
            idx = self.empty[0]
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) == self.capacity:
                heapq.heappop(self.empty)
        else:
            if len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].append(val)
            else:
                self.stacks.append([val])

    def pop(self):
        """
        :rtype: int
        """
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if self.stacks:
            return self.stacks[-1].pop()
        return -1

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.stacks):
            return -1
        if self.stacks[index]:
            heapq.heappush(self.empty, index)
            return self.stacks[index].pop()
        return -1


examples = [
    {
        "input": {
            "op": ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack",
     "pop", "pop", "pop", "pop", "pop"],
            "args": [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
        },
        "output": [None, None, None, None, None, None, 2, None, None, 20, 21, 5, 4, 3, 1, -1]
    }
]

import time

if __name__ == '__main__':

    for example in examples:
        print '----------'
        start = time.time()
        n = len(example["output"])
        obj = DinnerPlates(example['input']['args'][0][0])
        for i in range(1, n):
            if example['input']['args'][i]:
                str_v = 'obj.%s(%d)' % (example['input']['op'][i], example['input']['args'][i][0])
            else:
                str_v = 'obj.%s()' % (example['input']['op'][i])
            print str_v, eval(str_v), example['output'][i]
            # print obj.stacks, obj.stack_num
        end = time.time()
