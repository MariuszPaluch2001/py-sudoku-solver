import random
from src.checking_funcs import sep_row, sep_col, sep_box
from src.utilities import print_board
from src.check_board import check_board_correctness
from src.utilities import solve_sudoku

def empty_board_generate():
    return [0 for _ in range(81)]

def sudoku_soluntion_generate():
    board = empty_board_generate()
    solve_sudoku(board)
    return board

def add_empty_cells(board, numb_empty_cells):
    while(numb_empty_cells):
        rand_idx = random.randint(0, 80)
        if board[rand_idx]:
            board[rand_idx] = 0
            numb_empty_cells -= 1
    
    return board

def generate_sudoku(empty_cells):
    board = sudoku_soluntion_generate()
    add_empty_cells(board, empty_cells)
    return board
