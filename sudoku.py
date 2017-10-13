"""
@app:		Sudoku Solver

@author:	Nima Bavari <nima.bavari@gmail.com>

@desc:		A sudoku solver software written with an
			original, non-backtracking algorithm.
"""

def file_to_list(sudoku_file):

	"""
	Takes a file as input, where an unsolved sudoku is displayed
	in a grid fashion with unknown cells denoted as dashes (-),
	and converts it into a list of chars, replacing every instance
	of the dashes with a char '0'. Returns that list.
	"""

	try:
	    with open(sudoku_file, 'r') as f:
	        content = f.readlines()
	except:
		print('Error: Failed to open sudoku from file')

	content = [line.strip() for line in content]
	if not len(content) == 9:
		raise Exception('Error: Too many or too few sudoku rows')
	else:
		sudoku_list = []
		for line in content:
			if not len(line) == 9:
				raise Exception('Error: Too many or too few sudoku columns')
			else:
				for char in line:
					if char == '-':
						char = '0'

					if not char.isdigit():
						raise Exception('Error: Invalid character')
					else:
						sudoku_list.append(char)

		return sudoku_list


def solve_sudoku(s_file):

	"""
	Takes the list converted by the function file_to_list as input
	and, for each element of this list as a cell it determines the
	row, column, and the square that that cell is located. It then
	proceeds to identify the relevant value for each unsolved cell
	(char '0') and replaces it with that value. Returns this new
	list.
	"""

    s_list = file_to_list(s_file)
    while '0' in s_list:
	    for i in range(81):
	        if s_list[i] == '0':
	            row = [s_list[k + i - (i % 9)] for k in range(9)]
	            column = [s_list[9 * k + (i % 9)] for k in range(9)]
	            square = []
	            for k in range(3):
	                for j in range(3):
	                    square.append(s_list[(int((i - i % 9) / 9) - int((i - i % 9) / 9) % 3 + k) * 9 + (i % 9 - i % 3) + j])

	            candidates = set()
	            candidates.update(row)
	            candidates.update(column)
	            candidates.update(square)
	            candidates = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}.difference(candidates)
	            if len(candidates) == 1:
	                s_list[i] = candidates.pop()

    return s_list


def create_solution(file):

	"""
	Takes the list returned by the function solve_sudoku as input
	and writes it into a file in a grid fashion.
	"""

	sudoku = solve_sudoku(file)
	with open('solution.txt', 'w') as f:
		for i in range(81):
			f.write(sudoku[i])
			if i % 9 == 8 and not i == 80:
				f.write('\n')


create_solution('sudoku.txt')