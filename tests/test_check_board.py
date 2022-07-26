from src.check_board import check_rows_correctness, check_cols_correctness, check_boxs_correctness, check_board_correctness

bad_board = [1,3,3,3,3,3,7,8,9,
             9,8,7,6,5,4,3,2,1,
             1,2,3,4,5,6,7,8,9,
             9,8,7,6,5,4,3,2,1,
             1,2,3,4,5,6,7,8,9,
             9,8,7,6,5,4,3,2,1,
             1,2,3,4,5,6,7,8,9,
             9,8,7,6,5,4,3,2,1,
             1,2,3,4,5,6,7,8,9]

correct_board = [5, 4, 2, 8, 1, 7, 9, 3, 6, 
                 9, 8, 7, 6, 4, 3, 2, 1, 5, 
                 3, 6, 1, 9, 2, 5, 7, 8, 4, 
                 8, 5, 6, 1, 7, 4, 3, 2, 9, 
                 2, 9, 3, 5, 6, 8, 4, 7, 1, 
                 1, 7, 4, 3, 9, 2, 6, 5, 8, 
                 7, 3, 9, 4, 8, 1, 5, 6, 2, 
                 6, 2, 8, 7, 5, 9, 1, 4, 3, 
                 4, 1, 5, 2, 3, 6, 8, 9, 7]

def test_check_rows_correctness():
    assert not check_rows_correctness(bad_board)
    assert check_rows_correctness(correct_board)

def test_check_cols_correctness():
    assert not check_cols_correctness(bad_board)
    assert check_cols_correctness(correct_board)

def test_check_boxs_correctness():
    assert not check_boxs_correctness(bad_board)
    assert check_boxs_correctness(correct_board)

def test_check_board_correctness():
    assert not check_board_correctness(bad_board)
    assert check_board_correctness(correct_board)