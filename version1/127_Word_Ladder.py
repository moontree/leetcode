"""
Given two words (beginWord and endWord),
 and a dictionary's word list,
 find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note that beginWord is not a transformed word.

For example,
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).
 Please reload the code definition to get the latest changes.
"""
import string


def dis(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count


def ladder_length(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    left, right, wordList = {beginWord}, {endWord}, set(wordList)
    if endWord not in wordList:
        return 0
    I, L = range(len(beginWord)), string.ascii_lowercase
    length = 1
    while left and right:
        if left & right:
            return length
        left, right = sorted([left, right], key=len)
        wordList -= left
        left = wordList & {W[:i] + l + W[i + 1:] for l in L for i in I for W in left}
        length += 1
    return 0


examples = [
    {
        "wordList": ["hot", "dot", "dog", "lot", "log", "cog"],
        "beginWord": "hit",
        "endWord": "cog",
        "res": 5
    },  {
        "wordList": ["hot", "dot", "dog", "lot", "log", "cog"],
        "beginWord": "aet",
        "endWord": "cog",
        "res": 0
    },  {
        "wordList": ["hot", "cog", "dot", "dog", "hit", "lot", "log"],
        "beginWord": "hit",
        "endWord": "cog",
        "res": 5
    },  {
        "wordList": ["hot", "dot", "dog"],
        "beginWord": "hot",
        "endWord": "dot",
        "res": 2
    }
]


for example in examples:
    print ladder_length(example["beginWord"], example["endWord"], example["wordList"])
