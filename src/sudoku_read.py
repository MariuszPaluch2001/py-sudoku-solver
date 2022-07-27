
def read_sudoku_file(filename):
    """
    File should be located in folder "sudoku_samples".
    Cells in sudoku should be separate with space, can
    by group by line or all board can be in single line.
    """
    with open("sudoku_samples/" + filename) as f:
        return f.read().split()

def load_sudoku_from_file(filename):
    return list(map(int, read_sudoku_file(filename)))
