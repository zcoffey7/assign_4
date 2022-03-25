def new_board():
    empty_board = [
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
        ['8', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '8'],
        ['7', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '7'],
        ['6', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '6'],
        ['5', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '5'],
        ['4', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '4'],
        ['3', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '3'],
        ['2', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '2'],
        ['1', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '1'],
        [' ', '□', '□', '□', '□', '□', '□', '□', '□', ' ']
    ]
    return empty_board


def colour(board, square):
    row_l, col_l = (i for i in square)
    row = (ord(row_l) - 96)
    column = (9 - int(col_l))

    return board[column][row][1]


def count_pieces(board, colour):
    count = 0
    for i in board:
        for n in i:
            try:
                if n[1] == colour:
                    count += 1
            except:
                None

    return count


def piece(board, square):
    row_l, col_l = (i for i in square)
    row = (ord(row_l) - 96)
    column = (9 - int(col_l))
    toy = board[column][row][0]
    if toy == "□":
        return None
    else:
        return toy



def place_piece(board, square, colour, piece):
    row_l, col_l = (i for i in square)
    row = (ord(row_l) - 96)
    column = (9 - int(col_l))
    board[column][row] = [piece, colour]


def pretty(board):
    proj_board = []
    for i in board:
        v = []
        for n in i:
            try:
                v.append(n[0])
            except:
                v.append(n)
        proj_board.append(v)

    for i in proj_board:
        print(' '.join(i))
