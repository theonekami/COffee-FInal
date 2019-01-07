import itertools
import random

def make_board(m=3):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m # Origin of mxm block
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])): 
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()

def set_board():
    x=make_board()
    u=x
    d=[]
    for i in range(0,25):
        t=[random.randint(0,8),random.randint(0,8)]
        while(t in d):
            t=[random.randint(0,8),random.randint(0,8)]
        d.append(t)
    for i in d:
        x[i[0]][i[1]]=" "
    y=[x,u]
    return y
