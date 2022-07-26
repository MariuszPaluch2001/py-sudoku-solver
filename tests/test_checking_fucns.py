from src.checking_funcs import sep_row, row_check, sep_col, col_check, sep_box, box_check, is_correct

board = [0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         1,2,3,4,5,6,7,8,0,
         0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,
         0,0,3,0,0,0,0,0,0, # Repeating value in col 2
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

def test_col_check():

    assert col_check(board, 9, 5)
    assert not col_check(board, 38, 3)

def test_sep_box():

    assert list(sep_box(board, 0)) == [0,0,0,0,0,0,1,2,3]
    assert list(sep_box(board, 45)) == [0,0,0,0,0,0,0,0,3]

def test_box_check():

    assert box_check(board, 0 , 9) 
    assert not box_check(board, 0, 2)

    assert box_check(board, 45, 4)
    assert not box_check(board, 45, 3)

def test_is_correct():
    board2 = [0,0,0,0,0,0,1,0,0,
            0,0,0,0,0,0,0,3,0,
            1,2,3,4,5,6,7,8,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,3,0,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,]

    assert is_correct(board2, 7, 2)
    assert not is_correct(board2, 8, 7)
    assert not is_correct(board2, 6, 2)