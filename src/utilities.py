from src.checking_funcs import row_check, col_check, box_check

def find_empty_cell(board):
    for index, elem in enumerate(board):
        if elem == 0:
            return index
    

def find_empty_cell_none(board):
    for index, elem in enumerate(board):
        if elem == None:
            return index

def solve_sudoku(board):
    ...