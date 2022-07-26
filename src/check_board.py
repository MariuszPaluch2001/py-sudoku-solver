from src.checking_funcs import sep_row, sep_col, sep_box

def check_sum_rows(board):
    for i in range(9):
        if sum(sep_row(board, i*9)) != 45:
            return False
    
    return True

def check_sum_cols(board):
    for i in range(9):
        if sum(sep_col(board, i)) != 45:
            return False
    
    return True

def check_sum_boxs(board):
    for i in range(3):
        for j in range(3):
            if sum(sep_box(board, i*27 + j*3)) != 45:
                return False
    
    return True


def check_board_correctness(board):

    if (not check_sum_rows(board)
        or not check_sum_cols(board)
        or not check_sum_boxs(board)):
        return False

    return True