'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''



examples = [
    {
        "input" : [[".","8","7","6","5","4","3","2","1"],
                   ["2",".",".",".",".",".",".",".","."],
                   ["3",".",".",".",".",".",".",".","."],
                   ["4",".",".",".",".",".",".",".","."],
                   ["5",".",".",".",".",".",".",".","."],
                   ["6",".",".",".",".",".",".",".","."],
                   ["7",".",".",".",".",".",".",".","."],
                   ["8",".",".",".",".",".",".",".","."],
                   ["9",".",".",".",".",".",".",".","."]],
        "output" : True
    }

]

'''
map each row, col, box to fix index
'''
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    return len(seen) == len(set(seen))


for example in examples:
    print isValidSudoku(example['input'])