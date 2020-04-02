"""
Given two words (beginWord and endWord),
and a dictionary's word list,
 find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list.
 Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.
"""
import string
import collections


def find_ladders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """

    def recurse(word_list, cur, d=collections.defaultdict(list)):
        if not cur:
            return []
        if endWord in cur:
            return [[endWord]]
        word_list -= cur
        next_cur = set()
        I, L = range(len(beginWord)), string.ascii_lowercase
        for w in cur:
            for i in I:
                for l in L:
                    nw = w[:i] + l + w[i + 1:]
                    if nw in word_list:
                        next_cur.add(nw)
                        d[nw].append(w)
        res = []
        tmp = recurse(word_list, next_cur, d)
        for ww in tmp:
            for path in d[ww[0]]:
                res.append([path] + ww)
        return res
    return recurse(set(wordList), {beginWord})


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
    print find_ladders(example["beginWord"], example["endWord"], example["wordList"])
