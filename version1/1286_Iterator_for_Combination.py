"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and
a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.idx = 0
        self.strings = []

        def helper(prefix):
            if len(prefix) == combinationLength:
                self.strings.append(''.join([characters[i] for i in prefix]))
                return
            start = 0
            if prefix:
                start = prefix[-1] + 1
            for i in range(start, len(characters)):
                prefix.append(i)
                helper(prefix)
                prefix.pop()
        helper([])
        self.strings.sort()

    def next(self):
        """
        :rtype: str
        """
        self.idx += 1
        return self.strings[self.idx - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx == len(self.strings):
            return False
        return True

# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("acb", 2)
print obj.next()
print obj.hasNext()