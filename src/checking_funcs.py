def sep_row(board, pos_idx):
    row_idx = pos_idx // 9
    return board[row_idx*9: row_idx*9 + 9]

def row_check(board ,pos_idx ,value):
    return not any(value == i for i in sep_row(board, pos_idx))

def sep_col(board, pos_idx):
    col_idx = pos_idx % 9
    return (board[i*9 + col_idx] for i in range(9))

def col_check(board ,pos_idx ,value):
    ...

def box_check():
    ...