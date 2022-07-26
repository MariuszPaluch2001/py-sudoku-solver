from src.checking_funcs import is_correct
from src.check_board import check_board_correctness
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

if __name__ == "__main__":
    board = [5,4,0,8,0,7,9,3,0,
             0,0,0,6,4,0,0,1,5,
             3,0,0,9,0,5,0,0,4,
             0,5,6,1,0,0,3,0,9,
             0,0,3,0,6,8,0,0,1,
             0,7,0,3,9,2,6,0,0,
             0,0,0,4,8,1,0,0,0,
             6,2,0,7,5,9,0,0,3,
             4,1,0,0,3,0,0,9,0]

    solve_sudoku(board)
    print_board(board)
    res = check_board_correctness(board)
    print(res)
    