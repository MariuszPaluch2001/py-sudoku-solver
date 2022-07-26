from src.utilities import solve_sudoku, print_board
from src.check_board import check_board_correctness

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
    print(f"\nIs board correct? {res}")