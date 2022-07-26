from src.checking_funcs import sep_row, sep_col, sep_box

DIGITS = set((1,2,3,4,5,6,7,8,9))

def check_rows_correctness(board):
    for i in range(9):
        if sum(sep_row(board, i*9)) != 45 or set(sep_row(board, i*9)) != DIGITS:
            return False
    
    return True

def check_cols_correctness(board):
    for i in range(9):
        if sum(sep_col(board, i)) != 45 or set(sep_col(board, i)) != DIGITS:
            return False
    
    return True

def check_boxs_correctness(board):
    for i in range(3):
        for j in range(3):
            if sum(sep_box(board, i*27 + j*3)) != 45 or set(sep_box(board, i*27 + j*3)) != DIGITS:
                return False
    
    return True

def check_board_correctness(board):
    if (not check_rows_correctness(board)
        or not check_cols_correctness(board)
        or not check_boxs_correctness(board)):
        return False
    return True


