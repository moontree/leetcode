"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
 A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.chars = {}


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_dfs(self.root, word)

    def search_dfs(self, node, word):
        res = False
        if len(word) == 0:
            if node.chars.get('#'):
                return True
            else:
                return False
        c = word[0]
        if c == ".":
            for key in node.chars:
                n = node.chars[key]
                res = res or self.search_dfs(n, word[1:])
            return res
        else:
            if node.chars.get(c):
                return self.search_dfs(node.chars.get(c), word[1:])
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("abc")
print obj.search("abc")
print obj.search("ab.")
print obj.search(".a")
print obj.search("..c")
