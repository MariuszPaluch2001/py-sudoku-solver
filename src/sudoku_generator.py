import random
from src.checking_funcs import sep_row, sep_col, sep_box
from src.utilities import print_board
from src.check_board import check_board_correctness
from utilities import solve_sudoku

DIGITS = set((1,2,3,4,5,6,7,8,9))

def get_correct_digits(board, pos_idx):
    return tuple(DIGITS - set(sep_row(board, pos_idx)) - set(sep_col(board, pos_idx)) - set(sep_box(board, pos_idx)))

def dummy_sudoku_generate(numb_filled_cells):
    dummy_board = [0 for _ in range(81)]
    empty_fields = set(range(0,81))

    for _ in range(numb_filled_cells):
        cell_to_fill = random.sample(empty_fields, 1)[0]
        possible_moves = get_correct_digits(dummy_board, cell_to_fill)
        if not possible_moves:
            return None
        value = random.choice(possible_moves)
        dummy_board[cell_to_fill] = value

    return dummy_board

if __name__ == "__main__":
    board = dummy_sudoku_generate(32)
    print("Dummy board:")
    print_board(board)
    output = solve_sudoku(board)
    print(f"Output: {output}")
    if output:
        print_board(board)
