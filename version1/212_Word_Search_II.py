"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
 where "adjacent" cells are those horizontally or vertically neighboring.
 The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].

"""


def find_words(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    trie = {}
    for w in words:
        t = trie
        for c in w:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = '#'
    m, n = len(board), len(board[0])
    res = []
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            dfs(board, trie, i, j, "", res, visited)
    return list(set(res))


def dfs(board, trie, i, j, pre, res, visited):
    if '#' in trie:
        res.append(pre)
    if -1 < i < len(board) and -1 < j < len(board[0]):
        if visited[i][j]:
            return
        else:
            c = board[i][j]
            pre += board[i][j]
            if c in trie:
                visited[i][j] = True
                dfs(board, trie[c], i, j - 1, pre, res, visited)
                dfs(board, trie[c], i, j + 1, pre, res, visited)
                dfs(board, trie[c], i - 1, j, pre, res, visited)
                dfs(board, trie[c], i + 1, j, pre, res, visited)
                visited[i][j] = False
    else:
        return


examples = [
    {
        "board": [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ],
        "words": ["oath", "pea", "eat", "rain"],
    },
    {
        "board": [
            ['a', 'b'],
            ['a', 'a']
        ],
        "words": ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"],
        "res": ["aaa", "aaab", "aaba", "aba", "baa"]
    }
]


for example in examples:
    print find_words(example["board"], example["words"])
