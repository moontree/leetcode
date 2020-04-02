"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.chars = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        start = self.root
        for c in word:
            if start.chars.get(c) is None:
                start.chars[c] = Node(c)
            start = start.chars.get(c)
        start.chars["#"] = Node("#")

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        start = self.root

        for c in word:
            if start.chars.get(c) is None:
                return False
            start = start.chars.get(c)
        return start.chars.get("#") is not None

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        start = self.root
        for c in prefix:
            if start.chars.get(c) is None:
                return False
            start = start.chars.get(c)
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
print obj.search("ab")
obj.insert("ab")
print obj.search("ab")

print obj.startsWith("")