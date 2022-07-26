from checking_funcs import sep_row, sep_col, sep_box

def check_sum_rows(board):
    for i in range(9):
        if sum(sep_row(board, i*9)) != 45:
            return False, i
    
    return True, None

def check_sum_cols(board):
    for i in range(9):
        if sum(sep_col(board, i)) != 45:
            return False, i
    
    return True, None

def check_sum_boxs(board):
    for i in range(3):
        for j in range(3):
            if sum(sep_box(board, i*27 + j*3)) != 45:
                return False, (i,j)
    
    return True, None


def check_board_correctness(board):
    is_correct, cord = check_sum_rows(board)
    if not is_correct:
        print(f"Incorrect row {cord}")
        return False

    is_correct, cord = check_sum_cols(board)
    if not is_correct:
        print(f"Incorrect column {cord}")
        return False

    is_correct, cord = check_sum_boxs(board)
    if not is_correct:
        print(f"Incorrect box {cord}")
        return False

    return True