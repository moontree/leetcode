"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
 where "adjacent" cells are those horizontally or vertically neighboring.
 The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
"""

examples = [
    {
        "board": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "word": "ABCCED",
        "exist": True
    }, {
        "board": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "word": "CCBFDEC",
        "exist": True
    }, {
        "board": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'E', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "word": "ABCESEEEFS",
        "exist": True
    }
]


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if len(word) == 0:
        return True
    m = len(board)
    if m == 0 and len(word):
        return False
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if find_from_pos(board, i, j, word, 0):
                    return True
    return False


def find_from_pos(board, i, j, word, w):
    if w == len(word):
        return True
    if -1 < i < len(board) and -1 < j < len(board[0]) and board[i][j] == word[w]:
        tmp, board[i][j] = board[i][j], ""
        res = find_from_pos(board, i + 1, j, word, w + 1) or \
              find_from_pos(board, i - 1, j, word, w + 1) or \
              find_from_pos(board, i, j - 1, word, w + 1) or \
              find_from_pos(board, i, j + 1, word, w + 1)
        board[i][j] = tmp
        return res
    else:
        return False


for example in examples:
    print exist(example["board"], example["word"])
