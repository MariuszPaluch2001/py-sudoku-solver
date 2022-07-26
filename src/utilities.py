from src.checking_funcs import is_correct
import random

def find_empty_cell(board):
    for index, elem in enumerate(board):
        if elem == 0:
            return index

def solve_sudoku(board):
    
    pos_idx = find_empty_cell(board)

    if pos_idx is None:
        return board

    shuffled_numbers = list(range(1, 10))
    random.shuffle(shuffled_numbers)

    for number in shuffled_numbers:
        
        if is_correct(board, pos_idx, number):
            board[pos_idx] = number

            if solve_sudoku(board):
                return True
            
            board[pos_idx] = 0

    return False

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i*9 + j], end= ' ')
        print()
    