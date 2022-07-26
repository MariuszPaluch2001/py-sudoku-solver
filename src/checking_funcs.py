def sep_row(board, pos_idx):
    row_idx = pos_idx // 9
    for i in range(row_idx*9,row_idx*9 + 9):
        yield board[i]

def row_check(board ,pos_idx ,value):
    return not any(value == i for i in sep_row(board, pos_idx))

def sep_col(board, pos_idx):
    col_idx = pos_idx % 9
    for i in range(9):
        yield board[i*9 + col_idx]

def col_check(board ,pos_idx ,value):
    return not any(value == i for i in sep_col(board, pos_idx))

def sep_box(board, pos_idx):
    row_idx = pos_idx // 9
    col_idx = pos_idx % 9
    for i in range(3):
        for j in range(3):
            yield board[(row_idx+i)*9 + col_idx + j]

def box_check():
    ...