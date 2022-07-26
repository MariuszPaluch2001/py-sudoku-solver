from src.utilities import find_empty_cell, solve_sudoku
from src.check_board import check_board_correctness

def test_find_empty_cell():
    testing_list = [1,2,0,4,5,6]

    assert find_empty_cell(testing_list) == 2

    testing_full_list = [1,2,3,4,5,6,7,8,9]

    assert find_empty_cell(testing_full_list) is None

def test_solve_sudoku():
    solvable_board = [5,4,0,8,0,7,9,3,0,
                      0,0,0,6,4,0,0,1,5,
                      3,0,0,9,0,5,0,0,4,
                      0,5,6,1,0,0,3,0,9,
                      0,0,3,0,6,8,0,0,1,
                      0,7,0,3,9,2,6,0,0,
                      0,0,0,4,8,1,0,0,0,
                      6,2,0,7,5,9,0,0,3,
                      4,1,0,0,3,0,0,9,0]
    
    res = solve_sudoku(solvable_board)
    
    assert res
    assert check_board_correctness(solvable_board)
    
    un_solvable_board = [5,4,0,8,0,7,9,3,1, # Last element is initialy wrong
                         0,0,0,6,4,0,0,1,5,
                         3,0,0,9,0,5,0,0,4,
                         0,5,6,1,0,0,3,0,9,
                         0,0,3,0,6,8,0,0,1,
                         0,7,0,3,9,2,6,0,0,
                         0,0,0,4,8,1,0,0,0,
                         6,2,0,7,5,9,0,0,3,
                         4,1,0,0,3,0,0,9,0]

    res = solve_sudoku(un_solvable_board)

    assert not res
    assert not check_board_correctness(un_solvable_board)