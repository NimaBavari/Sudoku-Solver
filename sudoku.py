"""
@app:       sudoku_solver

@author:    Nima Bavari <nima.bavari@gmail.com>
            https://github.com/NimaBavari

@desc:      A sudoku solver written with an original,
            non-backtracking algorithm.
"""

class SudokuSolver:
    """
    :params     sudoku_file => a file where an unsolved
                sudoku is put in a grid fashion with
                unknown cells denoted as dashes (-).
    """
    def __init__(self, sudoku_file):
        self.sudoku_file = sudoku_file

    def _to_list(self):
        try:
            with open(self.sudoku_file, 'r') as f:
                content = f.readlines()
        except IOError:
            print('Error: Failed to open sudoku from file.')
        content = [line.strip() for line in content]
        if len(content) != 9:
            raise Exception('Error: Too many or too few rows.')
        else:
            sudoku_list = []
            for line in content:
                if len(line) != 9:
                    raise Exception('Error: Too many or too few columns.')
                else:
                    for char in line:
                        if char == '-':
                            char = '0'
                        if not char.isdigit():
                            raise Exception('Error: Invalid char.')
                        else:
                            sudoku_list.append(char)
            return sudoku_list

    def _solve_sudoku(self):
        s_list = self._to_list()
        while '0' in s_list:
            for i in range(81):
                if s_list[i] == '0':
                    row = [s_list[k + i - (i % 9)] for k in range(9)]
                    column = [s_list[9 * k + (i % 9)] for k in range(9)]
                    square = []
                    for k in range(3):
                        for j in range(3):
                            square.append(s_list[(int((i - i % 9) / 9) -
                                                  int((i - i % 9) / 9) % 3 + k)
                                                 * 9 + (i % 9 - i % 3) + j])
                    candidates = set()
                    candidates.update(row)
                    candidates.update(column)
                    candidates.update(square)
                    candidates = {'1', '2', '3', '4', '5', '6', '7',
                                  '8', '9'}.difference(candidates)
                    if len(candidates) == 1:
                        s_list[i] = candidates.pop()
        return s_list

    def write_solution(self):
        sudoku = self._solve_sudoku()
        with open('solution.txt', 'w') as f:
            for i in range(81):
                f.write(sudoku[i])
                if i % 9 == 8 and not i == 80:
                    f.write('\n')


# test
s = SudokuSolver('sudoku.txt')
s.write_solution()
