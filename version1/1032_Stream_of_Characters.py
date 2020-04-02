"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1,
the last k characters queried (in order from oldest to newest,
including this letter just queried)
spell one of the words in the given list.


Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"])
streamChecker.query('a')
streamChecker.query('b')
streamChecker.query('c')
streamChecker.query('d')
streamChecker.query('e')
streamChecker.query('f')
streamChecker.query('g')
streamChecker.query('h')
streamChecker.query('i')
streamChecker.query('j')
streamChecker.query('k')
streamChecker.query('l')


Note:

    1 <= words.length <= 2000
    1 <= words[i].length <= 2000
    Words will only consist of lowercase English letters.
    Queries will only consist of lowercase English letters.
    The number of queries is at most 40000.
"""


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = {}
        for word in words:
            cur = self.root
            for c in word[::-1]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = True
        self.q = ""

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.q = letter + self.q
        cur = self.root
        for c in self.q:
            if c not in cur:
                return False
            cur = cur[c]
            if '#' in cur:
                return True

        return False


if __name__ == '__main__':
    streamChecker = StreamChecker(["cd", "f", "kl"])
    print(streamChecker.root)
    print streamChecker.query('a')
    print streamChecker.query('b')
    print streamChecker.query('c')
    print streamChecker.query('d')
    print streamChecker.query('e')
    print streamChecker.query('f')
    print streamChecker.query('g')
    print streamChecker.query('h')
    print streamChecker.query('i')
    print streamChecker.query('j')
    print streamChecker.query('k')
    print streamChecker.query('l')
    print ('============')
    streamChecker = StreamChecker(["aab", "f", "kl"])
    print streamChecker.query('a')
    print streamChecker.query('a')
    print streamChecker.query('c')
    print streamChecker.query('a')
    print streamChecker.query('a')
    print streamChecker.query('a')
    print streamChecker.query('b')
    # word = "abababc"
    # prev = [-1]
    # for i in range(1, len(word)):
    #     p = prev[i - 1]
    #     while p > -1 and word[i] != word[p + 1]:
    #         p = prev[p]
    #     prev.append(p + 1)
    #
    # print prev
