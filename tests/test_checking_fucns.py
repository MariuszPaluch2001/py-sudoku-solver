from src.checking_funcs import sep_row, row_check, sep_col, col_check, sep_box, box_check

board = [0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         1,2,3,4,5,6,7,8,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,3,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,]

def test_sep_row():
    
    assert list(sep_row(board, 18)) == [1,2,3,4,5,6,7,8,0]
    assert list(sep_row(board, 26)) == [1,2,3,4,5,6,7,8,0]

    assert list(sep_row(board, 45)) == [0,0,3,0,0,0,0,0,0]
    assert list(sep_row(board, 53)) == [0,0,3,0,0,0,0,0,0]

def test_row_check():

    assert row_check(board, 26, 9)
    assert not row_check(board, 26, 8)

    assert row_check(board, 45, 4)
    assert not row_check(board, 45, 3)

def test_sep_col():
    assert list(sep_col(board, 2)) == [0, 0, 3, 0, 0, 3, 0, 0, 0]

def test_sep_box():
    assert list(sep_box(board, 0)) == [0,0,0,0,0,0,1,2,3]