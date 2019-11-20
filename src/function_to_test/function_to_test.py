def function(L):
	def new_grid():
		return [['' for i in range(3)] for j in range(3)]

	def is_empty(grid, i, j):
		return grid[i][j] == ''

	def mark_case(grid, i, j, mark):
			b = is_empty(grid, i, j)
			if b:
				grid[i][j] = mark
			return b, grid
	
	return (mark_case(*L))