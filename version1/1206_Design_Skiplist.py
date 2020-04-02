"""
=========================
Project -> File: leetcode -> 1206_Design_Skiplist.py
Author: zhangchao
=========================
Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time to add, erase and search.
Comparing with treap and red-black tree which has the same function and performance,
the code length of Skiplist can be comparatively short and the idea behind Skiplists are just simple linked lists.

For example:
we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it.
The Skiplist works this way:


Artyom Kalinin [CC BY-SA 3.0],
via Wikimedia Commons

You can see there are many layers in the Skiplist.
Each layer is a sorted linked list.
With the help of the top layers, add , erase and search can be faster than O(n).
It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

To be specific, your design should include these functions:

bool search(int target) : Return whether the target exists in the Skiplist or not.
void add(int num): Insert a value into the SkipList.
bool erase(int num): Remove a value in the Skiplist.
    If num does not exist in the Skiplist, do nothing and return false.
    If there exists multiple num values, removing any one of them is fine.
See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.



Example:

    Skiplist skiplist = new Skiplist();

    skiplist.add(1);
    skiplist.add(2);
    skiplist.add(3);
    skiplist.search(0);   // return false.
    skiplist.add(4);
    skiplist.search(1);   // return true.
    skiplist.erase(0);    // return false, 0 is not in skiplist.
    skiplist.erase(1);    // return true.
    skiplist.search(1);   // return false, 1 has already been erased.

Constraints:

    0 <= num, target <= 20000
    At most 50000 calls will be made to search, add, and erase.
"""
import random


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.down = None
        self.cnt = 1


class Skiplist(object):

    def __init__(self):
        left = [Node(-1) for _ in range(16)]
        right = [Node(65535) for _ in range(16)]
        for i in range(16):
            left[i].right = right[i]
            if i < 15:
                left[i].down = left[i + 1]
                right[i].down = right[i + 1]
        self.root = left[0]

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        cur = self.root
        while cur:
            if cur.val == target:
                return True
            if cur.right and cur.right.val <= target:
                cur = cur.right
            else:
                cur = cur.down
        return False

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        cur = self.root
        path = []
        while cur:
            while num >= cur.right.val:
                cur = cur.right
            path.append(cur)
            cur = cur.down
        prev = None
        for x in path[::-1]:
            node = Node(num)
            node.right = x.right
            x.right = node
            node.down = prev
            prev = node
            prob = random.random()
            if prob < 0.5:
                break

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        current = self.root
        is_removed = False
        while current:
            if current.val < num <= current.right.val:
                if current.right.val == num:
                    current.right = current.right.right
                    is_removed = True
                current = current.down
            else:
                current = current.right
        return is_removed

    def print_self(self):
        head = self.root
        for i in range(16):
            cur = head
            print 'layer', i, ':',
            while cur:
                print (cur.val, cur.down.val if cur.down else None),
                cur = cur.right
            head = head.down
            print ''


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
import time

if __name__ == '__main__':
    skiplist = Skiplist()
    print('------------')
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    skiplist.add(2)
    print skiplist.search(0) # return false.
    print skiplist.search(1) # return True.
    print skiplist.search(2) # return True.
    print skiplist.search(6) # return False.
    skiplist.add(4)
    print skiplist.erase(0) # return false, 0 is not in skiplist.
    print skiplist.erase(1)  #return true.
    print skiplist.search(1) # return false
    a = '[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,true,null,true,null,null,true,true,false,true,true,true,false,false,false,false,false,null,false,true,false,false,true,null,false,true,true,null,false,false,false,true,null,false,null,false,null,true,null,true,false,false,null,true,true,false,false,null,false,false,true,null,false,true,false,true,null,null,null,true,false,false,false,false,true,null,true,null,false,false,false,false,false,null,false,null,null,true,false,false,true,true,true,null,false,null,true,false,false,false,true,false,false,true,true,true,false,false,null,true,null,null,null,null,null,false,null,true,false,true,null,null,false,null,true,true,true,true,true,false,true,false,false,false,true,false,true,true,true,false,true,true,true,true,true,false,true]'
    b = '[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,true,null,true,null,null,true,true,false,true,true,true,false,false,false,false,false,null,false,true,false,false,true,null,false,true,true,null,false,false,false,true,null,false,null,false,null,true,null,true,false,false,null,true,true,false,false,null,false,false,true,null,false,true,false,true,null,null,null,true,false,false,false,false,true,null,true,null,false,false,false,false,false,null,false,null,null,true,false,false,true,true,true,null,false,null,true,false,false,false,true,false,false,true,true,true,false,false,null,true,null,null,null,null,null,false,null,true,false,true,null,null,false,null,true,true,true,true,true,false,true,false,false,false,true,false,true,true,true,false,true,true,true,true,true,false,true]'
    for x, y in zip(a.split(','), b.split(',')):
        if x != y:
            print x, y